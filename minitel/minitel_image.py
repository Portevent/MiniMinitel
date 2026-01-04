from random import random

from PIL import Image

from minitel.minitel_controller import MinitelController

def pseudo_random(min_value: int, max_value: int, bias = 1):
    return min_value + int((max_value - min_value) * (random() ** bias))

# Palette Minitel (8 couleurs) en RGB
minitel_palette = [
    (0, 0, 0),  # Noir
    (255, 0, 0),  # Rouge
    (0, 255, 0),  # Vert
    (255, 255, 0),  # Jaune
    (0, 0, 255),  # Bleu
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 255, 255)  # Blanc
]

pixel_to_g1_code = {
    "000000": "20", "100000": "21", "010000": "22", "110000": "23",
    "001000": "24", "101000": "25", "011000": "26", "111000": "27",
    "000100": "28", "100100": "29", "010100": "2A", "110100": "2B",
    "001100": "2C", "101100": "2D", "011100": "2E", "111100": "2F",
    "000010": "30", "100010": "31", "010010": "32", "110010": "33",
    "001010": "34", "101010": "35", "011010": "36", "111010": "37",
    "000110": "38", "100110": "39", "010110": "3A", "110110": "3B",
    "001110": "3C", "101110": "3D", "011110": "3E", "111110": "3F",
    "000001": "60", "100001": "61", "010001": "62", "110001": "63",
    "001001": "64", "101001": "65", "011001": "66", "111001": "67",
    "000101": "68", "100101": "69", "010101": "6A", "110101": "6B",
    "001101": "6C", "101101": "6D", "011101": "6E", "111101": "6F",
    "000011": "70", "100011": "71", "010011": "72", "110011": "73",
    "001011": "74", "101011": "75", "011011": "76", "111011": "77",
    "000111": "78", "100111": "79", "010111": "7A", "110111": "7B",
    "001111": "7C", "101111": "7D", "011111": "7E", "111111": "7F"
}

color_codes = {
    (0, 0, 0):       ("1B40", "1B50"),
    (255, 0, 0):     ("1B41", "1B51"),
    (0, 255, 0):     ("1B42", "1B52"),
    (255, 255, 0):   ("1B43", "1B53"),
    (0, 0, 255):     ("1B44", "1B54"),
    (255, 0, 255):   ("1B45", "1B55"),
    (0, 255, 255):   ("1B46", "1B56"),
    (255, 255, 255): ("1B47", "1B57")
}


minitel_color_names = {
    "Black": (0, 0, 0),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Yellow": (255, 255, 0),
    "Blue": (0, 0, 255),
    "Magenta": (255, 0, 255),
    "Cyan": (0, 255, 255),
    "White": (255, 255, 255)
}

