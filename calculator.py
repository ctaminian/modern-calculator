from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

def main():

    app = QApplication([])

    # Create main window
    window = QWidget()
    window.setWindowTitle("Calculator")
    window.resize(300, 500)

    # Apply gradient background to the entire app
    window.setStyleSheet("""
        QWidget {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                        stop:0 #FDFC47, stop:1 #24FE41);
        }
    """)

    # Center the window
    screen = app.primaryScreen().geometry()
    x = (screen.width() - window.width()) // 2
    y = (screen.height() - window.height()) // 2
    window.move(x, y)

    # Create display (Ensuring it stays at the very top)
    display = QLineEdit()
    display.setAlignment(Qt.AlignmentFlag.AlignRight)
    display.setReadOnly(True)
    display.setFixedHeight(100)
    display.setStyleSheet("""
        QLineEdit {
            font-size: 50px;
            border: none;
            background: transparent;
            padding: 20px;
            color: black;
        }
    """)

    display.setText("0")

    # Function to create custom buttons with gradients
    def create_button(text, font_size, width, height, func_name, display):
        btn = QPushButton(text)
        btn.setFixedSize(width, height)
        
        if func_name in button_functions_dict:
             btn.clicked.connect(lambda _, d=display: button_functions_dict[func_name](d))

        btn.setStyleSheet(f"""
            QPushButton {{
                font-size: {font_size}px;
                background: rgba(255, 255, 255, 0.9);
                border: 1px solid rgba(0, 0, 0, 0.1);
                color: black;
            }}
            QPushButton:hover {{
                background: rgba(255, 255, 255, 0.2);
            }}
        """)
        return btn

    # Create grid layout for buttons
    grid_layout = QGridLayout()
    grid_layout.setContentsMargins(0, 0, 0, 0)
    grid_layout.setSpacing(0)
    grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    # Create buttons with different colors and sizes
    buttons = [
        [("C", 20, 75, 80, "press_c"), ("⌫", 15, 75, 80, "press_del"), ("÷", 25, 75, 80, "press_divide"), ("x", 20, 75, 80, "press_multiply")],
        [("7", 20, 75, 80, "press_7"), ("8", 20, 75, 80, "press_8"), ("9", 20, 75, 80, "press_9"), ("-", 20, 75, 80, "press_minus")],
        [("4", 20, 75, 80, "press_4"), ("5", 20, 75, 80, "press_5"), ("6", 20, 75, 80, "press_6"), ("+", 20, 75, 80, "press_plus")],
        [("1", 20, 75, 80, "press_1"), ("2", 20, 75, 80, "press_2"), ("3", 20, 75, 80, "press_3"), ("=", 20, 75, 160, "press_equals")],
        [("0", 20, 150, 80, "press_0"), (".", 20, 75, 80, "press_dot")]
    ]

    # Add buttons to grid layout
    for row_idx, row in enumerate(buttons):
        col_idx = 0
        for text, font_size, width, height, func_name in row:
            btn = create_button(text, font_size, width, height, func_name, display)

            # Special case: If button is "0", make it span 2 columns
            if text == "0":
                grid_layout.addWidget(btn, row_idx, col_idx, 1, 2)
                col_idx += 2

            # Special case: If button is "=", make it span 2 rows
            elif text == "=":
                grid_layout.addWidget(btn, row_idx, col_idx, 2, 1)

            else:
                grid_layout.addWidget(btn, row_idx, col_idx)
                col_idx += 1

    # Main vertical layout
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    layout.addWidget(display)
    layout.addLayout(grid_layout)

    window.setLayout(layout)

    window.show()
    app.exec()

# Button functions
def press_c(display):
    display.setText("0")

def press_del(display):
    if display.text()[:-1] == "":
        display.setText("0")
    else:
        display.setText(display.text()[:-1])

def press_dot(display):
    text = display.text()
    if "." in text.split()[-1]:
        return
    display.setText(text + ".")

def press_divide(display):
    display.setText(display.text() + "÷")

def press_multiply(display):
    display.setText(display.text() + "x")

def press_minus(display):
    display.setText(display.text() + "-")

def press_plus(display):
    display.setText(display.text() + "+")

def press_1(display):
    if display.text() == "0":
        display.setText("1")
    else:    
        display.setText(display.text() + "1")

def press_2(display):
    if display.text() == "0":
        display.setText("2")
    else:    
        display.setText(display.text() + "2")

def press_3(display):
    if display.text() == "0":
        display.setText("3")
    else:    
        display.setText(display.text() + "3")

def press_4(display):
    if display.text() == "0":
        display.setText("4")
    else:    
        display.setText(display.text() + "4")

def press_5(display):
    if display.text() == "0":
        display.setText("5")
    else:    
        display.setText(display.text() + "5")

def press_6(display):
    if display.text() == "0":
        display.setText("6")
    else:    
        display.setText(display.text() + "6")

def press_7(display):
    if display.text() == "0":
        display.setText("7")
    else:    
        display.setText(display.text() + "7")

def press_8(display):
    if display.text() == "0":
        display.setText("8")
    else:    
        display.setText(display.text() + "8")

def press_9(display):
    if display.text() == "0":
        display.setText("9")
    else:    
        display.setText(display.text() + "9")

def press_0(display):
    if display.text() == "0":
        display.setText("0")
    else:    
        display.setText(display.text() + "0")

def press_equals(display):
    pass

button_functions_dict = {
    "press_c": press_c,
    "press_del": press_del,
    "press_divide": press_divide,
    "press_multiply": press_multiply,
    "press_minus": press_minus,
    "press_plus": press_plus,
    "press_equals": press_equals,
    "press_dot": press_dot,
    "press_1": press_1,
    "press_2": press_2,
    "press_3": press_3,
    "press_4": press_4,
    "press_5": press_5,
    "press_6": press_6,
    "press_7": press_7,
    "press_8": press_8,
    "press_9": press_9,
    "press_0": press_0,
}

if __name__ == "__main__":
    main()