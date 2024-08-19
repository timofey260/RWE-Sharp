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
   background-color: #2A2A2A;
   color: #E0E0E0;
   border: 1px solid #444444;
}
QMainWindow {
   background-color: #2A2A2A;
}

QMainWindow::separator {
   background-color: #444444;
}

QToolBar {
   background-color: #3D3D3D;
   border: 1px solid #444444;
}

QStatusBar {
   background-color: #2A2A2A;
   color: #E0E0E0;
   border-top: 1px solid #444444;
}
QFrame {
   background-color: #2A2A2A;
   border: 0px solid #444444;
}

QGroupBox {
   background-color: #2A2A2A;
   border: 1px solid #444444;
   color: #E0E0E0;
}



QPushButton {
   background-color: #3D3D3D;
   color: #E0E0E0;
   border: 1px solid #555555;
}

QPushButton:hover {
   background-color: #505050;
}

QPushButton:pressed {
   background-color: @accent_medium;
   border-color: @accent_medium;
}

QCheckBox {
   color: #E0E0E0;
}

QCheckBox::indicator {
   border: 1px solid #555555;
   width: 16px;
   height: 16px;
}

QCheckBox::indicator:checked {
   background-color: @accent_medium;
   border: 1px solid @accent_medium;
}
QScrollBar:vertical {
   background: #2A2A2A;
   width: 15px;
   margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
   background: #3D3D3D;
   min-height: 20px;
   border-radius: 0px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
   background: #2A2A2A;
   height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
   background: none;
}

QPushButton {
   background-color: #3D3D3D;
   color: #E0E0E0;
   border: 1px solid #555555;
   padding: 5px;
}

QPushButton:hover {
   background-color: #505050;
}

QPushButton:pressed {
   background-color: @accent_medium;
   border-color: @accent_medium;
}

QMainWindow {
   background-color: #151a1e;
}
QCalendar {
   background-color: #151a1e;
}
QTextEdit {
   border-width: 1px;
   border-style: solid;
   border-color: @accent_medium;
   background-color: #222b2e;
   color: #d3dae3;
}
QPlainTextEdit {
   border-width: 1px;
   border-style: solid;
   border-color: @accent_medium;
   background-color: #222b2e;
   color: #d3dae3;
}
QToolButton {
   border-style: solid;
   border-color: #444444;
   border-width: 1px;
   border-radius: 5px;
   color: #d3dae3;
   padding: 2px;
   background-color: #3D3D3D;
}
QToolButton:hover {
   border-color: #444444;
   color: #d3dae3;
   background-color: #505050;
}
QToolButton:pressed {
   border-color: @accent_medium;
   color: #d3dae3;
   background-color: @accent_medium;
}
QLineEdit {
   border-width: 1px;
   border-style: solid;
   border-color: @accent_medium;
   background-color: #222b2e;
   color: #d3dae3;
}
QLabel {
   color: #d3dae3;
}
QLCDNumber {
   color: #4d9b87;
}
QProgressBar {
   text-align: center;
   color: #d3dae3;
   border-radius: 10px;
   border-color: transparent;
   border-style: solid;
   background-color: #52595d;
}
QProgressBar::chunk {
   background-color: #214037;
   border-radius: 10px;
}
QMenuBar {
   background-color: #151a1e;
}
QMenuBar::item {
   color: #d3dae3;
   spacing: 3px;
   padding: 1px 4px;
   background-color: #151a1e;
}

QMenuBar::item:selected {
   background-color: #252a2e;
   color: #FFFFFF;
}
QMenu {
   background-color: #151a1e;
}
QMenu::item:selected {
   background-color: #252a2e;
   color: #FFFFFF;
}
QMenu::item {
   color: #d3dae3;
   background-color: #151a1e;
}
QTabWidget {
   color: #d3dae3;
   background-color: #151a1e;
}
QTabWidget::pane {
   border-color: #050a0e;
   background-color: #1e282c;
   border-style: solid;
   border-width: 1px;
   border-bottom-left-radius: 4px;
   border-bottom-right-radius: 4px;
   padding: 2px;
}
QTabBar::tab:selected {
   border-color: #9B9B9B;
   border-bottom-color: #C2C7CB; /* same as pane color */
}
QTabBar::tab {
   border-style: solid;
   border-width: 1px;
   border-top-color: #050a0e;
   border-left-color: #050a0e;
   border-bottom-color: #050a0e;
   color: #d3dae3;
   padding: 3px;
   background-color: #151a1e;
}
QTabBar::tab:selected, QTabBar::tab:hover {
   border-top-color: #050a0e;
   border-left-color: #050a0e;
   border-bottom-color: #050a0e;
   color: #FFFFFF;
   background-color: #1e282c;
}
QCheckBox {
   color: #d3dae3;
   padding: 2px;
}
QCheckBox:disabled {
   color: #808086;
   padding: 2px;
}
QCheckBox::indicator:checked {
   height: 10px;
   width: 10px;
   border-style: solid;
   border-width: 1px;
   border-color: @accent_medium;
   background-color: #1e282c;
}
QCheckBox::indicator:unchecked {
   height: 10px;
   width: 10px;
   border-style: solid;
   border-width: 1px;
   border-color: @accent_medium;
   background-color: transparent;
}
QRadioButton {
   color: #d3dae3;
   padding: 1px;
}
QRadioButton::indicator:checked {
   height: 10px;
   width: 10px;
   border-style: solid;
   border-radius: 5px;
   border-width: 1px;
   border-color: @accent_medium;
   background-color: #1e282c;
}
QRadioButton::indicator:!checked {
   height: 10px;
   width: 10px;
   border-style: solid;
   border-radius: 5px;
   border-width: 1px;
   border-color: @accent_medium;
   background-color: transparent;
}
QStatusBar {
   color: #027f7f;
}
QSpinBox, QDoubleSpinBox, QTimeEdit, QDateTimeEdit, QDateEdit{
   color: #d3dae3;
   background-color: #222b2e;
   border-width: 1px;
   border-style: solid;
   border-color: @accent_medium;
}