class MinitelImage(MinitelController):

    def convert_image_to_minitel_palette(self, image):
        image = image.convert("RGB")
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                original_color = pixels[x, y]
                closest_color = min(minitel_palette,
                                    key=lambda color: sum((color[i] - original_color[i]) ** 2 for i in range(3)))
                pixels[x, y] = closest_color
        return image

    def get_preview_image(self, filepath, mode="resize", bg_color=(0, 0, 0)):
        image = Image.open(filepath)
        image = image.convert("RGB")
        target_width, target_height = 80, 72

        if mode == "resize":
            image = image.resize((target_width, target_height), Image.LANCZOS)
        elif mode == "center":
            iw, ih = image.size
            if iw > target_width or ih > target_height:
                scale_factor = min(target_width / iw, target_height / ih)
                new_width = int(iw * scale_factor)
                new_height = int(ih * scale_factor)
                image = image.resize((new_width, new_height), Image.LANCZOS)
                iw, ih = image.size
            new_img = Image.new("RGB", (target_width, target_height), bg_color)
            left = (target_width - iw) // 2
            top = (target_height - ih) // 2
            new_img.paste(image, (left, top))
            image = new_img

        image = self.convert_image_to_minitel_palette(image)
        return image

    def image_to_G1_row(self, filepath, mode="resize", bg_color=(0, 0, 0)):
        image = self.get_preview_image(filepath, mode, bg_color)
        mosaic_hex_list = []
        mosaic_hex = ""
        target_width, target_height = 80, 72
        for y in range(0, target_height, 3):
            for x in range(0, target_width, 2):
                block_pixels = [
                    image.getpixel((x, y)),
                    image.getpixel((x + 1, y)),
                    image.getpixel((x, y + 1)),
                    image.getpixel((x + 1, y + 1)),
                    image.getpixel((x, y + 2)),
                    image.getpixel((x + 1, y + 2))
                ]
                color_count = {}
                for pixel in block_pixels:
                    color_count[pixel] = color_count.get(pixel, 0) + 1
                sorted_colors = sorted(color_count.items(), key=lambda item: item[1], reverse=True)
                bg, fg = sorted_colors[0][0], (sorted_colors[1][0] if len(sorted_colors) > 1 else (255, 255, 255))
                if bg == fg:
                    fg = (0, 0, 0) if bg != (0, 0, 0) else (255, 255, 255)
                binary_string = ''.join(['1' if pixel == fg else '0' for pixel in block_pixels])
                g1_code = pixel_to_g1_code.get(binary_string, "7F")
                cell = color_codes[bg][1] + color_codes[fg][0] + g1_code
                mosaic_hex += cell
            mosaic_hex_list.append(mosaic_hex)
            mosaic_hex = ""
        return mosaic_hex_list

    def image_to_G1(self, filepath, mode="resize", bg_color=(0, 0, 0)):
        image = self.get_preview_image(filepath, mode, bg_color)
        mosaic_hex = ""
        target_width, target_height = 80, 72
        for y in range(0, target_height, 3):
            for x in range(0, target_width, 2):
                block_pixels = [
                    image.getpixel((x, y)),
                    image.getpixel((x + 1, y)),
                    image.getpixel((x, y + 1)),
                    image.getpixel((x + 1, y + 1)),
                    image.getpixel((x, y + 2)),
                    image.getpixel((x + 1, y + 2))
                ]
                color_count = {}
                for pixel in block_pixels:
                    color_count[pixel] = color_count.get(pixel, 0) + 1
                sorted_colors = sorted(color_count.items(), key=lambda item: item[1], reverse=True)
                bg, fg = sorted_colors[0][0], (sorted_colors[1][0] if len(sorted_colors) > 1 else (255, 255, 255))
                if bg == fg:
                    fg = (0, 0, 0) if bg != (0, 0, 0) else (255, 255, 255)
                binary_string = ''.join(['1' if pixel == fg else '0' for pixel in block_pixels])
                g1_code = pixel_to_g1_code.get(binary_string, "7F")
                cell = color_codes[bg][1] + color_codes[fg][0] + g1_code
                mosaic_hex += cell
        return mosaic_hex

    def showImage(self, filepath: str, mode="resize", bg_color=(0, 0, 0)):

        self._writeByte(b'\x1B\x3B\x60\x58\x52')
        self._writeByte(b'\x14')
        self.clearScreen()
        self.teletelModeOn()
        self._writeByte(b'\x1B\x3A\x6A\x43')

        bg_color = minitel_color_names.get(bg_color, (0, 0, 0)) if mode == "center" else (0, 0, 0)

        mosaic_hex = self.image_to_G1(filepath, mode, bg_color)
        data_bytes = bytes.fromhex(mosaic_hex)
        self._writeByte(data_bytes)


    def showImageBuggy(self, filepath: str, mode="resize", bg_color=(0, 0, 0)):

        self._writeByte(b'\x1B\x3B\x60\x58\x52')
        self._writeByte(b'\x14')
        self.clearScreen()
        self.teletelModeOn()
        self._writeByte(b'\x1B\x3A\x6A\x43')

        bg_color = minitel_color_names.get(bg_color, (0, 0, 0)) if mode == "center" else (0, 0, 0)

        mosaic_hex = self.image_to_G1_row(filepath, mode, bg_color)
        data_bytes = [bytes.fromhex(mosaic) for mosaic in mosaic_hex]
        for line in data_bytes:
            self._writeByte(line)

        queue = []

        empty = b'\x1bP\x1bG '

        while True:
            if len(queue) < 20:
                x_max_length = 12

                y = pseudo_random(2, len(data_bytes) - 2)
                x_start = pseudo_random(5, 40 - x_max_length)
                x_length = pseudo_random(4, x_max_length, 2)

                offset = pseudo_random(0, x_length, 3)

                glitch_instruction = (1+x_start, 1+y, y, 5*(x_start + offset), 5*(x_start+x_length), offset)
                display_instruction = (1+x_start, 1+y, y, 5*(x_start), 5*(x_start+x_length), 0)

                index = pseudo_random(min(len(queue), 5), len(queue))
                index2 = pseudo_random(index, len(queue))
                queue.insert(index, glitch_instruction)
                queue.insert(index2+1, display_instruction)

            dequeue_count = 0

            if len(queue) > 4:
                dequeue_count = 1
            if len(queue) > 10:
                dequeue_count = 4

            for dequeue in range(dequeue_count):
                x, y, line, fromByte, toByte, offset = queue.pop(0)
                self.cursorMove(x, y)
                for i in range(offset):
                    self._writeByte(empty)
                self._writeByte(data_bytes[line][fromByte:toByte])