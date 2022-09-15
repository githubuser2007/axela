import speech_recognition as s
import wikipedia as w
import pyjokes
import pyttsx3

engine = pyttsx3.init()
sr = s.Recognizer()

print('listening')
try:
	with s.Microphone() as m:
		audio = sr.listen(m)
		query = sr.recognize_google(audio, language='eng-in')


			

		if 'joke' in query:
			joke = pyjokes.get_joke(language='en', category='neutral')
			print(f'heres a joke for you: {joke}')
			engine.say(joke)
			engine.runAndWait()

		elif 'search' in query:
			result = w.summary(query)
			print(f'you have searched for {query}')
			print(result)
			engine.say(result)
			engine.runAndWait()
			
		else:
			pass

except (w.exceptions.PageError,s.UnknownValueError):
	print('dint catch that')