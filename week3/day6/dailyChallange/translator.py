from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator()

translations = translator.translate(french_words, src='fr', dest='en')

translated_dict = {trans.origin: trans.text for trans in translations}

print(translated_dict)
