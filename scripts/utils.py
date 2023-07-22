from PIL import Image, ImageFont, ImageDraw
from tabulate import tabulate

def df_to_image( df, size=30 ):

    text = tabulate(
        tabular_data = df, headers='keys', showindex=False,
        tablefmt='psql', stralign='center', numalign='right' )

    l_lines = text.split('\n')
    hor_char_len = max([ len(line) for line in l_lines])
    ver_char_len = len(l_lines)

    PAD = 5
    PAD_FMT = int( PAD * size / 10 )
    WIDTH = int( size * hor_char_len * 0.57 ) + PAD_FMT * 2
    HEIGHT = int( size * ver_char_len * 0.9 ) + PAD_FMT * 2

    img_pil = Image.new(mode='RGB', size=(WIDTH, HEIGHT), color=(40,40,40))
    draw = ImageDraw.Draw(img_pil)

    font = ImageFont.truetype( font = 'consolas.ttf', size=size)

    draw.text( xy=(PAD_FMT, PAD_FMT), text=text, fill=(255, 255, 255), font=font )

    return img_pil