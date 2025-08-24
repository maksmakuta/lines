# Lines (WIP)

 Backend for Twitter/X like social network

### Features

- Bearer tokens authentification
- Simple pagination (in query)
- Put, get and delete any posts/comments/likes/subscriptions

### Dependencies

- Python 3.13+
- FastAPI
- SQLAlchemy

### Try it out

1. Clone repo

 ```
    git clone --depth=1 https://github.com/maksmakuta/lines && cd lines
 ```

2. Make virtual environment

 ```
 python -m venv venv && source venv/bin/activate 
 ```

3. Install dependencies

 ```
 pip install -r requirements.txt
 ```

4. Run server

 ```
 fastapi dev app/main.py
 ```

5. Get docs

When server is starting you can find urls, it looks like that:

 ```
 server   Server started at http://127.0.0.1:8000
 server   Documentation at http://127.0.0.1:8000/docs
 ```

click on second url to get docs for API, also you can test it there if you want

6. To close server press Ctrl+C

### Author
 Maks Makuta (C) 2025  
 [MIT License](license.md)
