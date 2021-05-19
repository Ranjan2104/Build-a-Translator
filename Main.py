from googletrans import Translator

text = '''  Der du von dem Himmel bist,
Alles Leid und Schmerzen stillest,
Den, der doppelt elend ist,
Doppelt mit Erquickung füllest;
Ach, ich bin des Treibens müde!. '''

# Create an instance of Translator to use
translator = Translator()
# detect the language
lang = translator.detect(text)
print(lang)
# Call the translate()
res = translator.translate(text)
#print the result
print(res.text)
