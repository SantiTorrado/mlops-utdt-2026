import tempfile
import gradio as gr
from gtts import gTTS

def text_to_speech(inputs):
	text = inputs
	speech = gTTS(text)
	speech.save("prueba.mp3")
	return "prueba.mp3", text


outputs = [gr.Audio(label="Output"), "text"]

demo = gr.Interface(fn=text_to_speech, 
             inputs="text",
             outputs=outputs,
             )
             
demo.launch()
