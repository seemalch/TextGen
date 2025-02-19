import streamlit as st
import whisper
import tempfile
import os
from myscript import transcribe_audio

# Set Full-Width Layout
st.set_page_config(
    page_title="Whisper AI Transcriber",
    page_icon="🎙",
    layout="wide"
)

# Custom Styling for Modern & Sleek UI
st.markdown(
    """
    <style>
        /* Global Background */
        .stApp {
            background-color: #f9f9f9;
            font-family: 'Arial', sans-serif;
        }

        /* Title Style */
        .title {
            color: #134587;
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Subtitle Style */
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #777;
            margin-bottom: 30px;
        }

        /* File Upload Box */
        .stFileUploader {
            border-radius: 12px;
            background-color: #ffffff;
            border: 2px solid #ddd;
            padding: 25px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }

        /* Audio Player Styling */
        .stAudio {
            margin-top: 10px;
            border-radius: 12px;
            background-color: #ffffff;
            padding: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Text Area Styling for Transcription Output */
        .stTextArea textarea {
            font-size: 18px !important;
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            border: 2px solid #ddd;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05);
            height: 250px;
        }

        /* Buttons Styling */
        .stButton>button {
            background-color: #134587 !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 18px !important;
            padding: 15px 28px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #103a65 !important;
        }

        /* Download Button */
        .stDownloadButton button {
            background-color: #134587 !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 16px !important;
            padding: 15px 24px;
        }

        /* Spacing Between Elements */
        .stBlock {
            margin-top: 40px;
        }

        /* Mobile responsiveness */
        @media (max-width: 800px) {
            .stButton>button {
                width: 100%;
                font-size: 16px !important;
                padding: 12px 24px;
            }
            .stTextArea textarea {
                height: 180px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Header
st.markdown('<p class="title">🎙 Whisper AI - Audio Transcription</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload an audio file to transcribe speech to text.</p>', unsafe_allow_html=True)

# File Upload Section
uploaded_file = st.file_uploader("📤 Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    st.audio(uploaded_file, format="audio/mp3", start_time=0)

    if st.button("🔍 Transcribe Audio"):
        with st.spinner("⏳ Transcribing... Please wait."):
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_filename = tmp_file.name

            # Transcribe
            transcription = transcribe_audio(tmp_filename)

            # Display Transcription
            st.subheader("📝 Transcription Output:")
            if transcription:
                st.text_area("Transcribed Text:", transcription, height=350, key="transcription")
            else:
                st.error("❌ No transcription available.")

            # Save transcription to a file
            txt_filename = "transcription.txt"
            with open(txt_filename, "w", encoding="utf-8") as f:
                f.write(transcription)

            # Download Button
            st.download_button(
                label="⬇️ Download Transcript",
                data=transcription,
                file_name=txt_filename,
                mime="text/plain"
            )

            # Cleanup
            os.remove(tmp_filename)