import gradio as gr
import urllib.parse
from PIL import Image
import requests
from io import BytesIO

def generate_image(prompt):
    # Encode the prompt text into a URL format
    encoded_prompt = urllib.parse.quote(prompt)
    
    # Pollinations.ai generates images on-the-fly without an API key
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true"
    
    # Fetch image from the endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise ValueError(f"Failed to fetch image: {response.status_code}")

# Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# AI Image Generator")
    with gr.Row(equal_height=True):
        textbox = gr.Textbox(lines=1, show_label=False, placeholder="e.g. A cute cat sitting on a couch...")
        button = gr.Button("Generate", variant="primary")
        image = gr.Image(height=400)

    button.click(
        fn=generate_image,
        inputs=textbox,
        outputs=image,
    )

demo.launch(share=True)