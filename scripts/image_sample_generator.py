from PIL import Image, ImageFont, ImageDraw
import exercise_queries as eq

def text_to_image( text, size=30 ):

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


# for idx in range(1,45):
for idx in [13]:
    sql = getattr( eq, f'get_exercise_{idx}' )()
    output = eq.execute_sql(sql=sql)

    print(f'Index : {idx}\n')
    # print(output)
    img_pil = text_to_image(text=output)
    img_pil.show()

    break

    file_name = f'../images/sample_{idx:02d}.png'
    img_pil.save(file_name)
