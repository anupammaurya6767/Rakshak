# 🏡 Rakshak Security Project

Rakshak is an open-source security system that captures images and videos when motion is detected and sends them to your Telegram bot for notification. This README will guide you through the setup process.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Introduction

🏡 Rakshak is your home's security guard! It captures images and videos when motion is detected and sends them to your Telegram bot for instant notification. Whether you're at home or away, Rakshak keeps you informed about any unusual activity.

## Features

🌟 **Key Features:**

- 📸 Motion Detection: Detects motion using a webcam.
- 📬 Telegram Alerts: Sends captured images to your Telegram bot.
- 📅 Timestamps: Includes timestamps in notifications.
- 🗄️ Database Storage: Stores motion events in MongoDB.

## Getting Started

### Prerequisites

Before setting up Rakshak, make sure you have the following prerequisites:

- 💻 Hardware (e.g., Jetson, Intel NUC)
- 📷 Webcam
- 📞 Telegram bot token
- 📦 Python 3.6+

### Installation

1. Clone the Rakshak repository to your hardware:

   ```shell
   git clone https://github.com/anupammaurya6767/Rakshak.git
   ```

2. Install the project's dependencies using `pip`:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

### Configuration

1. Edit `config.json` file in the `config` directory and add your Telegram bot token:

   ```json
   {
       "telegram_token": "YOUR_TELEGRAM_BOT_TOKEN"
   }
   ```

2. Adjust other configuration settings in the `config.json` file as needed.

### Running the Project

1. Start Rakshak by running the following command:

   ```shell
   python main.py
   ```

2. Rakshak will continuously monitor your home for motion and send Telegram notifications when motion is detected.

## Contributing

We welcome contributions from the community! Whether it's fixing bugs, adding new features, or improving documentation, your contributions are valuable. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
