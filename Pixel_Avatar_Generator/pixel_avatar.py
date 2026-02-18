"""
Generate a pixel-art avatar you can use on different platforms.
"""

from PIL import Image, ImageDraw
import random

# symmetry is needed to generate tasty avatars
symmetry = []
avatar_color = (255, 255, 255)
background_color = (0, 0, 0)


def create_square(border, draw, color, element, size):
    if element == size // 2:
        draw.rectangle(border, color)
    elif len(symmetry) == element + 1:
        used_color = symmetry.pop()
        draw.rectangle(border, used_color)
    else:
        symmetry.append(color)
        draw.rectangle(border, color)


def draw_avatar(border, draw, size):
    x0, y0, x1, y1 = border
    square_size = (x1 - x0) / size

    colors = [avatar_color, background_color]

    i = 1
    for y in range(0, size):
        i *= -1
        element = 0
        for x in range(0, size):
            top_left_x = x * square_size + x0
            top_left_y = y * square_size + y0
            bot_right_x = top_left_x + square_size
            bot_right_y = top_left_y + square_size
            create_square((top_left_x, top_left_y, bot_right_x, bot_right_y), draw, random.choice(colors), element, size)
            if element == size // 2 or element == 0:
                i *= -1
            element += i


def generate_avatar(pixel_size=9, image_size=400, target_folder='.', avatar_name='PixelAvatar'):
    original_dimension = image_size

    orig_image = Image.new('RGB', (original_dimension, original_dimension), color=background_color)
    draw = ImageDraw.Draw(orig_image)
    friend_size = original_dimension
    padding = friend_size / pixel_size

    top_left_x = padding / 2
    top_left_y = padding / 2
    bot_right_x = top_left_x + friend_size - padding
    bot_right_y = top_left_y + friend_size - padding
    draw_avatar((top_left_x, top_left_y, bot_right_x, bot_right_y), draw, pixel_size)

    orig_image.save("../{}/{}.png".format(target_folder, avatar_name))


if __name__ == '__main__':
    generate_avatar()
