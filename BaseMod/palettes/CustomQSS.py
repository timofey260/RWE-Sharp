import os
import re
from BaseMod.Palettes.RaspberryDark import RaspberryDark
from PySide6.QtWidgets import QApplication
from RWESharp.Core import PATH_BASEMOD
from RWESharp.Modify import Theme

with open(r"C:\Users\ATOM\Documents\GitHub\RWE-Sharp\BaseMod\Palettes\qssfiles\sharp.txt") as file:
    current_theme = file.read()

color_map = RaspberryDark


class ThemeManager(Theme):
    def __init__(self, mod, widget=None):
        super().__init__("Moonlight Dark", mod)  # Example colors
        print(self.get_stylesheet())

        # Apply stylesheet to the QApplication instance if widget is None
        if widget is None:
            app = QApplication.instance()
            if app is not None:
                app.setStyleSheet(self.get_stylesheet())
            else:
                print("Error: QApplication instance not found.")

    def get_stylesheet(self):
        # with open(r"C:\Users\ATOM\Documents\GitHub\RWE-Sharp\BaseMod\Palettes\qssfiles\sharp.txt") as file:
        # TODO, not thigs
        print(CSSPaletizer(color_map, current_theme))
        return CSSPaletizer(color_map, current_theme)
placeholder_mapping = { }

def CSSPaletizer(palette_name, input_string):
      placeholder_mapping = {
           # base colors
           "@base_dark": 0,
           "@base_medium": 1,
           "@base_light": 2,
           "@text_misc": 3,
           # border
           "@border_dark": 4,
           "@border_medium": 5,
           "@border_light": 6,
           # text
           "@text_dark": 7,
           "@text_medium": 8,
           "@text_light": 9,
           "@text_disabled": 10,
           "@text_enabled": 11,
           # accents
           "@accent_light": 12,
           "@accent_medium": 13,
           "@accent_dark": 14,
           # color variations
           "@alt_base_dark": 15,
           "@alt_base_medium": 16,
           "@alt_base_light": 17,
           "@alt_text_misc": 18,
           "@alt_border_dark": 19,
           "@alt_border_medium": 20,
           "@alt_border_light": 21,
           "@alt_text_dark": 22,
           "@alt_text_medium": 23,
           "@alt_text_light": 24,
           "@alt_text_disabled": 25,
           "@alt_text_enabled": 26,
           "@alt_accent_light": 27,
           "@alt_accent_medium": 28,
           "@alt_accent_dark": 29,
           # specific colors
           "@misc_color_30": 30,
           "@misc_color_31": 31,
           "@misc_color_32": 32,
           "@misc_color_33": 33,
           "@misc_color_34": 34,
           "@misc_color_35": 35,
           "@misc_color_36": 36,
           "@misc_color_37": 37,
           "@misc_color_38": 38,
           "@misc_color_39": 39,
           "@misc_color_40": 40,
           "@misc_color_41": 41,
           "@misc_color_42": 42,
           "@misc_color_43": 43,
           "@misc_color_44": 44,
           "@misc_color_45": 45,
           "@misc_color_46": 46,
           "@misc_color_47": 47,
           "@misc_color_48": 48,
           "@misc_color_49": 49,
           "@misc_color_50": 50,
           "@misc_color_51": 51,
           "@misc_color_52": 52,
           "@misc_color_53": 53,
           "@misc_color_54": 54,
           "@misc_color_55": 55,
           "@misc_color_56": 56,
           "@misc_color_57": 57,
           "@misc_color_58": 58,
           "@misc_color_59": 59

       }
       # Define a fixed mapping of CSS placeholders to palette colors

    # Create a dictionary to map each placeholder to its corresponding color
    color_replacements = {key: color_map.get(str(idx)) for key, idx in placeholder_mapping.items() if idx is not None}

    # Replace placeholders in the input string with corresponding colors
    def replace_color(match):
        placeholder = match.group(0)
        return color_replacements.get(placeholder, placeholder)

    placeholder_pattern = r'@\w+@'
    return re.sub(placeholder_pattern, replace_color, input_string)
