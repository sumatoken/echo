import os
import azure.cognitiveservices.speech as speechsdk
from speechSynthetis import textToSpeech
from wake import recognise_wake_word
from engine import generatePrompt, generateResponse

speech_config = speechsdk.SpeechConfig(
    subscription=os.environ.get("AZURE_SPEECH_KEY"),
    region=os.environ.get("AZURE_SPEECH_REGION"),
)
speech_config.speech_recognition_language = "en-US"
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=audio_config
)


def run():
    recognised_keyword = recognise_wake_word()
    print(recognised_keyword)
    if recognised_keyword:
        print("How may I help you?")
        textToSpeech(
            "How may I help you?",
            speech_config=speech_config,
            audio_config=audio_config,
        )
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            prompt = generatePrompt(speech_recognition_result.text)
            response = generateResponse(prompt)
            textToSpeech(
                response,
                speech_config=speech_config,
                audio_config=audio_config,
            )
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print(
                "No speech could be recognized: {}".format(
                    speech_recognition_result.no_match_details
                )
            )
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details))


while True:
    run()
