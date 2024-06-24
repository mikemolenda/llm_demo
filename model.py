import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.utils import logging

logging.set_verbosity_info()
logger = logging.get_logger('transformers')

with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

model_name = config['model']['name']
logger.info(f'Loading model {model_name}. This might take several minutes.')
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def run(
        user_input: str,
        conversation_history: list[str],
):
    history_string = '\n'.join(conversation_history)
    inputs = tokenizer.encode_plus(history_string, user_input, return_tensors='pt')
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    conversation_history.append(user_input)
    conversation_history.append(response)
    return response
