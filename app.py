import gradio as gr

def greet(name):
    return "Hello " + name + ", I'm Scormon!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    demo.launch()