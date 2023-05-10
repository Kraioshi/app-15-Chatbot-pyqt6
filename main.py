import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication, QStatusBar
from backend import Chatbot
import threading
import pyperclip


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(500, 475)
        self.setWindowTitle("ChatGPT OpenAI Chatbot")

        # Add chat area widget

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 370)
        self.chat_area.setReadOnly(True)

        # Add input field widget

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 390, 480, 28)
        self.input_field.returnPressed.connect(self.respond)

        # Add the button

        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(10, 430, 60, 30)
        self.send_button.clicked.connect(self.respond)

        # Add clear button

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(80, 430, 60, 30)
        self.clear_button.clicked.connect(self.clear)

        # Add copy button

        self.copy_button = QPushButton("Copy", self)
        self.copy_button.setGeometry(150, 430, 60, 30)
        self.copy_button.clicked.connect(self.copy)



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

    def clear(self):
        self.chat_area.clear()

    def copy(self):
        txt = self.chat_area.toPlainText()
        pyperclip.copy(txt)


app = QApplication(sys.argv)
project = ChatbotWindow()
sys.exit(app.exec())