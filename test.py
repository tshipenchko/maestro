from PIL import Image, ImageDraw, ImageFont

command_output = """\
┌────┬──────────────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
│ id │ name             │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
└────┴──────────────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘
Module
┌────┬──────────────────────────────┬───────────────┬──────────┬──────────┬──────┬──────────┬──────────┬──────────┐
│ id │ module                       │ version       │ pid      │ status   │ ↺    │ cpu      │ mem      │ user     │
├────┼──────────────────────────────┼───────────────┼──────────┼──────────┼──────┼──────────┼──────────┼──────────┤
│ 0  │ pm2-logrotate                │ 2.7.0         │ 153703   │ online   │ 0    │ 0%       │ 64.2mb   │ root     │
└────┴──────────────────────────────┴───────────────┴──────────┴──────────┴──────┴──────────┴──────────┴──────────┘
"""

font_size = 24
font = ImageFont.truetype(
    "/home/user/project/maestro/assets/ubuntu_mono.ttf", font_size
)

with Image.new("RGB", (0, 0)) as img:
    text_bbox = ImageDraw.Draw(img).multiline_textbbox((0, 0), command_output, font=font)

padding = 20
image_width = text_bbox[2] - text_bbox[0] + padding
image_height = text_bbox[3] - text_bbox[1] + padding

image = Image.new("RGB", (image_width, image_height), color="black")
draw = ImageDraw.Draw(image)
draw.multiline_text((padding//2, padding//2), command_output, fill="white", font=font)

image.save("command_output.png")
