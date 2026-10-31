import tempfile
import gradio as gr
import pytesseract
from gtts import gTTS

def image_to_speech(inputs):
    text = pytesseract.image_to_string(inputs)
    speech = gTTS(text)
    speech.save("prueba.mp3")
    return "prueba.mp3", text

inputs = gr.Image(type="pil")
outputs = [gr.Audio(label="Output"), gr.Textbox(label="Extracted Text")]

demo = gr.Interface(fn=image_to_speech, 
             inputs=inputs,
             outputs=outputs,
             )
             
demo.launch()
