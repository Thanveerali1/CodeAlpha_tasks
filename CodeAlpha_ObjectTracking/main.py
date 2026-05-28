from ultralytics import YOLO
from sort import *
import cv2
import numpy as np
import cvzone

# LOAD YOLO MODEL

model = YOLO("yolov8n.pt")

# START WEBCAM

cap = cv2.VideoCapture("videos/test.mp4")

# TRACKER

tracker = Sort(
    max_age=20,
    min_hits=3,
    iou_threshold=0.3
)

while True:

    success, frame = cap.read()

    if not success:
        break

    # YOLO DETECTION

    results = model(frame, stream=True)

    detections = np.empty((0, 5))

    for r in results:

        boxes = r.boxes

        for box in boxes:

            # BOUNDING BOX

            x1, y1, x2, y2 = box.xyxy[0]

            x1, y1, x2, y2 = (
                int(x1),
                int(y1),
                int(x2),
                int(y2)
            )

            # CONFIDENCE

            conf = round(
                float(box.conf[0]),
                2
            )

            # CLASS NAME

            cls = int(box.cls[0])

            currentClass = model.names[cls]

            # FILTER LOW CONFIDENCE

            if conf > 0.5:

                currentArray = np.array(
                    [x1, y1, x2, y2, conf]
                )

                detections = np.vstack(
                    (detections, currentArray)
                )

    # TRACK OBJECTS

    resultsTracker = tracker.update(detections)

    for result in resultsTracker:

        x1, y1, x2, y2, Id = result

        x1, y1, x2, y2, Id = (
            int(x1),
            int(y1),
            int(x2),
            int(y2),
            int(Id)
        )

        w, h = x2 - x1, y2 - y1

        # DRAW BOX

        cvzone.cornerRect(
            frame,
            (x1, y1, w, h),
            l=9
        )

        # SHOW ID

        cvzone.putTextRect(
            frame,
            f'ID: {Id}',
            (max(0, x1), max(35, y1)),
            scale=1,
            thickness=2
        )

    # SHOW OUTPUT

    cv2.imshow(
        "CodeAlpha Object Detection & Tracking",
        frame
    )

    # EXIT

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()