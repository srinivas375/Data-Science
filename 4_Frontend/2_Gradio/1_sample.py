"""
Install gradio - pip install --upgrade gradio
run gradio file - py filename.py (for manual reloading)
run gradio file - gradio filename.py (for automatic reloading)
"""

# A simple UI interface

import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn = greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()