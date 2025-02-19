from flask import Blueprint, request, jsonify
from .services.auth_service import login_user, register_user
from .services.recommendation import recommend_course
from .services.quiz_service import adaptive_quiz
from .services.ai_tutor import ai_tutor

main_bp = Blueprint('main', __name__)

@main_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    register_user(data['username'], data['password'])
    return jsonify({"message": "User registered successfully!"})

@main_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if login_user(data['username'], data['password']):
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@main_bp.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json['input']
    recommended_course = recommend_course(user_input)
    return jsonify({"recommended_course": recommended_course})

@main_bp.route('/quiz', methods=['GET'])
def quiz():
    result = adaptive_quiz()
    return jsonify({"result": result})

@main_bp.route('/ask_tutor', methods=['POST'])
def ask_tutor():
    question = request.json['question']
    answer = ai_tutor(question)
    return jsonify({"answer": answer})