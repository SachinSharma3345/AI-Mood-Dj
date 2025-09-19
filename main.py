from emotion_detector import detect_emotion
from playlist_generator import create_playlist

if __name__ == "__main__":
    print("📸 Detecting emotion...")
    emotion = detect_emotion()
    print(f"😄 Detected Emotion: {emotion}")
    print("🎶 Creating your personalized playlist...")
    create_playlist(emotion)