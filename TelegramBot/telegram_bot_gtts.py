from io import BytesIO
import os
import asyncio
from gtts import gTTS
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def start(update, context):
    welcome_text = 'Hola, soy mlops-mim-bot, acá va la lista de cosas que me podés pedir'
    await update.message.reply_text(welcome_text)
    await send_help_text(update, context)
start_handler = CommandHandler('start', start)

async def unknown(update, context):
    unknown_text = 'No reconozco ese comando. Esta es la lista de cosas que me podes pedir'
    await update.message.reply_text(unknown_text)
    await send_help_text(update, context)
unknown_handler = MessageHandler(filters.ALL, unknown)

async def send_help_text(update, context):
    help_text = '/speech genera un audio a partir de tu texto' + '\n'
    await update.message.reply_text(help_text)
    
async def speech(update, context):
    text = ' '.join(context.args)
    
    if not text:
        await update.message.reply_text("Please provide text after the /speech command.")
        return

    tts = gTTS(text=text, lang='en')
    audio_file = "speech.mp3"
    tts.save(audio_file)

    with open(audio_file, 'rb') as audio:
        await update.message.reply_audio(audio)
    os.remove(audio_file)
speech_handler = CommandHandler('speech', speech)

    

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(start_handler)
app.add_handler(speech_handler)
app.add_handler(unknown_handler)

app.run_polling()