QDial {
   background: #16a085;
}
QToolBox {
   color: #a9b7c6;
   background-color: #222b2e;
}
QToolBox::tab {
   color: #a9b7c6;
   background-color: #222b2e;
}
QToolBox::tab:selected {
   color: #FFFFFF;
   background-color: #222b2e;
}
QScrollArea {
   color: #555555;
   background-color: #222b2e;
}
QSlider::groove:horizontal {
   border: 1px solid @accent_medium;
   height: 5px;
   background: #3d4d53;
   margin: 2px 0;
}
QSlider::handle:horizontal {
   background: @accent_medium;
   border: 1px solid @accent_medium;
   width: 10px;
   margin: -5px 0;
   border-radius: 2px;
}
QSlider::add-page:qlineargradient {
   background: #2f3a3f;
   border-top: 1px solid #3d4d53;
   border-bottom: 1px solid #3d4d53;
}
QSlider::sub-page:qlineargradient {
   background: #16a085;
   border-top: 1px solid #3d4d53;
   border-bottom: 1px solid #3d4d53;
}
QSlider::groove:vertical {
   border: 1px solid @accent_medium;
   width: 5px;
   background: #3d4d53;
   margin: 0 0;
}
QSlider::handle:vertical {
   background: @accent_medium;
   border: 1px solid @accent_medium;
   height: 10px;
   margin: 0 -5px;
   border-radius: 2px;
}
QSlider::add-page:vertical {
   background: #16a085;
   border-left: 1px solid #3d4d53;
   border-right: 1px solid #3d4d53;
}
QSlider::sub-page:vertical {
   background: #2f3a3f;
   border-left: 1px solid #3d4d53;
   border-right: 1px solid #3d4d53;
}
QScrollBar:horizontal {
   background: #2A2A2A;
   height: 15px;
   margin: 0px 0px 0px 0px;
}
QScrollBar::handle:horizontal {
   background: #3D3D3D;
   min-width: 20px;
   border-radius: 0px;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
   background: #2A2A2A;
   width: 0px;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
   background: none;
}
QTreeView, QListView {
   border-width: 1px;
   border-style: solid;
   border-color: @accent_medium;
   background-color: #222b2e;
   alternate-background-color: #151a1e;
   color: #d3dae3;
}
QTableView, QTableWidget, QTreeWidget {
   gridline-color: #151a1e;
   border-width: 1px;
   border-style: solid;
   border-color: @accent_medium;
   background-color: #222b2e;
   color: #d3dae3;
}
QTableView::item:selected, QTreeView::item:selected, QListView::item:selected, QTableWidget::item:selected, QTreeWidget::item:selected {
   background-color: #214037;
}
QHeaderView::section {
   background-color: #151a1e;
   color: #d3dae3;
   padding: 5px;
   border-style: solid;
   border-color: #151a1e;
   border-width: 0px 0px 1px 1px;
}
QHeaderView::section:selected, QHeaderView::section::checked {
   background-color: #222b2e;
}
QSplitter::handle {
   background-color: #222b2e;
}
QTreeView::branch:selected {
   background-color: #214037;
}
QTreeView::branch:hover {
   background-color: #214037;
}
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
   border-image: url(noline.png) 0;
}
QTreeView::branch:has-children:!has-siblings:closed, QTreeView::branch:closed:has-children:has-siblings {
   border-image: none;
   image: url(branch-closed.png);
}
QTreeView::branch:open:has-children:!has-siblings, QTreeView::branch:open:has-children:has-siblings {
   border-image: none;
   image: url(branch-open.png);
}
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
   border-image: url(noline.png) 0;
}
QDockWidget {
   titlebar-close-icon: url(close.png);
   titlebar-normal-icon: url(undock.png);
}
QTreeWidget::branch:closed:has-children:has-siblings {
   border-image: none;
   image: url(branch-closed.png);
}
QTreeWidget::branch:closed:has-children:!has-siblings {
   border-image: none;
   image: url(branch-closed.png);
}
QTreeWidget::branch:open:has-children:has-siblings {
   border-image: none;
   image: url(branch-open.png);
}
QTreeWidget::branch:open:has-children:!has-siblings {
   border-image: none;
   image: url(branch-open.png);
}




QGroupBox::title {
   color: #4fa0F8b;
   subcontrol-origin: margin;
   subcontrol-position: top left;
   padding: 0 3px;
}
          QWidget {
    color: #a9b7c6;
    background-color: #222b2e;
    selection-background-color: @accent_medium;
}
QScrollArea {
    border: none;
}
QScrollArea > QWidget > QAbstractScrollArea > QWidget {
    background-color: #222b2e;
}
QScrollArea > QWidget > QAbstractScrollArea > QViewport {
    background-color: #222b2e;
}
"""

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



