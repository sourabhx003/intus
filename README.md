# Intus Windows ChatBot

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and python3.10:

### Docker

```sh
# Clone this repository
git clone https://github.com/sourabhx003/intus.git

# Go into the repository
cd intus

# Install dependencies
docker build -t intus_chatbot .

# Run the app
docker run -p 8000:8000 intus_chatbot
```

### Local

```sh
# Clone this repository
git clone https://github.com/sourabhx003/intus.git

# Go into the repository
cd intus

# Create virtual env
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
fastapi dev main.py
```

## Calling the api

### Request package

Open a new terminal which will call the endpoints

```sh
# Calls our API
python3 test/chatAPI.py
# interactive API calls
python3 test/interactive.py
```

### Curl

Open a new terminal which will call the endpoints

```sh
# Calls our API
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"message":"How many types of windows are there is construction?", "session_name": "sourabh"}' \
  http://127.0.0.1:8000/intus/chatbot
```



### For formatting and linting
We're using ruff for formatting and lniting [Ruff](https://docs.astral.sh/ruff/)

```sh
ruff check                  # Lint all files in the current directory.
ruff check --fix            # Lint all files in the current directory, and fix any fixable errors.
ruff format                 # Formats all files in the current directory.
```

## License

MIT

