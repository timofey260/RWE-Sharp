import os
import re
from PIL import Image



def CSSPaletizer(palette_name, input_string ):
    # Join the input string list into a single string if it's a list
    if isinstance(input_string, list):
        input_string = ' '.join(input_string)

    # Define a regular expression pattern for matching hex color codes
    hex_color_pattern = r'#[0-9A-Fa-f]{6}\b'

    # Find all matches in the input string
    matches = re.findall(hex_color_pattern, input_string)

    # Check if there are more colors in the string than in the color map
    if isinstance(palette_parser(palette_name), type) or not hasattr(palette_parser(palette_name), "__iter__"):
        raise ValueError("color_map must be an iterable object.")
    elif len(matches) > len(list(palette_parser(palette_name))):
        raise ValueError("Not enough predefined colors in color_map for all found hex colors.")

    # Create a dictionary to map each found color to its replacement
    color_replacements = {color: palette_parser(palette_name)[i] for i, color in enumerate(matches)}

    # Replace each color in the input string with its corresponding predefined color
    def replace_color(match):
        return color_replacements[match.group(0)]

    # Perform the replacements
    return re.sub(hex_color_pattern, replace_color, input_string)

def palette_parser(palette_name):
    image_path = r"C:\Users\ATOM\Documents\GitHub\RWE-Sharp\BaseMod\Palettes\Theme_palettes\pallette5.png" # TODO: OS PATH
    img = Image.open(image_path)
    img = img.convert("RGB")
    # Get the pixels as a list
    pixels = list(img.getdata())
    # Convert the pixels to hex format
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in pixels]
    return hex_colors




