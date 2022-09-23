import gradio as gr
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.on_event("startup")
def print_foo():
    print("FOO!!!")

def dream(prompt):
    return ["static/lion.jpg"] * 2, {}

block = gr.Blocks().queue()
with block:
    prompt = gr.Text()
    gallery = gr.Gallery().style(grid=[2], height="auto")
    contains_nfsw = gr.JSON(visible=False)
    btn = gr.Button("Generate")
    btn.click(dream, inputs=prompt, outputs=[gallery, contains_nfsw])


app = gr.mount_gradio_app(app, block, "/gradio")
app.mount("/", StaticFiles(directory="static", html=True), name="static")
