# LLM Demo

## Setup
### Adding Hugging Face token
The default model for this project is [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf). You will need to request access to this model, and then set up an API token to use it with this project.
After you receive access, you will need to generate a Hugging Face API token with permissions for the repository, and place it in an environment variable called `HUGGING_FACE_HUB_TOKEN`. 

If you are using a JetBrains IDE, you can set this up in the run configuration by adding `HUGGING_FACE_HUB_TOKEN=your_token` to the Environment variables field.

If you are using VSCode, you can set this up in the launch configuration by adding `"env": {"HUGGING_FACE_HUB_TOKEN": "your_token"}` to the configuration.

And if you are running main.py from the command line, simply set `HUGGING_FACE_HUB_TOKEN=your_token` before invoking `python main.py`.