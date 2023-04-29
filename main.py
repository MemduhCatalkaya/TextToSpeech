from gtts import gTTS
print("Welcome to 'Text to Speech' Converter!\n-----------------------\nFor English please type 'en'\nFor French please type 'fr'\nFor Spanish please type 'es'\n-----------------------")
while True:
    my_lang = input("Chose language: ").lower()
    if my_lang in ["en", "es", "fr"]:
        while True:
            try:
                my_text = input("Please enter your text: ")
                tts = gTTS(my_text, lang=my_lang)
                file_name = input("Please enter your file name: ")
                tts.save(f"{file_name}.mp3")
                print(f"-----------------------\nYour mp3 file has been saved as {file_name}.mp3.\nEnjoy!")
                break
            except AssertionError:
                print("Please enter a text!!")
        break
    else:
        print("Please enter a valid language!")
