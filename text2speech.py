# File: text_to_speech.py

import pyttsx3

def text_to_speech(text: str, voice_id: int = 0, rate: int = 200) -> None:
    """
    Converts text to speech.

    :param text: The text to convert to speech.
    :param voice_id: The index of the voice to use (default is 0).
    :param rate: The speech rate (default is 200 words per minute).
    """
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set the voice
        voices = engine.getProperty('voices')
        if 0 <= voice_id < len(voices):
            engine.setProperty('voice', voices[voice_id].id)
        else:
            print(f"Invalid voice_id {voice_id}. Using default voice.")

        # Set the rate of speech
        engine.setProperty('rate', rate)

        # Speak the text
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Text-to-Speech program!")
    user_text = input("Enter the text you want to convert to speech: ")

    print("\nAvailable Voices:")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")

    try:
        selected_voice = int(input("\nSelect the voice ID (default is 0): ") or 0)
    except ValueError:
        selected_voice = 0

    try:
        speech_rate = int(input("Enter the speech rate (default is 200): ") or 200)
    except ValueError:
        speech_rate = 200

    text_to_speech(user_text, voice_id=selected_voice, rate=speech_rate)
