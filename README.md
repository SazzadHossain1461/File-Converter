🔊 Simple Python Text-to-Speech (TTS) GUIThis is a straightforward, single-file Python application that converts text input into audible speech. It uses the Google Text-to-Speech library (gTTS) for high-quality audio generation and provides a simple Graphical User Interface (tkinter) for ease of use.✨ FeaturesGUI Interface: Easy-to-use window for inputting text.Audio Generation: Converts text into a clear MP3 file.Instant Playback: Automatically saves and plays the generated audio.🚀 Setup and InstallationThis project requires Python 3.x.1. Install DependenciesYou only need the gTTS library. The tkinter library is usually included with a standard Python installation.pip install gTTS
2. Run the ApplicationSave the code (e.g., as tts_app.py).Run the file from your terminal:python tts_app.py
3. UsageThe simple GUI window will appear.Type or paste the text you want to hear into the input field.Click the "Start" button.The application will generate the audio, save it as output.mp3 in the same directory, and immediately play the file using your system's default media player.💻 Code OverviewThe core functionality is contained within the texttoSpeech function, which handles fetching the text, calling gTTS, and using the os.system command for playback.# Function to handle TTS conversion and playback
def texttoSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    # Saves the audio file
    output.save("output.mp3")
    # Plays the audio file (uses 'start' command on Windows)
    os.system("start output.mp3")
