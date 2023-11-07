from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import os
import sys
from MongoDBManager import MongoDBManager

# Create the start message
start_message = """
🌟 Welcome to the Security Bot! 🌟

I'm your friendly bot designed to help you monitor your security with advanced features. My developer, Tanjiro, has worked hard to make me the best security companion.

You can control me by using various commands. Here are some things you can do:

🔹 /start - Show this welcome message.
🔹 /help - Get help and instructions.

Ready to get started? Feel free to explore and protect your surroundings! 👍
"""

# Create inline buttons
repo_button = InlineKeyboardButton("👉 Repository", url="https://github.com/your-repo")
developer_button = InlineKeyboardButton("👨‍💻 Developer's GitHub", url="https://github.com/tanjiro")
support_button = InlineKeyboardButton("💰 Support", url="https://www.paypal.com")

# Create an inline keyboard
inline_keyboard = InlineKeyboardMarkup(
    [[repo_button, developer_button], [support_button]]
)

# Read the configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]
bot_token = config["telegram"]["bot_token"]

app = Client("motion_detector_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command(["start", "help"]))
def start(_client, message):
    message.reply_text(
        text=start_message,
        reply_markup=inline_keyboard,
    )

@app.on_message(filters.command(["restart"]))
def restart(_client, message):
    message.reply_text("Restarting the application...")
    restart_application()

@app.on_message(filters.command(["getlogs"]))
def get_logs_command(_client, message):
    get_logs(chat_id)


def send_notification(chat_id, message, image_path=None):
    if image_path:
        msg = app.send_photo(chat_id, photo=image_path, caption=message)
        if msg.photo:
            image_link = msg.photo[-1].file_id
            # Save to MongoDB
            mongo_manager = MongoDBManager()
            mongo_manager.store_link_in_mongodb(message, image_link)
            mongo_manager.close_connection()
    else:
        app.send_message(chat_id, message)

def run_telegram_bot():
    app.run()

def get_logs(chat_id):
    log_dir = config["logging"]["log_dir"]
    logs = os.listdir(log_dir)
    if logs:
        for log in logs:
            app.send_document(chat_id, document=f"{log_dir}/{log}")
    else:
        app.send_message(chat_id, "No log files available.")

def restart_application():
    python = sys.executable
    os.execl(python, python, *sys.argv)
