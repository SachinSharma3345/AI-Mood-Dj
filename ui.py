
import gradio as gr
from emotion_detector import detect_emotion
from playlist_generator import generate_playlist

def process_image(image):
    emotion = detect_emotion(image)
    playlist_link = generate_playlist(emotion)
    return f"🎭 Detected Emotion: {emotion.capitalize()}", f"🎵 [Click to Open Playlist]({playlist_link})"

iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(source="webcam", tool="editor", label="📷 Take a selfie"),
    outputs=["text", "markdown"],
    title="🎶 AI Mood DJ",
    description="Take a selfie to detect your mood and get a Spotify playlist made just for you!"
)

if __name__ == "__main__":
    iface.launch()
