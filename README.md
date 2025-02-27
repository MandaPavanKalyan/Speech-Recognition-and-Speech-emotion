# Speech Recognition and Sentiment Analysis  

## Overview  
This project demonstrates two key functionalities:  
1. **Speech Recognition and Text-to-Speech (TTS)** – Captures audio input, converts it to text, and reads it back using a speech engine.  
2. **Sentiment Analysis on Speech Input** – Analyzes the sentiment of the recognized speech using VADER sentiment analysis.  

---

## Steps Involved  

### 1. Import Required Libraries  
- **SpeechRecognition (`speech_recognition`)**: For capturing and converting speech to text.  
- **pyttsx3**: For text-to-speech conversion.  
- **VADER Sentiment Analysis (`vaderSentiment`)**: For analyzing the sentiment of spoken words.  

---

### 2. Speech Recognition and Text-to-Speech  
- The script continuously listens for speech input using a microphone.  
- It processes the audio using Google's Speech-to-Text API.  
- The recognized speech is printed and then spoken back using `pyttsx3`.  

---

### 3. Sentiment Analysis on Speech Input  
- Once speech is recognized, the text is passed through **VADER SentimentIntensityAnalyzer**.  
- The sentiment is analyzed, returning scores for **positive, negative, and neutral sentiment**, along with an overall **compound score**.  

---

## Installation  

Ensure you have Python installed, then install the required dependencies:  

```bash
pip install SpeechRecognition pyttsx3 vaderSentiment
```

---

## Usage  

Run the script using:  

```bash
python speech_sentiment.py
```

After running:  
1. The script will **calibrate the microphone** to filter out background noise.  
2. It will prompt the user to start speaking.  
3. The spoken words will be **recognized and spoken back** using TTS.  
4. Sentiment analysis will be performed, and the **sentiment scores** will be displayed.  

---

## Example Output  

```
wait for the calibration  
start speaking...  
Did you say: "I love programming!"  
{'neg': 0.0, 'neu': 0.4, 'pos': 0.6, 'compound': 0.85}
```

---

## Future Enhancements  
- Support for **multi-language speech recognition**.  
- Integration with **Google Translate** for language translation.  
- Improved accuracy using **custom speech models**.  

---

## Author  
Developed by **[Manda Pavan Kalyan]**  
