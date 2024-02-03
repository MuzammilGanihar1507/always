import gradio as gr
import openai

# Set your OpenAI GPT API key
openai.api_key = "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"

# Function to generate a response using the OpenAI GPT model
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci-002",  # You can choose a different engine if needed

        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Gradio Interface
iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(),
    outputs=gr.Textbox(),
    title="ChatGPT Replica"
)

# Launch the Gradio interface
iface.launch(share=True)