from translate import Translator
translator = Translator(to_lang="en", from_lang="fr")

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translated_words = {}

for word in french_words:
    translated_words[word] = translator.translate(word)

print(translated_words)