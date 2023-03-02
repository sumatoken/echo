from engine import (
    generatePrompt,
    generateResponse,
    listenToSpeech,
    listenForWakeWord,
    textToSpeech,
    addToContext,
)
from playsound import playsound


def run():
    recognisedWakeWord = listenForWakeWord()
    while recognisedWakeWord:
        playsound("wake.mp3")
        recognisedSpeech = listenToSpeech()
        if recognisedSpeech == "Exit.":
            exit()
        prompt = generatePrompt(recognisedSpeech)
        response = generateResponse(prompt)
        addToContext(recognisedSpeech, response)
        textToSpeech(response)


run()
