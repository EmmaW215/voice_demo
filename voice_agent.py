from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

client = ElevenLabs(
    api_key="sk_57faab0b8d2c355f462ab753f9fc2d74cbe1bf0dd4c3683b" #os.environ["ELEVENLABS_API_KEY"]
)

def listen():
   return client.speech_to_text.convert(model_id="scribe_v2",
                                        cloud_storage_url="https://audio-samples.github.io/samples/mp3/blizzard_unconditional/sample-0.mp3")

def speak(text, **kwargs):
    tts_args = {
        "voice_id": "JBFqnCBsd6RMkjVDRZzb",
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_128",
    }
    tts_args.update(**kwargs)

    audio = client.text_to_speech.convert(
        text=text,
        **tts_args
    )

    play(audio)


if __name__ == "__main__":
    audio_data = listen()
    print(audio_data)
    text = audio_data.text
    speak(text)
