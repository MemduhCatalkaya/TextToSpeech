from gtts import gTTS
import tkinter as tk

screen = tk.Tk()
screen.title("Text To Speech")
screen.minsize(500, 500)

language_frame = tk.Frame()
language_frame.pack(padx=30, pady=30)

language_label = tk.Label(language_frame, text="Chose a language",
                          font=("times new roman", 12, "bold", "italic"))
language_label.pack()
language = "en"
text_input = ""


def language_selection():
    global language
    language = var.get()


def convert_click():
    try:
        global text_input
        text_input = text.get(0.1, tk.END)
        tts = gTTS(text_input, lang=language)
        tts.save(f"{file_name_entry.get()}.mp3")
        info_label.config(text=f"Your mp3 file has been saved as {file_name_entry.get()}.mp3")
    except AssertionError:
        info_label.config(text="Please enter your text!!")


var = tk.StringVar()
language_check_english = tk.Radiobutton(language_frame, variable=var, value="en",
                                        text="English (default)", command=language_selection,
                                        font=("times new roman", 10, "bold", "italic"))
language_check_english.pack(anchor="w")

language_check_spanish = tk.Radiobutton(language_frame, variable=var, value="es",
                                        text="Spanish", command=language_selection,
                                        font=("times new roman", 10, "bold", "italic"))
language_check_spanish.pack(anchor="w")

language_check_french = tk.Radiobutton(language_frame, variable=var, value="fr",
                                       text="French", command=language_selection,
                                       font=("times new roman", 10, "bold", "italic"))
language_check_french.pack(anchor="w")

text_label = tk.Label(text="Enter your text to be converted",
                      font=("times new roman", 14, "bold", "italic"))
text_label.pack(pady=5)
text = tk.Text(width=50, height=10)
text.pack()

file_name_label = tk.Label(text="Enter your file name to be saved as mp3",
                           font=("times new roman", 14, "bold", "italic"))
file_name_label.pack(pady=5)

file_name_entry = tk.Entry(width=20)
file_name_entry.pack(pady=5)

convert_button = tk.Button(text="Convert", width=20, height=1, command=convert_click)
convert_button.pack(pady=5)

info_label = tk.Label(text="Please enter your text and file name, then press 'Convert'.",
                      font=("times new roman", 12, "bold", "italic"))
info_label.pack()
screen.mainloop()
