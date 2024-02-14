import datetime
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def text_to_png(src: str) -> BytesIO:
    file = BytesIO()

    font_size = 24
    font = ImageFont.truetype(
        "./assets/ubuntu_mono.ttf", font_size
    )

    with Image.new("RGB", (0, 0)) as img:
        text_bbox = ImageDraw.Draw(img).multiline_textbbox(
            (0, 0), src, font=font
        )

    padding = 20
    image_width = text_bbox[2] - text_bbox[0] + padding
    image_height = text_bbox[3] - text_bbox[1] + padding

    image = Image.new("RGB", (image_width, image_height), color="black")
    draw = ImageDraw.Draw(image)
    draw.multiline_text(
        (padding // 2, padding // 2), src, fill="white", font=font
    )

    image.save(file, "png")
    file.name = f"deploy_result_{datetime.datetime.now()}.png"
    file.seek(0)
    return file
