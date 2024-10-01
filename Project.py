import streamlit as st
import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone(language):
    try:
        # Creates an instance of a speech config with specified subscription key and service region.
        speech_config = speechsdk.SpeechConfig(subscription="a4d5d383f9444eb6aabac82bc184f8f8", region="westus")
        speech_config.speech_recognition_language = language
        
        # Creates a recognizer with the given settings
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        st.info("Say something...")

        # Starts speech recognition, and returns after a single utterance is recognized. The speech recognition
        # is performed asynchronously.
        result = speech_recognizer.recognize_once()

        # Check the result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            result_text = "Recognized: {}".format(result.text)
        elif result.reason == speechsdk.ResultReason.NoMatch:
            result_text = "No speech could be recognized: {}".format(result.no_match_details)
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            result_text = "Speech Recognition canceled: {}".format(cancellation_details.reason)
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                result_text += "\nError details: {}".format(cancellation_details.error_details)

        st.success(result_text)

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.title("Speech Recognition with Azure")
st.write("Select the language and click the button below, then say something...")

# Dropdown for language selection
language = st.selectbox("Select Language", ["en-US", "hi-IN"], index=0)

if st.button("Start Recognition"):
    recognize_from_microphone(language)
