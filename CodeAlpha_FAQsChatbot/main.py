import customtkinter as ctk
from tkinter import END

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# DOWNLOAD NLTK DATA

nltk.download('punkt')

# APP THEME

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

# FAQ DATASET

faq_questions = [

    "What is artificial intelligence?",
    "What is machine learning?",
    "What is deep learning?",
    "What is Python?",
    "What is OpenCV?",
    "What is computer vision?",
    "What is NLP?",
    "What is TensorFlow?",
    "What is YOLO?",
    "What is generative AI?",
    "What is data science?",
    "What is a chatbot?",
    "What is supervised learning?",
    "What is unsupervised learning?",
    "What is neural network?"
]

faq_answers = [

    "Artificial Intelligence is the simulation of human intelligence by machines.",

    "Machine Learning is a subset of AI where systems learn from data.",

    "Deep Learning uses neural networks to solve complex AI problems.",

    "Python is a popular programming language used in AI development.",

    "OpenCV is a computer vision library used for image and video processing.",

    "Computer Vision helps computers understand images and videos.",

    "NLP stands for Natural Language Processing.",

    "TensorFlow is a deep learning framework developed by Google.",

    "YOLO is a real-time object detection algorithm.",

    "Generative AI creates new content like text, images, and code.",

    "Data Science involves extracting insights and knowledge from data.",

    "A chatbot is a software application that communicates with users.",

    "Supervised learning uses labeled datasets to train AI models.",

    "Unsupervised learning finds hidden patterns in unlabeled data.",

    "A neural network is a brain-inspired AI system used in deep learning."
]

# VECTORIZE QUESTIONS

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(faq_questions)

# CHATBOT RESPONSE FUNCTION

def chatbot_response(user_input):

    # LOWERCASE INPUT

    user_input = user_input.lower()

    # NORMALIZE COMMON TERMS

    replacements = {

        "ai": "artificial intelligence",
        "ml": "machine learning",
        "cv": "computer vision",
        "nlp": "natural language processing"
    }

    for short, full in replacements.items():

        user_input = user_input.replace(short, full)

    # VECTORIZE USER INPUT

    user_vector = vectorizer.transform([user_input])

    # CALCULATE SIMILARITY

    similarity = cosine_similarity(user_vector, X)

    score = similarity.max()

    index = similarity.argmax()

    # UNKNOWN QUESTION HANDLING

    if score < 0.2:

        return "Sorry, I don't understand that question."

    return faq_answers[index]

# SEND MESSAGE FUNCTION

def send_message():

    user_input = entry.get()

    if user_input.strip() == "":
        return

    # USER MESSAGE

    chatbox.insert(
        END,
        f"\n🧑 You:\n{user_input}\n",
    )

    # BOT RESPONSE

    response = chatbot_response(user_input)

    chatbox.insert(
        END,
        f"\n🤖 AI Assistant:\n{response}\n",
    )

    # AUTO SCROLL

    chatbox.see(END)

    # CLEAR INPUT

    entry.delete(0, END)

# MAIN WINDOW

app = ctk.CTk()

app.geometry("900x700")

app.title("CodeAlpha AI FAQ Chatbot")

# TITLE

title = ctk.CTkLabel(
    app,
    text="AI FAQ Chatbot",
    font=("Arial", 30, "bold")
)

title.pack(pady=20)

# CHATBOX

chatbox = ctk.CTkTextbox(
    app,
    width=800,
    height=500,
    font=("Arial", 16),
    corner_radius=15
)

chatbox.pack(
    padx=20,
    pady=20
)

# INPUT FRAME

input_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

input_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

# ENTRY FIELD

entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Ask something...",
    height=50,
    font=("Arial", 16)
)

entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)

# SEND BUTTON

send_button = ctk.CTkButton(
    input_frame,
    text="Send",
    width=120,
    height=50,
    font=("Arial", 16, "bold"),
    command=send_message
)

send_button.pack(side="right")

# ENTER KEY SUPPORT

entry.bind(
    "<Return>",
    lambda event: send_message()
)

# RUN APP

app.mainloop()