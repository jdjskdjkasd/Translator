from translate import Translator

tr = Translator(from_lang="ru", to_lang="en")
ucInp = input()

print(tr.translate(ucInp))