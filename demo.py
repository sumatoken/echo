from engine import (
    generatePrompt,
    generateResponse,
    listenToSpeech,
    listenForWakeWord,
    textToSpeech,
    addToContext,
)


def run():
    recognisedWakeWord = listenForWakeWord()
    while recognisedWakeWord:
        recognisedSpeech = listenToSpeech()
        if recognisedSpeech == "exit.":
            exit()
        prompt = generatePrompt(recognisedSpeech)
        response = generateResponse(prompt)
        addToContext(recognisedSpeech, response)
        textToSpeech(response)


run()
