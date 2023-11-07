import json
import os
from TelegramBot import run_telegram_bot, get_logs
from OpenCVMotionDetector import OpenCVMotionDetector

if __name__ == "__main__":
    motion_detector = OpenCVMotionDetector()

    try:
        motion_detector.detect_motion()
    finally:
        motion_detector.cap.release()
        cv2.destroyAllWindows()

    run_telegram_bot()
