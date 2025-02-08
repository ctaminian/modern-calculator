from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

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

display.setText("470.3")

# Function to create custom buttons with gradients
def create_button(text, font_size, width, height):
    btn = QPushButton(text)
    btn.setFixedSize(width, height)
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
    [("C", 20, 75, 80,), ("⌫", 15, 75, 80,), ("÷", 25, 75, 80,), ("x", 20, 75, 80,)],
    [("7", 20, 75, 80,), ("8", 20, 75, 80,), ("9", 20, 75, 80,), ("-", 20, 75, 80,)],
    [("4", 20, 75, 80,), ("5", 20, 75, 80,), ("6", 20, 75, 80,), ("+", 20, 75, 80,)],
    [("1", 20, 75, 80,), ("2", 20, 75, 80,), ("3", 20, 75, 80,), ("=", 20, 75, 160,)],
    [("0", 20, 150, 80,), (".", 20, 75, 80,)]
]

# Add buttons to grid layout
for row_idx, row in enumerate(buttons):
    col_idx = 0
    for item in row:
        text, font_size, width, height = item
        btn = create_button(text, font_size, width, height)

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
