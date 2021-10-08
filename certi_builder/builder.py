import logging
import os
import re
from typing import Text, List

from PIL import Image, ImageDraw, ImageFont, ImageColor

import pandas as pd

logger = logging.getLogger(__name__)


def generate_certificate(
    certificate_image_path: Text,
    names_file_path: Text,
    text_color: Text,
    x_location: float,
    y_location: float,
    is_bold: bool,
    is_italics: bool,
    font_size: int,
    output_location: Text,
    font_file_path: Text,
):
    names_list = get_names(names_file_path)
    text_color = ImageColor.getcolor(text_color, "RGB")
    font = ImageFont.truetype(font_file_path, font_size)
    font_bold = ImageFont.truetype(os.getcwd() + "/fonts/Roboto-Bold.ttf", font_size)
    font_italic = ImageFont.truetype(
        os.getcwd() + "/fonts/Roboto-Italic.ttf", font_size
    )
    location = (x_location, y_location)
    for name in names_list:
        image = Image.open(certificate_image_path)
        drawImage = ImageDraw.Draw(image)
        if is_bold:
            drawImage.text(location, name, text_color, font=font_bold)
        elif is_italics:
            drawImage.text(location, name, text_color, font=font_italic)
        else:
            drawImage.text(location, name, text_color, font=font)

        image.save(f"{output_location}\certificate_{name}.png")


def get_names(names_path: Text) -> List:
    try:
        name_df = pd.read_excel(names_path)
        name_list = name_df["name"].tolist()
        return name_list
    except Exception as exception:
        logger.error(f"Error: {exception}")


def path_exist(file_path: Text, is_file: bool) -> (bool, Text):
    if is_file:
        if os.path.isfile(file_path):
            return True, "exists"
        else:
            return False, f"{file_path} not found"
    else:
        if os.path.isdir(file_path):
            return True, "exists"
        else:
            return False, f"{file_path} not found"


def validate_hex(hex_code: Text) -> bool:
    hex_pattern = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    compile_pattern = re.compile(hex_pattern)
    match = re.search(compile_pattern, hex_code)
    if match:
        return True
    else:
        return False
