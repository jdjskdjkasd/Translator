from googletrans import Translator

#from types import new_class
#pip install googletrans==4.0.0-rc1

def Translaitor(text, dest_lang=str):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

class main():
    print("---Перводчик с русского, на разные языки---")
    print("Введите переводимое слово: ")
    text_to_translate = input()
    print("На какой язык вы хотите перевести?"
          "\n1 - Английский"
          "\n2 - Испанский"
          "\n3 - Французкий"
          "\n4 - Сразу на все 3 языка")
    userInp = int(input())
    match(userInp):
        case 1:
            translated_text = Translaitor(text_to_translate, "en")
            print(f"Оригинальный текст: {text_to_translate}")
            print(f"Переведенный текст: {translated_text}")
        case 2:
            translated_text = Translaitor(text_to_translate, "ca")
            print(f"Оригинальный текст: {text_to_translate}")
            print(f"Переведенный текст: {translated_text}")
        case 3:
            translated_text = Translaitor(text_to_translate, "fr")
            print(f"Оригинальный текст: {text_to_translate}")
            print(f"Переведенный текст: {translated_text}")
        case 4:
            print("---English---")
            translated_text = Translaitor(text_to_translate, "en")
            print(f"Оригинальный текст: {text_to_translate}")
            print(f"Переведенный текст: {translated_text}")

            print("---Spanish---")
            translated_text = Translaitor(text_to_translate, "ca")
            print(f"Оригинальный текст: {text_to_translate}")
            print(f"Переведенный текст: {translated_text}")

            print("---French---")
            translated_text = Translaitor(text_to_translate, "fr")
            print(f"Оригинальный текст: {text_to_translate}")
            print(f"Переведенный текст: {translated_text}")

main()
