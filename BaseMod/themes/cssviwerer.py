import re
from PIL import Image


def find_hex_colors(input_string):
    hex_pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'

    # Find all matches of the pattern in the input string
    hex_colors = re.findall(hex_pattern, input_string)

    return hex_colors


# Example usage
input_string = """
QToolTip {
    background-color: #3B3B3B;
    color: #D6D6D6;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 5px;
}
QMainWindow {
    background-color: #1E1E1E;
}
QMainWindow::separator {
    background-color: #505050;
    height: 2px;
}
QToolBar {
    background-color: #2B2B2B;
    border: 1px solid #505050;
    spacing: 4px;
}
QStatusBar {
    background-color: #1E1E1E;
    color: #D6D6D6;
    border-top: 1px solid #505050;
    padding: 4px;
}
QFrame {
    background-color: #1E1E1E;
    border: 0px solid #505050;
}
QGroupBox {
    background-color: #1E1E1E;
    border: 1px solid #505050;
    color: #D6D6D6;
    border-radius: 6px;
    margin-top: 10px;
}
QGroupBox::title {
    color: #4CAF50;
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
}
QPushButton {
    background-color: #2B2B2B;
    color: #D6D6D6;
    border: 1px solid #666666;
    padding: 8px;
    border-radius: 4px;
    transition: background-color 0.3s, border-color 0.3s;
}
QPushButton:hover {
    background-color: #3A3A3A;
    border-color: #7B7B7B;
}
QPushButton:pressed {
    background-color: #4CAF50;
    border-color: #4CAF50;
    color: #FFFFFF;
}
QCheckBox {
    color: #D6D6D6;
    padding: 4px;
}
QCheckBox::indicator {
    border: 1px solid #666666;
    width: 16px;
    height: 16px;
    border-radius: 3px;
    background-color: #2B2B2B;
}
QCheckBox::indicator:checked {
    background-color: #4CAF50;
    border: 1px solid #4CAF50;
}
QScrollBar:vertical, QScrollBar:horizontal {
    background: #1E1E1E;
    width: 15px;
    margin: 0px;
    border-radius: 7px;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #3A3A3A;
    min-height: 20px;
    border-radius: 7px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    background: #1E1E1E;
    height: 0px;
    width: 0px;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
QLineEdit {
    border-width: 1px;
    border-style: solid;
    border-color: #4CAF50;
    background-color: #252525;
    color: #D6D6D6;
    padding: 6px;
    border-radius: 4px;
}
QLabel {
    color: #D6D6D6;
}
QLCDNumber {
    color: #4CAF50;
}
QProgressBar {
    text-align: center;
    color: #D6D6D6;
    border-radius: 8px;
    background-color: #3A3A3A;
    border: 1px solid #4CAF50;
}
QProgressBar::chunk {
    background-color: #388E3C;
    border-radius: 8px;
}
QMenuBar {
    background-color: #1E1E1E;
    border-bottom: 1px solid #505050;
}
QMenuBar::item {
    color: #D6D6D6;
    padding: 6px 12px;
    background-color: transparent;
}
QMenuBar::item:selected {
    background-color: #333333;
    color: #FFFFFF;
    border-radius: 4px;
}
QMenu {
    background-color: #1E1E1E;
    border: 1px solid #505050;
}
QMenu::item {
    color: #D6D6D6;
    padding: 8px 20px;
}
QMenu::item:selected {
    background-color: #333333;
    color: #FFFFFF;
}
QTabWidget {
    color: #D6D6D6;
    background-color: #1E1E1E;
    border: 1px solid #505050;
}
QTabWidget::pane {
    border-color: #333333;
    background-color: #2B2B2B;
    border-radius: 6px;
    padding: 4px;
}
QTabBar::tab {
    border-style: solid;
    border-width: 1px;
    border-radius: 4px;
    border-color: #505050;
    color: #D6D6D6;
    padding: 6px;
    background-color: #2B2B2B;
}
QTabBar::tab:selected, QTabBar::tab:hover {
    color: #FFFFFF;
    background-color: #333333;
    border-color: #4CAF50;
}
QSlider::groove:horizontal, QSlider::groove:vertical {
    border: 1px solid #4CAF50;
    background: #3D3D3D;
    border-radius: 2px;
}
QSlider::handle:horizontal, QSlider::handle:vertical {
    background: #4CAF50;
    border: 1px solid #4CAF50;
    border-radius: 4px;
    width: 16px;
    height: 16px;
}
QTreeView, QListView, QTableView, QTableWidget, QTreeWidget {
    border: 1px solid #4CAF50;
    background-color: #252525;
    color: #D6D6D6;
    selection-background-color: #4CAF50;
    alternate-background-color: #1E1E1E;
}
QHeaderView::section {
    background-color: #1E1E1E;
    color: #D6D6D6;
    padding: 5px;
    border-style: solid;
    border-color: #1E1E1E;
    border-width: 0px 0px 1px 1px;
}
QHeaderView::section:selected, QHeaderView::section::checked {
    background-color: #333333;
}
QSplitter::handle {
    background-color: #252525;
}
QDockWidget {
  border: 1px solid #252525;
}
QDockWidget::title {
    text-align: left;
    background: #252525;
    padding-left: 6px;
    color: #4CAF50;
    border-radius: 4px;
}
QWidget {
    color: #D6D6D6;
    background-color: #252525;
    selection-background-color: #4CAF50;
}
QScrollArea {
    border: none;
}
QScrollArea, QWidget, QAbstractScrollArea, QWidget,
QScrollArea, QWidget, QAbstractScrollArea, QViewport {
    background-color: #252525;
}

QDockWidget::close-button, QDockWidget::float-button {
    border: 1px solid transparent;
    background: #357c38;
    border-radius: 5px;

}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: #4caf50;
    border-radius: 10px;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;

}

QDockWidget::title {
    text-align: left;
    background: #252525;
    padding-left: 1px;
    color: #4CAF50;
    border-radius: 8px;
}

QComboBox {
    border: 1px solid #4caf50;
    border-radius: 5px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
}


QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover{
    border: 1px solid #6dfb72;
    color: #eff0f1;
    border-radius: 2px;
}



QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 1px;
    border-left-color: #515151;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}
QComboBox::down-arrow {
    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);
}"""

result = find_hex_colors(input_string)

# Print the list of colors
print("Found hex colors:", result)

# Print the number of colors
print("Number of hex colors found:", len(result))


def hex_to_rgb(hex_color):
    """Convert a HEX color to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def create_image(hex_colors, size=(43, 2)):
    """Create an image from a list of HEX colors."""
    # Ensure the number of colors matches the required size
    if len(hex_colors) != size[0] * size[1]:
        raise ValueError(f"Number of colors ({len(hex_colors)}) does not match the image size ({size[0]}x{size[1]}).")

    # Create a new image with the specified size
    img = Image.new('RGB', size)
    pixels = img.load()

    # Convert HEX colors to RGB and populate the image
    for i, hex_color in enumerate(hex_colors):
        x = i % size[0]
        y = i // size[0]
        pixels[x, y] = hex_to_rgb(hex_color)

    return img



hex_colors = find_hex_colors(""" #FFFFFFF """)


# Create the image
image = create_image(hex_colors)

# Save or show the image
image.show()  # To display the image
image.save("hex_colors_image.png")



