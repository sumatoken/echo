import azure.cognitiveservices.speech as speechsdk


def recognise_wake_word():
    """runs keyword spotting locally, with direct access to the result audio"""
    model = speechsdk.KeywordRecognitionModel("keyword.table")

    keyword = "Hey Echo"

    keyword_recognizer = speechsdk.KeywordRecognizer()

    done = False

    def recognized_cb(evt):
        result = evt.result
        if result.reason == speechsdk.ResultReason.RecognizedKeyword:
            print("RECOGNIZED KEYWORD: {}".format(result.text))
        nonlocal done
        done = True

    def canceled_cb(evt):
        result = evt.result
        if result.reason == speechsdk.ResultReason.Canceled:
            print("CANCELED: {}".format(result.cancellation_details.reason))
        nonlocal done
        done = True

    keyword_recognizer.recognized.connect(recognized_cb)
    keyword_recognizer.canceled.connect(canceled_cb)

    result_future = keyword_recognizer.recognize_once_async(model)
    print(
        'Say something starting with "{}" followed by whatever you want...'.format(
            keyword
        )
    )
    result = result_future.get()

    if result.reason == speechsdk.ResultReason.RecognizedKeyword:
        stop_future = keyword_recognizer.stop_recognition_async()
        print("Stopping...")
        stopped = stop_future.get()
        return True
