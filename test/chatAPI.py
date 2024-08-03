import requests

endpoint = "http://127.0.0.1:8000/intus/chatbot"
r = requests.post(
    endpoint,
    json={"message": "My name is Sourabh, what's your name", "session_name": "sourabh"},
)
print(r.text)  # displays the result body.

r = requests.post(
    endpoint,
    json={
        "message": "How many types of windows are there is construction?",
        "session_name": "sourabh",
    },
)
print(r.text)

r = requests.post(
    endpoint,
    json={"message": "Do you know about the Intus Windows?", "session_name": "sourabh"},
)
print(r.text)

r = requests.post(
    endpoint,
    json={
        "message": "Do you know what's my name, as based on our previous conversation",
        "session_name": "sourabh",
    },
)
print(r.text)
