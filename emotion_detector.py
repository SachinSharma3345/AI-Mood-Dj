# import cv2
# from fer import FER
# from moviepy.editor import VideoFileClip


# def detect_emotion():
#     detector = FER(mtcnn=True)
#     cam = cv2.VideoCapture(0)
#     emotion_detected = "neutral"

#     print("Press 'q' to capture emotion")

#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             break
#         cv2.imshow("Emotion Detection", frame)

#         key = cv2.waitKey(1)
#         if key == ord('q'):
#             results = detector.detect_emotions(frame)
#             if results:
#                 emotion_scores = results[0]["emotions"]
#                 emotion_detected = max(emotion_scores, key=emotion_scores.get)
#             break

#     cam.release()
#     cv2.destroyAllWindows()
#     return emotion_detected


import cv2
from fer import FER

def detect_emotion():
    detector = FER(mtcnn=False)  # ✅ MTCNN disabled (safer on Mac)
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Could not access the webcam.")
        return "camera_error"

    emotion_detected = "neutral"
    print("Press 'q' to capture emotion...")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to read from camera.")
            break

        cv2.imshow("Emotion Detection - Press 'q' to Capture", frame)
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            results = detector.detect_emotions(frame)
            if results:
                emotion_scores = results[0]["emotions"]
                emotion_detected = max(emotion_scores, key=emotion_scores.get)
            else:
                print("No face detected. Please try again.")
                emotion_detected = "undetected"
            break

    cam.release()
    cv2.destroyAllWindows()
    return emotion_detected


if __name__ == "__main__":
    emotion = detect_emotion()
    print(f"🎭 Detected Emotion: {emotion}")
