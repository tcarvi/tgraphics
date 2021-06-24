import speech_recognition as sr


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Informe seu comando:")

        audio = r.listen(source)

        print("Processando comando em input_planta_structure.json .... ")

        # recognize speech using google

        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Estrutura de comandos atualizados = ")


        except Exception as e:
            print("Error :  " + str(e))




        # write audio
        with open("recordedComando1.wav", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()