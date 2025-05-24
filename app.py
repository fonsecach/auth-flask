from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')


@app.route('/')
def root():
    return 'Aplication is running!'


if __name__ == '__main__':
    app.run(debug=True)
    
