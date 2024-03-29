import gradio as gr
from agent import Agent

def main():
  llm_agent = Agent()

  demo = gr.Interface(fn=llm_agent.run, inputs=gr.Textbox(label="Query"),
                      outputs=[gr.Textbox(label="Response"), gr.Textbox(label="Snippets")])
  demo.launch(server_name="0.0.0.0", server_port=8080)


if __name__ == '__main__':
  main()

