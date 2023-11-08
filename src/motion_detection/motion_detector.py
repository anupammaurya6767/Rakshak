import cv2
import os
import time
import json
import logging
from src.telegram.bot import send_notification
from src.logger import logger  # Import the logger module

# Read the configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

chat_id = config["telegram"]["chat_id"]
log_dir = config["logging"]["log_dir"]

class OpenCVMotionDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.fgbg = cv2.createBackgroundSubtractorMOG2()
        self.log_filename = f"{log_dir}/motion_detector.log"
        self.init_logging()

    def init_logging(self):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def detect_motion(self):
        while True:
            ret, frame = self.cap.read()

            # Apply background subtraction to detect motion
            fgmask = self.fgbg.apply(frame)

            # Threshold to focus on significant changes
            thresh = cv2.threshold(fgmask, 128, 255, cv2.THRESH_BINARY)[1]

            # Find contours in the thresholded image
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            motion_detected = False

            for contour in contours:
                if cv2.contourArea(contour) > 1000:  # You can adjust this threshold as needed
                    motion_detected = True
                    break

            if motion_detected:
                # Save the image with a timestamp
                timestamp = int(time.time())
                image_filename = f"{timestamp}.jpg"
                image_path = os.path.join("data/temp_images", image_filename)
                cv2.imwrite(image_path, frame)

                # Send a notification with the image
                # only for unrecognized persons (if condition to be added)
                send_notification(chat_id, "Motion detected!", image_path=image_path)

                # Delete the image from the server
                os.remove(image_path)

                # Log the motion event
                logger.info("Motion detected and recorded.")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
