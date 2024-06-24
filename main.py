from model import run


def main():
    conversation_history = []
    while True:
        user_input = input('You: ')
        if user_input == 'exit':
            break
        response = run(user_input, conversation_history)
        print(f'Bot: {response}')


if __name__ == '__main__':
    main()
