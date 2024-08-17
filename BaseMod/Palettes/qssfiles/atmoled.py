atmoled_qss = """	        
            QScrollArea {
                border: none;
            }
            QScrollArea, QWidget, QAbstractScrollArea, QWidget {
                background-color: #000000;
            }
            QScrollArea, QWidget, QAbstractScrollArea, QViewport {
                background-color: #000000;
            }
	    
	    QTextEdit, QListView,QScrollArea {
		background-color: #000000;
	    }
           QToolTip {
               background-color: #000000;
               color: #1f1f1f;
               border: 1px solid #1f1f1f;
           }
           QMainWindow {
               background-color: #000000;
           }

           QMainWindow::separator {
               background-color: #1f1f1f;
           }

           QToolBar {
               background-color: #000000;
               border: 1px solid #1f1f1f;
           }

           QStatusBar {
               background-color: #000000;
               color: #1f1f1f;
               border-top: 1px solid #1f1f1f;
           }
           QFrame {
               background-color: #000000;
               border: 0px solid #1f1f1f;
           }

           QGroupBox {
               background-color: #000000;
               border: 1px solid #1f1f1f;
               color: #1f1f1f;
           }

           QPushButton {
               background-color: #000000;
               color: #1f1f1f;
               border: 1px solid #1f1f1f;
           }

           QPushButton:hover {
               background-color: #333333;
           }

           QPushButton:pressed {
               background-color: #333333;
               border-color: #333333;
           }

           QCheckBox {
               color: #1f1f1f;
           }

           QCheckBox::indicator {
               border: 1px solid #1f1f1f;
               width: 16px;
               height: 16px;
           }

           QCheckBox::indicator:checked {
               background-color: #333333;
               border: 1px solid #333333;
           }
           QScrollBar:vertical {
               background: #000000;
               width: 15px;
               margin: 0px 0px 0px 0px;
           }

           QScrollBar::handle:vertical {
               background: #333333;
               min-height: 20px;
               border-radius: 0px;
           }

           QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
               background: #000000;
               height: 0px;
           }

           QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
               background: none;
           }

           QPushButton {
               background-color: #000000;
               color: #1f1f1f;
               border: 1px solid #1f1f1f;
               padding: 5px;
           }

           QPushButton:hover {
               background-color: #333333;
           }

           QPushButton:pressed {
               background-color: #333333;
               border-color: #333333;
           }

           QMainWindow {
               background-color: #000000;
           }
           QCalendar {
               background-color: #000000;
           }
           QTextEdit {
               border-width: 1px;
               border-style: solid;
               border-color: #1f1f1f;
               background-color: #000000;
               color: #1f1f1f;
           }
           QPlainTextEdit {
               border-width: 1px;
               border-style: solid;
               border-color: #1f1f1f;
               background-color: #000000;
               color: #1f1f1f;
           }
           QToolButton {
               border-style: solid;
               border-color: #1f1f1f;
               border-width: 1px;
               border-radius: 5px;
               color: #1f1f1f;
               padding: 2px;
               background-color: #000000;
           }
           QToolButton:hover {
               border-color: #1f1f1f;
               color: #1f1f1f;
               background-color: #333333;
           }
           QToolButton:pressed {
               border-color: #333333;
               color: #1f1f1f;
               background-color: #333333;
           }
           QLineEdit {
               border-width: 1px;
               border-style: solid;
               border-color: #1f1f1f;
               background-color: #000000;
               color: #1f1f1f;
           }
           QLabel {
               color: #1f1f1f;
           }
           QLCDNumber {
               color: #1f1f1f;
           }
           QProgressBar {
               text-align: center;
               color: #1f1f1f;
               border-radius: 10px;
               border-color: transparent;
               border-style: solid;
               background-color: #333333;
           }
           
           QProgressBar::chunk {
               background-color: #1f1f1f;
               border-radius: 10px;
           }
           QMenuBar {
               background-color: #000000;
           }
           QMenuBar::item {
               color: #1f1f1f;
               spacing: 3px;
               padding: 1px 4px;
               background-color: #000000;
           }
           QListWidget {
               background-color: #000000;
               color: #1f1f1f;
               alternate-background-color: #333333;
           }

           QMenuBar::item:selected {
               background-color: #333333;
               color: #1f1f1f;
           }
           QMenu {
               background-color: #000000;
           }
           QMenu::item:selected {
               background-color: #333333;
               color: #1f1f1f;
           }
           QMenu::item {
               color: #1f1f1f;
               background-color: #000000;
           }
           QTabWidget {
               color: #1f1f1f;
               background-color: #000000;
           }
           QTabWidget::pane {
               border-color: #1f1f1f;
               background-color: #000000;
               border-style: solid;
               border-width: 1px;
               border-bottom-left-radius: 4px;
               border-bottom-right-radius: 4px;
               padding: 2px;
           }
           QTabBar::tab:selected {
               border-color: #1f1f1f;
               border-bottom-color: #000000;
            }
           QTabBar::tab {
               border-style: solid;
               border-width: 1px;
               border-top-color: #1f1f1f;
               border-left-color: #1f1f1f;
               border-bottom-color: #1f1f1f;
               color: #1f1f1f;
               padding: 3px;
               background-color: #000000;
           }
           QTabBar::tab:selected, QTabBar::tab:hover {
               border-top-color: #1f1f1f;
               border-left-color: #1f1f1f;
               border-bottom-color: #1f1f1f;
               color: #1f1f1f;
               background-color: #333333;
           }
           QCheckBox {
               color: #1f1f1f;
               padding: 2px;
           }
           QCheckBox:disabled {
               color: #333333;
               padding: 2px;
           }
           QCheckBox::indicator:checked {
               height: 10px;
               width: 10px;
               border-style: solid;
               border-width: 1px;
               border-color: #1f1f1f;
               background-color: #333333;
           }
           QCheckBox::indicator:unchecked {
               height: 10px;
               width: 10px;
               border-style: solid;
               border-width: 1px;
               border-color: #1f1f1f;
               background-color: transparent;
           }
           QRadioButton {
               color: #1f1f1f;
               padding: 1px;
           }
           QRadioButton::indicator:checked {
               height: 10px;
               width: 10px;
               border-style: solid;
               border-radius: 5px;
               border-width: 1px;
               border-color: #1f1f1f;
               background-color: #333333;
           }
           QRadioButton::indicator:!checked {
               height: 10px;
               width: 10px;
               border-style: solid;
               border-radius: 5px;
               border-width: 1px;
               border-color: #1f1f1f;
               background-color: transparent;
           }
           QStatusBar {
               color: #1f1f1f;
           }
           QSpinBox, QDoubleSpinBox, QTimeEdit, QDateTimeEdit, QDateEdit{
               color: #1f1f1f;
               background-color: #000000;
               border-width: 1px;
               border-style: solid;
               border-color: #1f1f1f;
           }
           
           QDial {
               background: #000000;
           }
           QToolBox {
               color: #1f1f1f;
               background-color: #000000;
           }
           QToolBox::tab {
               color: #1f1f1f;
               background-color: #000000;
           }
           QToolBox::tab:selected {
               color: #1f1f1f;
               background-color: #000000;
           }
           QScrollArea {
               color: #1f1f1f;
               background-color: #000000;
           }
           QSlider::groove:horizontal {
               border: 1px solid #1f1f1f;
               height: 5px;
               background: #333333;
               margin: 2px 0;
           }
           QSlider::handle:horizontal {
               background: #1f1f1f;
               border: 1px solid #1f1f1f;
               width: 10px;
               margin: -5px 0;
               border-radius: 2px;
           }
           QSlider::add-page:qlineargradient {
               background: #000000;
               border-top: 1px solid #333333;
               border-bottom: 1px solid #333333;
           }
           QSlider::sub-page:qlineargradient {
               background: #1f1f1f;
               border-top: 1px solid #333333;
               border-bottom: 1px solid #333333;
           }
           QSlider::groove:vertical {
               border: 1px solid #1f1f1f;
               width: 5px;
               background: #333333;
               margin: 0 0;
           }
           QSlider::handle:vertical {
               background: #1f1f1f;
               border: 1px solid #1f1f1f;
               height: 10px;
               margin: 0 -5px;
               border-radius: 2px;
           }
           QSlider::add-page:vertical {
               background: #1f1f1f;
               border-left: 1px solid #333333;
               border-right: 1px solid #333333;
           }
           QSlider::sub-page:vertical {
               background: #000000;
               border-left: 1px solid #333333;
               border-right: 1px solid #333333;
           }
"""
