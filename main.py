import json
import os
from TelegramBot import run_telegram_bot, get_logs
from OpenCVMotionDetector import OpenCVMotionDetector
from internet_connection.connect import establish_internet_connection


if __name__ == "__main__":
    # Establish the internet connection
    establish_internet_connection("config/config.json")
    motion_detector = OpenCVMotionDetector()

    try:
        motion_detector.detect_motion()
    finally:
        motion_detector.cap.release()
        cv2.destroyAllWindows()

    run_telegram_bot()
