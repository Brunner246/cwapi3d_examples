from PyQt5.QtWidgets import (QDialog,
                             QListWidget,
                             QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QListWidgetItem,
                             QLabel,
                             QPushButton)


class CustomListWidgetItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumHeight(15)
        self.widget = QWidget(parent)

        self.layout = QHBoxLayout()
        self.pbn1 = QPushButton("Button 1")
        self.pbn1.setStyleSheet("background-color: transparent; border: none; color: black;")
        self.pbn2 = QPushButton("Button 2")
        [button.setStyleSheet("background-color: transparent; border: none; color: black;")
         for button in [self.pbn1, self.pbn2]]
        [self.layout.addWidget(label) for label in [self.pbn1, self.pbn2]]

        self.widget.setLayout(self.layout)

        self.pbn1.clicked.connect(lambda : print("Button 1"))
        self.pbn2.clicked.connect(lambda: print("Button 2"))


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_widget = None
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 500, 300)
        self.list_widget = QListWidget(self)
        list_widget_item = QListWidgetItem(self.list_widget)
        list_widget1 = CustomListWidgetItem(self.list_widget)

        self.list_widget.insertItem(0, list_widget_item)
        self.list_widget.setItemWidget(list_widget_item, list_widget1)

        vertical_layout = QVBoxLayout(self)
        vertical_layout.addWidget(self.list_widget)

        self.setLayout(vertical_layout)


if __name__ == '__main__':
    print("test")
    dialog = Dialog()
    dialog.show()
