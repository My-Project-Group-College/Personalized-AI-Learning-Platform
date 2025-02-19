from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample course data
courses = {
    "Python Basics": "Learn the basics of Python programming.",
    "Advanced Python": "Deep dive into Python's advanced features.",
    "Machine Learning": "Introduction to machine learning concepts.",
    "Data Science": "Learn data analysis and visualization.",
}

# Convert course descriptions to TF-IDF vectors
course_titles = list(courses.keys())
course_descriptions = list(courses.values())
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(course_descriptions)

def recommend_course(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    recommended_index = np.argmax(similarities)
    return course_titles[recommended_index]