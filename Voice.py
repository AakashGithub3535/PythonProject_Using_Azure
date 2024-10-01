import azure.cognitiveservices.speech as speechsdk
def recognize_from_microphone():
    try:
        # Creates an instance of a speech config with specified subscription key and service region.
        speech_config = speechsdk.SpeechConfig(subscription="a4d5d383f9444eb6aabac82bc184f8f8", region="westus")
        
        # Creates a recognizer with the given settings
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        print("Say something...")

        # Starts speech recognition, and returns after a single utterance is recognized. The speech recognition
        # is performed asynchronously.
        result = speech_recognizer.recognize_once()

        # Check the result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    recognize_from_microphone()
