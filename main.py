import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)
        self.setWindowTitle("ChatGPT OpenAI Chatbot")

        # Add chat area widget

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field widget

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add the button

        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 50, 40)
        self.button.clicked.connect(self.respond)

        # Add clear button
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(10, 400, 40, 30)
        self.clear_button.clicked.connect(self.clear)

        self.show()

    def respond(self):
        user_text = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_text}</p>")
        self.input_field.clear()
        re = self.chatbot.get_response(user_text)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {re}</p>")

    def clear(self):
        self.chat_area.clear()




app = QApplication(sys.argv)
project = ChatbotWindow()
# project.show()
sys.exit(app.exec())