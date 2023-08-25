from fastapi import FastAPI
import gradio as gr
import time

app = FastAPI()

def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i+1]
        
with gr.Blocks() as chat_demo:
  chat_demo.queue()
  gr.ChatInterface(slow_echo)


app = gr.mount_gradio_app(app, chat_demo, path="/")

# import gradio as gr
# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles


# app = FastAPI()

# @app.on_event("startup")
# def print_foo():
#     print("FOO!!!")

# def dream(prompt):
#     return ["static/lion.jpg"] * 2, {}

# block = gr.Blocks()
# with block:
#     prompt = gr.Text()
#     gallery = gr.Gallery().style(grid=[2], height="auto")
#     contains_nfsw = gr.JSON(visible=False)
#     btn = gr.Button("Generate")
#     btn.click(dream, inputs=prompt, outputs=[gallery, contains_nfsw])

# block.queue()

# app = gr.mount_gradio_app(app, block, "/gradio")
# app.mount("/", StaticFiles(directory="static", html=True), name="static")
