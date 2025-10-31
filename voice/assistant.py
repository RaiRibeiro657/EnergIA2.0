import speech_recognition as sr
import pyttsx3
import requests
import time

API_URL = "http://localhost:5000"

engine = pyttsx3.init()
engine.setProperty("rate", 170)  
engine.setProperty("volume", 1.0)

def speak(text):
    """Fala uma mensagem e também imprime no terminal."""
    print(f"Assistente: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Escuta um comando de voz e converte para texto."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Diga um comando...")
        r.adjust_for_ambient_noise(source, duration=0.8)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="pt-BR").lower()
        print(f"Você disse: {command}")
        return command
    except sr.UnknownValueError:
        speak("Não entendi, pode repetir por favor?")
        return None
    except sr.RequestError:
        speak("Erro na conexão com o serviço de reconhecimento de voz.")
        return None

def execute_command(command):

    command = command.lower().strip()

    if "ligar tudo" in command:
        r = requests.get(f"{API_URL}/status")
        data = r.json()
        for room in data["comodos"].keys():
            requests.post(f"{API_URL}/toggle", json={"room": room, "state": True})
        speak("Todos os cômodos foram ligados.")
        return

    elif "desligar tudo" in command:
        r = requests.get(f"{API_URL}/status")
        data = r.json()
        for room in data["comodos"].keys():
            requests.post(f"{API_URL}/toggle", json={"room": room, "state": False})
        speak("Todos os cômodos foram desligados.")
        return

    elif "ligar" in command:
        room = command.split("ligar")[-1].strip()
        requests.post(f"{API_URL}/toggle", json={"room": room, "state": True})
        speak(f"{room} ligada.")
        return

    elif "desligar" in command:
        room = command.split("desligar")[-1].strip()
        requests.post(f"{API_URL}/toggle", json={"room": room, "state": False})
        speak(f"{room} desligada.")
        return

    elif "status" in command or "bateria" in command:
        r = requests.get(f"{API_URL}/status")
        status = r.json()
        speak(f"A bateria está em {status['bateria_restante']:.0f} watt-hora.")
        on_rooms = [r for r, info in status["comodos"].items() if info["on"]]
        if on_rooms:
            speak("Os cômodos ligados são: " + ", ".join(on_rooms))
        else:
            speak("Todos os cômodos estão desligados.")
        return

    elif "sair" in command or "encerrar" in command:
        speak("Encerrando o assistente EnergIA. Até logo!")
        exit(0)

    else:
        speak("Comando não reconhecido.")
S
    try:
        r = requests.get(f"{API_URL}/status")
        data = r.json()
        if all(info["on"] for info in data["comodos"].values()):
            speak("Atenção! Todos os cômodos estão ligados. O consumo está muito alto. "
                  "Considere desligar algum aparelho para economizar energia.")
    except:
        pass

if __name__ == "__main__":
    speak("Assistente EnergIA iniciada. Pode falar seus comandos.")
    while True:
        cmd = listen_command()
        if cmd:
            execute_command(cmd)
        time.sleep(0.5)
