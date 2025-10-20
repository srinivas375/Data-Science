# Building a chatBot interface, using gradio

import gradio as gr
import random

responses = ["Good morning", "Welcome, to bot", "My pleasure", "Good bye", "See you again", "Happy to hear", "Thanks for the feedback"]

def random_response(message, history):
    return random.choice(responses)

gr.ChatInterface(
    fn = random_response,
    type="messages"
).launch()