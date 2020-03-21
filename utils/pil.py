from PIL import Image, ImageFont, ImageDraw


class ImgCreate:
    def __init__(self, img_path):
        photo = Image.open(img_path)
        width, height = Image.open(img_path).size
        self.transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        self.transparent.paste(photo, (0, 0))
        self.drawing = ImageDraw.Draw(self.transparent)

    def text_drawing(self, cordinate: tuple, text, color: tuple, font):
        """ Рисование текста """
        self.drawing.text(cordinate, text, fill=color, font=font)

    def img_save(self, name):
        """ Сохранение изображения """
        self.transparent.save(name)


def img_busstop(name_png: str, _data: list, name_png_first: str = 'png/таблица.png', cordinates_x: tuple = (60, 650, 1250),
                cordinate_y: int = 45, y_step: int = 92, color: tuple = (34, 34, 34), font: str = 'font/impact.ttf'):
    """ Рисования изображения с данными """
    img_tuls = ImgCreate(name_png_first)
    cordinate_y_ = cordinate_y
    font = ImageFont.truetype(font, 34)
    for value in _data:
        cordinate_y_ += y_step
        img_tuls.text_drawing((cordinates_x[0], cordinate_y_), value[0].capitalize(), color, font)
        img_tuls.text_drawing((cordinates_x[1], cordinate_y_), str(value[1][0]), color, font)
        img_tuls.text_drawing((cordinates_x[2], cordinate_y_), str(value[1][1]), color, font)
    img_tuls.img_save(name_png)
