import customtkinter as ctk
from deep_translator import GoogleTranslator
import pyperclip

# APP THEME

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

# MAIN WINDOW

app = ctk.CTk()

app.geometry("900x700")

app.title("CodeAlpha AI Language Translator")

# TITLE

title = ctk.CTkLabel(
    app,
    text="AI Language Translator",
    font=("Arial", 32, "bold")
)

title.pack(pady=20)

# INPUT TEXT

input_text = ctk.CTkTextbox(
    app,
    width=800,
    height=180,
    font=("Arial", 16)
)

input_text.pack(pady=20)

# LANGUAGE LIST

language_names = [

    "english",
    "hindi",
    "french",
    "german",
    "spanish",
    "japanese",
    "korean",
    "arabic",
    "russian",
    "chinese"
]

# SOURCE LANGUAGE

source_lang = ctk.CTkComboBox(
    app,
    values=language_names,
    width=300
)

source_lang.set("english")

source_lang.pack(pady=10)

# TARGET LANGUAGE

target_lang = ctk.CTkComboBox(
    app,
    values=language_names,
    width=300
)

target_lang.set("hindi")

target_lang.pack(pady=10)

# OUTPUT TEXT

output_text = ctk.CTkTextbox(
    app,
    width=800,
    height=180,
    font=("Arial", 16)
)

output_text.pack(pady=20)

# TRANSLATE FUNCTION

def translate_text():

    text = input_text.get(
        "1.0",
        "end"
    ).strip()

    if text == "":
        return

    try:

        translated = GoogleTranslator(
            source=source_lang.get(),
            target=target_lang.get()
        ).translate(text)

        output_text.delete(
            "1.0",
            "end"
        )

        output_text.insert(
            "end",
            translated
        )

    except Exception as e:

        output_text.delete(
            "1.0",
            "end"
        )

        output_text.insert(
            "end",
            f"Translation Error:\n{e}"
        )

# COPY FUNCTION

def copy_text():

    translated = output_text.get(
        "1.0",
        "end"
    )

    pyperclip.copy(translated)

# SWAP LANGUAGES

def swap_languages():

    source = source_lang.get()

    target = target_lang.get()

    source_lang.set(target)

    target_lang.set(source)

# BUTTON FRAME

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

button_frame.pack(pady=20)

# TRANSLATE BUTTON

translate_button = ctk.CTkButton(
    button_frame,
    text="Translate",
    width=180,
    height=50,
    font=("Arial", 16, "bold"),
    command=translate_text
)

translate_button.pack(
    side="left",
    padx=10
)

# COPY BUTTON

copy_button = ctk.CTkButton(
    button_frame,
    text="Copy",
    width=180,
    height=50,
    font=("Arial", 16, "bold"),
    command=copy_text
)

copy_button.pack(
    side="left",
    padx=10
)

# SWAP BUTTON

swap_button = ctk.CTkButton(
    button_frame,
    text="Swap",
    width=180,
    height=50,
    font=("Arial", 16, "bold"),
    command=swap_languages
)

swap_button.pack(
    side="left",
    padx=10
)

# ENTER KEY SUPPORT

app.bind(
    "<Return>",
    lambda event: translate_text()
)

# RUN APP

app.mainloop()