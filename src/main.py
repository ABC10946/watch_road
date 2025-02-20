import cv2
import time
import argparse
from motion_detector import MotionDetector
from prometheus_metrics import PrometheusMetrics

def main():
    parser = argparse.ArgumentParser(description="Motion detection script")
    parser.add_argument("--nogui", action="store_true", help="Run without GUI")
    args = parser.parse_args()

    url = "http://raspi43.local:8080/?action=stream"
    video = cv2.VideoCapture(url)

    motion_detector = MotionDetector()
    prometheus_metrics = PrometheusMetrics(redisEnabled=False)

    while True:
        ret, frame = video.read()

        if not ret:
            print("Failed to read frame")
            break

        try:
            if ret:
                frame = cv2.rotate(frame, cv2.ROTATE_180)
                large_contours, _ = motion_detector.detect_motion(frame)

                if len(large_contours) > 0:
                    prometheus_metrics.increment_motion_count()
                    print(time.time(), "Motion detected")
                
                frame = motion_detector.draw_contours(frame, large_contours)

                if not args.nogui:
                    cv2.namedWindow("Motion Detection", cv2.WINDOW_NORMAL)
                    cv2.imshow("Motion Detection", frame)

                key = cv2.waitKey(1)
                if key == 27:
                    break

        except Exception as e:
            print(e)
            break

    video.release()
    if not args.nogui:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()