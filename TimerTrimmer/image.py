from PIL import Image, ImageFont, ImageDraw
import textwrap

def overlay_text(
    day=int,
    text=str,
    *,
    image_path=str,
    save_path=str,
    ) -> None:
    """Add text over an image"""
    # Wrap the text
    wrap_cap_2xl = 305
    wrap_cap_xl = 225
    wrap_cap_lg = 100
    wrap_length_xl = 47
    wrap_length_lg = 38
    wrap_length_md = 29
    wrap_length_sm = 21
    image = Image.open(image_path)

    if (text_length:= len(text)) >= wrap_cap_2xl:
        print(day, text_length, "2xl")
        text = textwrap.fill(text, width=wrap_length_xl)
        image_size_ratio = image.size[0] * .010
    elif text_length >= wrap_cap_xl:
        print(day, text_length, "xl")
        text = textwrap.fill(text, width=wrap_length_lg)
        image_size_ratio = image.size[0] * .012
    elif text_length >= wrap_cap_lg:
        print(day, text_length, "lg")
        text = textwrap.fill(text, width=wrap_length_md)
        image_size_ratio = image.size[0] * .014
    else:
        print(day, text_length, "md")
        text = textwrap.fill(text, width=wrap_length_sm)
        image_size_ratio = image.size[0] * .020
        
    draw = ImageDraw.Draw(image)
    font_size = 1
    font = ImageFont.truetype("assets/Lato-BoldItalic.ttf", font_size)

    while font.getbbox(text)[1] < image_size_ratio:
        font_size += 1
        font = ImageFont.truetype("assets/Lato-BoldItalic.ttf", font_size)

    smallerfont = ImageFont.truetype("assets/Lato-BoldItalic.ttf", 30)
    draw.text((10, 100), f"#{day}", font=smallerfont, fill=(50, 50, 50, 5))
    draw.text((90, 100), text, font=font, fill=(50, 50, 50, 255))
    draw.text((400, 550), "#31DaysofNeurodivergence", font=smallerfont, fill=(250, 250, 250, 255))
    return image