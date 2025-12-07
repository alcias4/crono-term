
import pyttsx3


def vouce_text(text: str) -> None:
    # Opcione facil
    #pyttsx3.speak(text)

    engine =  pyttsx3.init()

    # Velocidad (rate)
    rate  = engine.getProperty("rate") # Obtener la velocidad actual
    engine.setProperty("rate", 100)
    print("Velocidad: ",rate)

    # Volumne
    volum = engine.getProperty("volume")
    print(volum)
    engine.setProperty("volume", 3.0)

    # Voz
    voice = engine.getProperty("voices")
    engine.setProperty("voice", voice[4].id) # type: ignore


    engine.say(text)
    engine.runAndWait()
    engine.stop()
