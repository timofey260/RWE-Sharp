import re
from PIL import Image
from PySide6.QtWidgets import QApplication
from RWESharp.Modify import

Style = 3


class ThemeManager(Palette):
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
        return CSSPaletizer("palette5.png", CSSPaletizer())


def CSSPaletizer(palette_name, input_string):
    placeholder_mapping = {
        #base colors
        "{{base_dark}}": 0,
        "{{base_medium}}": 1,
        "{{base_light}}": 2,
        "{{text_misc}}": 3,
        #border
        "{{border_dark}}": 4,
        "{{border_medium}}": 5,
        "{{border_light}}": 6,
        #text
        "{{text_dark}}": 7,
        "{{text_medium}}": 8,
        "{{text_light}}": 9,
        "{{text_disabled}}":10,
        "{{text_enabled}}":11,
        #accents
        "{{accent_light}}": 12,
        "{{accent_medium}}": 13,
        "{{accent_dark}}": 14,
        #color variations
        "{{alt_base_dark}}": 15,
        "{{alt_base_medium}}": 16,
        "{{alt_base_light}}": 17,
        "{{alt_text_misc}}": 18,
        "{{alt_border_dark}}": 19,
        "{{alt_border_medium}}": 20,
        "{{alt_border_light}}": 21,
        "{{alt_text_dark}}": 22,
        "{{alt_text_medium}}": 23,
        "{{alt_text_light}}": 24,
        "{{alt_text_disabled}}": 25,
        "{{alt_text_enabled}}": 26,
        "{{alt_accent_light}}": 27,
        "{{alt_accent_medium}}": 28,
        "{{alt_accent_dark}}": 29,
        # specific colors
        "{{tab_background}}": 30,
        "{{tab_selected}}": 31,
        "{{progressbar_background}}": 32,
        "{{progressbar_chunk}}": 33,
        "{{slider_handle}}": 34,
        "{{slider_groove}}": 35,
        "{{slider_add_page}}": 36,
        "{{slider_sub_page}}": 37,
        "{{slider_page_indicator}}": 38,
        "{{slider_page_indicator_active}}": 39,
        "{{slider_page_indicator_disabled}}": 40,
        "{{slider_page_indicator_selected}}": 41,
        "{{treeview_branch_selected}}": 42,
        "{{treeview_branch_hover}}": 43,
        "{{calendar_background}}": 44,
        "{{text_disabled_light}}": 45,
        "{{groupbox_title}}": 46,
        "{{dockwidget_title}}": 47,
        "{{lineedit_background}}": 48,
        "{{misc_color_79}}": 49,
        "{{misc_color_80}}": 50,
        "{{misc_color_81}}": 51,
        "{{misc_color_82}}": 52,
        "{{misc_color_83}}": 53,
        "{{misc_color_84}}": 54,
        "{{misc_color_85}}": 55,
        "{{misc_color_86}}": 56,
        "{{misc_color_87}}": 57,
        "{{misc_color_88}}": 58,
        "{{misc_color_89}}": 59

    }
    # Define a fixed mapping of CSS placeholders to palette colors

    # Parse the palette image and get the colors in the order of the mapping
    color_map = {idx: color for idx, color in enumerate(palette_parser(palette_name))}
    print(color_map)
    # Create a dictionary to map each placeholder to its corresponding color
    color_replacements = {key: color_map.get(idx) for key, idx in placeholder_mapping.items() if idx is not None}

    # Replace placeholders in the input string with corresponding colors
    def replace_color(match):
        placeholder = match.group(0)
        return color_replacements.get(placeholder, placeholder)

    placeholder_pattern = r'{{\w+}}'
    return re.sub(placeholder_pattern, replace_color, input_string)


def palette_parser(palette_name):
    # Load the image from the path (Update with your correct path)
    image_path = r"C:\Users\ATOM\Documents\GitHub\RWE-Sharp\BaseMod\Palettes\Theme_palettes\palette5.png"
    img = Image.open(image_path)
    img = img.convert("RGB")

    # Get the pixels as a list
    pixels = list(img.getdata())

    # Assume a fixed number of slots (e.g., first 8 pixels are our palette slots)
    palette_slots = 256  # Update if you have more slots
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in pixels[:palette_slots]]

    return hex_colors


# Example usage


# Create the theme manager and get the styled CSS
theme_manager = ThemeManager(mod=None)
styled_css = theme_manager.get_stylesheet()
