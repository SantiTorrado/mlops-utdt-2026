import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("Text-To-Speech App")

text = st.text_area("Ingresar el texto a reproducir", "Hello, Streamlit!")

st.sidebar.title("Audio Options")
language = st.sidebar.selectbox("Elegir lenguaje", ['en', 'es', 'fr', 'de', 'it'], index=0)

if st.button("Generar audio"):
    tts = gTTS(text, lang=language)
    st.balloons()

    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    st.audio(audio_buffer, format='audio/mp3')
