import cv2
import datetime
import os
import time

from detector import process_frame
from database import init_db, insert_event
from event_bus import publish_event

# Create folders
os.makedirs("snapshots", exist_ok=True)
os.makedirs("database", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Initialize database
init_db()

# Start camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Unable to access camera")
    exit()

ret, frame1 = cap.read()
ret, frame2 = cap.read()

if not ret:
    print("Unable to read frames")
    exit()

# Metrics
event_count = 0
last_event_time = time.time()
cooldown_seconds = 2

prev_frame_time = time.time()

while True:

    status = "Monitoring"

    contours = process_frame(frame1, frame2)

    motion_detected = False

    for contour in contours:

        if cv2.contourArea(contour) < 1500:
            continue

        motion_detected = True

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame1,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Event generation with cooldown
    if motion_detected:

        status = "Motion Detected"

        current_time = time.time()

        if current_time - last_event_time >= cooldown_seconds:

            event_count += 1

            timestamp = datetime.datetime.now()

            filename = (
                f"snapshots/"
                f"{timestamp.strftime('%Y%m%d_%H%M%S_%f')}.jpg"
            )

            cv2.imwrite(filename, frame1)

            insert_event(
                "MOTION",
                str(timestamp),
                filename
            )

            publish_event(
                f"Motion detected -> {filename}"
            )

            last_event_time = current_time

    # FPS Calculation
    current_frame_time = time.time()

    fps = 1 / (current_frame_time - prev_frame_time)

    prev_frame_time = current_frame_time

    # Dashboard
    cv2.putText(
        frame1,
        f"Events: {event_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    status_color = (0, 255, 0)

    if status == "Motion Detected":
        status_color = (0, 0, 255)

    cv2.putText(
        frame1,
        f"Status: {status}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        status_color,
        2
    )

    cv2.putText(
        frame1,
        datetime.datetime.now().strftime("%H:%M:%S"),
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame1,
        f"FPS: {int(fps)}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Vision Event Processing System",
        frame1
    )

    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()