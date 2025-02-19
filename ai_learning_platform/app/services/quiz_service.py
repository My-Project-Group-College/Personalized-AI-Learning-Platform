import random

# Sample quiz questions with difficulty levels
questions = [
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4", "difficulty": "easy"},
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin"], "answer": "Paris", "difficulty": "medium"},
    {"question": "What is the square root of 64?", "options": ["6", "8", "10"], "answer": "8", "difficulty": "hard"},
]

def adaptive_quiz():
    score = 0
    difficulty_level = "easy"
    
    for _ in range(3):  # 3 questions for demonstration
        # Filter questions based on difficulty level
        filtered_questions = [q for q in questions if q["difficulty"] == difficulty_level]
        question = random.choice(filtered_questions)
        
        print("\nQuestion:", question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")
        
        user_answer = input("Your answer (1/2/3): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
            difficulty_level = "hard" if difficulty_level == "medium" else "medium"
        else:
            print("Incorrect!")
            difficulty_level = "easy"
    
    print(f"\nQuiz ended! Your score: {score}/3")
    return score