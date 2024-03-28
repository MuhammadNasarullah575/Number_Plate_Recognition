import cv2
from predict_modified import DetectionPredictor  # Import the DetectionPredictor class from predict_modified.py

# Initialize the YOLO-based detector
detector = DetectionPredictor()

# OpenCV VideoCapture
cap = cv2.VideoCapture('test_vid.mp4')  # Change the video source if using a webcam or a different video file

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the current frame
    detector.predict(frame)

    # Display the annotated frame
    cv2.imshow("License Plate Recognition", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
