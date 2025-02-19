import whisper

def transcribe_audio(audio_path):
    """Transcribe the given audio file using Whisper"""
    try:
        print("Loading Whisper model... ⏳")
        model = whisper.load_model("base")

        print(f"Transcribing '{audio_path}'... 📝")
        result = model.transcribe(audio_path)

        transcription = result["text"]
        print("\n✅ Transcription Complete!\n")
        print(transcription)

        # Save the transcription to a file
        save_path = "transcription.txt"
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(transcription)

        print(f"\n📄 Transcription saved as '{save_path}'")
        return transcription  # ✅ FIXED: Now it returns the text instead of just printing it

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return f"❌ Error occurred: {e}"  # Return error message to display in Streamlit

if __name__ == "__main__":
    audio_path = input("Enter the path of the audio file: ").strip()
    
    if not audio_path:
        print("❌ Please provide a valid audio file path.")
    else:
        transcribe_audio(audio_path)
