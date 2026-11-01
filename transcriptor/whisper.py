from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()


api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)



#Agregar input o upload
audio_file = Path("audio.wav")
languages = "es"
prompt="Entrevista entre un medico y su paciente"

with audio_file.open("rb") as audio:

    #Caro, pero mas preciso. Sincrono de esta forma
    transcription = client.audio.transcriptions.create(
        model="gpt-transcribe", 
        file=audio, 
        response_format="text",
        languages=[languages],
        prompt=prompt,
        chunking_strategy="auto",
    )

    #Barato - Casi seguro que alcanza
    '''
    transcription = client.audio.transcriptions.create(
        model=whisper-1", file=audio_file
    )
    '''

    print(transcription)



