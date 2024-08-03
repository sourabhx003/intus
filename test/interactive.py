import requests


def main():
    endpoint = "http://127.0.0.1:8000/intus/chatbot"

    while True:
        exit_condition = int(input("Do you want to exit(0-> No and 1-> Yes): "))

        if exit_condition == 1:
            break

        prompt = input("Enter your prompt: ")
        r = requests.post(
            endpoint,
            json={"message": prompt, "session_name": "sourabh"},
        )
        print(r.text)  # displays the result body.


if __name__ == "__main__":
    main()
