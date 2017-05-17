from PIL import Image, ImageDraw, ImageFont
class EmojiGenerator():
    
    def __init__(self, word, color, font_path):
        self.color = color
        text_canvas = Image.new('RGB', (128, 128), (255, 255, 255))
        draw = ImageDraw.Draw(text_canvas)
        font = ImageFont.truetype(font_path, 15)
        draw.text((10, 10), word, font=font, self.hex_color())
        text_canvas.save("{}.png".format(name), 'PNG', quality=100, optimize=True)

    def hex_color(self):
        if isinstance(self.color, tuple):
            return self.color
        elif self.color = 'R' or 'red':
            return '#FF2600'
        elif self.color = 'G' or 'green':
            return '#22C350'
        elif self.color = 'B' or 'blue':
            return '#0c00cc'
        elif self.color = 'Br' or 'brown':
            return '#6B492D'
        else:
            return '#191919' # Black
