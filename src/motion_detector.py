import cv2

class MotionDetector:
    def __init__(self):
        self.backSub = cv2.createBackgroundSubtractorMOG2()
        self.min_contour_area = 8000

    def detect_motion(self, frame):
        fg_mask = self.backSub.apply(frame)
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > self.min_contour_area]
        return large_contours, fg_mask

    def draw_contours(self, frame, contours):
        frame_out = frame.copy()
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            frame_out = cv2.rectangle(frame_out, (x, y), (x + w, y + h), (0, 0, 200), 3)
        return frame_out