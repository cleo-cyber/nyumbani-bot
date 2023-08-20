import openai
import gradio as gr
# from decouple import config
# API_KEY=config('API_KEY')
with open('hidden.txt') as f:
    openai.api_key = f.read()

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Nyumbani AI Chatbot",
             description="Here to help you with your questions about your Housing needs.",
             theme="compact").launch(share=True)
2