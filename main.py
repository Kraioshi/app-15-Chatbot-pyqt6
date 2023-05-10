import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(500, 500)
        self.setWindowTitle("ChatGPT OpenAI Chatbot")

        # Add chat area widget

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 370)
        self.chat_area.setReadOnly(True)

        # Add input field widget

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 390, 410, 28)

        # Add the button

        self.button = QPushButton("Send", self)
        self.button.setGeometry(430, 389, 60, 30)
        self.button.clicked.connect(self.respond)

        self.show()

    def respond(self):
        user_text = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_text}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_text, ))
        thread.start()

    def get_bot_response(self, user_text):
        re = self.chatbot.get_response(user_text)
        self.chat_area.append(f"<p style='color:#333333; background-color: #D6D6D6'>Bot: {re}</p>")


app = QApplication(sys.argv)
project = ChatbotWindow()
# project.show()
sys.exit(app.exec())