import os

class Config:
    PORT = int(os.getenv("FLASK_PORT", 5002))
    DATA_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
