import cv2
url = "http://raspi43.local:8080/?action=stream"

video = cv2.VideoCapture(url)
backSub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = video.read()
    if ret:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        fg_mask = backSub.apply(frame)

        contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        retval, mask_thresh = cv2.threshold(fg_mask, 180, 255, cv2.THRESH_BINARY)

        # set the kernal
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        # Apply erosion
        mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)

        min_contour_area = 8000  # Define your minimum area threshold
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

        frame_out = frame.copy()
        for cnt in large_contours:
            x, y, w, h = cv2.boundingRect(cnt)
            frame_out = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 200), 3)
         
        # Display the resulting frame
        # cv2.imshow('Frame_final', frame_out)

        # frame_ct = cv2.drawContours(frame, large_contours, -1, (0, 255, 0), 2)

        # edges = cv2.Canny(frame, 100, 200)
        cv2.namedWindow("Test", cv2.WINDOW_NORMAL)
        cv2.imshow("Test", frame_out)

        key = cv2.waitKey(1)

        if key == 27:
            break
