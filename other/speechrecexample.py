import speech_recognition as sr

def transcribe_audio(file_path):
    # Create object Recognizer
    r = sr.Recognizer()

    # Open audiofile
    with sr.AudioFile(file_path) as audio_file:
        # Read audio from file
        audio = r.record(audio_file)

        try:
            text = r.recognize_google(audio, language="") # Use language, from file
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания речи; {str(e)}")

# Example using function transcribe_audio
audio_file_path = "audio.wav"
transcribed_text = transcribe_audio(audio_file_path)
print("Текст из аудиофайла: ")
print(transcribed_text)
