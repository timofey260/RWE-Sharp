circular_qss = """
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
            titlebar-close-icon: url(close.svg);
            titlebar-normal-icon: url(undock.svg);
            titlebar-height: 22px;
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
        QScrollArea > QWidget > QAbstractScrollArea > QWidget, 
        QScrollArea > QWidget > QAbstractScrollArea > QViewport {
            background-color: #252525;
        }
    """
