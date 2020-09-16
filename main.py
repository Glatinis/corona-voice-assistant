import os
import time
import infogetter
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

r = sr.Recognizer()

def main():
    countries = infogetter.get_countries()

    case_words = ["cases", "infected", "places", "expected"]
    death_words = ["deaths", "kills", "sets", "debts"]
    recovered_words = ["recovered", "recover", "saved"]
    
    while True:
        speech = getSpeech().lower().split()
        print(speech)
        # speech = "cases in USA".lower().split()
        selected_country = speech2country(speech, countries)
        print(speech)

        time.sleep(2)

        if selected_country != None:
            for word in case_words:
                if word in speech and "in" in speech:
                    print("Cases")
                    say(f"Total cases in {selected_country.name.lower()} are {selected_country.t_cases}.")
                    break

            for word in death_words:
                if word in speech and "in" in speech:
                    print("Deaths")
                    say(f"Total deaths in {selected_country.name.lower()} are {selected_country.t_deaths}.")
                    break

            for word in recovered_words:
                if word in speech and "in" in speech:
                    print("Recovered")
                    say(f"Total recovered in {selected_country.name.lower()} are {selected_country.t_recovered}.")
                    break

            break


def getSpeech():
    while True:
        with sr.Microphone() as source:
            print("Talk.")

            r.adjust_for_ambient_noise(source)
            audio_text = r.listen(source)
            print("stop talking before i give you corona virus.")

            try:
                text = r.recognize_google(audio_text)
                break
            except:
                print("Please try again.")

    return text

def speech2country(speech, countries):
    if "in" in speech:
        print(speech[speech.index("in") + 1])
        for country in countries:
            if country.name.lower() == speech[speech.index("in") + 1]:
                return country
        return None
    return None

def say(text):
    gTTS(text).save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")

main()