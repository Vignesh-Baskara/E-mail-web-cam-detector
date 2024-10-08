import os
import cv2
import time
from mailing import send_email
import glob
from threading import Thread

video = cv2.VideoCapture(0)
time.sleep(1)

window_name = "My video"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)  # Create the window with normal size capability
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # Set to fullscreen

first_frame = None
status_list = []
count = 1

def clean_folder():
    print("Cleaning started...")
    images = glob.glob("images/*.png")
    for image in images:
        try:
            os.remove(image)
        except PermissionError as e:
            print(f"Error removing {image}: {e}")
    print("Cleaning ended.")

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5500:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]
    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        # Start the email and cleaning processes asynchronously
        email_thread = Thread(target=send_email, args=(image_with_object,))
        clean_thread = Thread(target=clean_folder)

        email_thread.start()


    cv2.imshow(window_name, frame)  # Show the color frame with contours in the fullscreen window

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
clean_thread.start()
