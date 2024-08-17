import re
from PIL import Image
from PySide6.QtWidgets import QApplication
from RWESharp.Modify import Palette
from BaseMod.Palettes.qssfiles.darkeum import darkeum_qss
from BaseMod.Palettes.qssfiles.atmoled import atmoled_qss
from BaseMod.Palettes.qssfiles.Sharp import sharp_qss
from BaseMod.Palettes.qssfiles.Circular import circular_qss

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
        return darkeum_qss

        #CSSPaletizer("palette5.png", ) TODO, not thigs



def CSSPaletizer(palette_name, input_string):
    placeholder_mapping = {
        "{{background_dark}}": 0,
        "{{background_medium}}": 1,
        "{{background_light}}": 2,
        "{{text_light}}": 3,
        "{{border_dark}}": 4,
        "{{border_medium}}": 5,
        "{{border_accent}}": 6,
        "{{text_dark}}": 7,
        "{{text_disabled}}": 8,
        "{{highlight}}": 9,
        "{{highlight_selected}}": 10,
        "{{tab_background}}": 11,
        "{{tab_selected}}": 12,
        "{{progressbar_background}}": 13,
        "{{progressbar_chunk}}": 14,
        "{{slider_handle}}": 15,
        "{{slider_groove}}": 16,
        "{{slider_add_page}}": 17,
        "{{slider_sub_page}}": 18,
        "{{treeview_branch_selected}}": 19,
        "{{treeview_branch_hover}}": 20,
        "{{calendar_background}}": 21,
        "{{text_disabled_light}}": 22,
        "{{groupbox_title}}": 23,
        "{{dockwidget_title}}": 24,
        "{{lineedit_background}}": 25,
        "{{lineedit_border}}": 26,
        "{{spinbox_background}}": 27,
        "{{spinbox_border}}": 28,
        "{{radiobutton_checked}}": 29,
        "{{radiobutton_unchecked}}": 30,
        "{{combobox_background}}": 31,
        "{{combobox_border}}": 32,
        "{{scrollarea_background}}": 33,
        "{{scrollbar_vertical_handle}}": 34,
        "{{scrollbar_horizontal_handle}}": 35,
        "{{scrollbar_vertical_background}}": 36,
        "{{scrollbar_horizontal_background}}": 37,
        "{{scrollbar_add_page}}": 38,
        "{{scrollbar_sub_page}}": 39,
        "{{menu_background}}": 40,
        "{{menu_selected}}": 41,
        "{{menu_text}}": 42,
        "{{header_background}}": 43,
        "{{header_text}}": 44,
        "{{header_selected}}": 45,
        "{{dockwidget_titlebar_close_icon}}": 46,
        "{{dockwidget_titlebar_normal_icon}}": 47,
        "{{misc_color_48}}": 48,
        "{{misc_color_49}}": 49,
        "{{misc_color_50}}": 50,
        "{{misc_color_51}}": 51,
        "{{misc_color_52}}": 52,
        "{{misc_color_53}}": 53,
        "{{misc_color_54}}": 54,
        "{{misc_color_55}}": 55,
        "{{misc_color_56}}": 56,
        "{{misc_color_57}}": 57,
        "{{misc_color_58}}": 58,
        "{{misc_color_59}}": 59,
        "{{misc_color_60}}": 60,
        "{{misc_color_61}}": 61,
        "{{misc_color_62}}": 62,
        "{{misc_color_63}}": 63,
        "{{misc_color_64}}": 64,
        "{{misc_color_65}}": 65,
        "{{misc_color_66}}": 66,
        "{{misc_color_67}}": 67,
        "{{misc_color_68}}": 68,
        "{{misc_color_69}}": 69,
        "{{misc_color_70}}": 70,
        "{{misc_color_71}}": 71,
        "{{misc_color_72}}": 72,
        "{{misc_color_73}}": 73,
        "{{misc_color_74}}": 74,
        "{{misc_color_75}}": 75,
        "{{misc_color_76}}": 76,
        "{{misc_color_77}}": 77,
        "{{misc_color_78}}": 78,
        "{{misc_color_79}}": 79
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
    image_path = r"/BaseMod/Palettes/Theme_palettes/palette5.png"
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


