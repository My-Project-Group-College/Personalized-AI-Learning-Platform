import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///users.db')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key')