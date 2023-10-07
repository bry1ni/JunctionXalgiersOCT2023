import pandas as pd
import numpy as np
from numpy.linalg import norm
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
import requests

# Load the datasets
students = pd.read_csv('studentInfo.csv')
courses = pd.read_csv('courseInfo.csv')
feedback = pd.read_csv('recommendationTarget.csv')

# Merge datasets to get a comprehensive view
student_course = pd.merge(students, feedback, on='Student ID')
full_data = pd.merge(student_course, courses, on='Course ID')

# Encode categorical variables
label_encoder = LabelEncoder()
full_data['Major'] = label_encoder.fit_transform(full_data['Major'])
full_data['Language Pref.'] = label_encoder.fit_transform(full_data['Language Pref.'])
full_data['Course Name'] = label_encoder.fit_transform(full_data['Course Name'])

# Create a user-item matrix
user_item_matrix = pd.pivot_table(full_data, values='Past Grade', index='Student ID', columns='Course ID', fill_value=0)

# Convert the user-item matrix to a NumPy array
user_item_matrix_array = user_item_matrix.to_numpy()


# Calculate cosine similarity between students
def cosine_similarity_matrix(matrix):
    norm_matrix = matrix / norm(matrix, axis=-1, keepdims=True)
    similarity_matrix = np.dot(norm_matrix, norm_matrix.T)
    return similarity_matrix


cosine_sim = cosine_similarity(user_item_matrix_array)


# Define a function to get course.txt recommendations
def get_course_recommendations(student_id, top_n=3):
    sim_scores = list(enumerate(cosine_sim[student_id]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]
    course_indices = [i[0] for i in sim_scores]
    recommendations = full_data['Course Name'].iloc[course_indices].unique()
    return recommendations


student_id = 1
recommendations = get_course_recommendations(student_id)
recommendations_names = []
for i in range(3):
    recommendations_names.append(courses['Course Name'][i])
print(f"Course recommendations for Student {student_id}:\n{recommendations_names}")

url = 'https://your-api-endpoint.com/recommendations'
data = {'student_id': student_id, 'recommendations': recommendations.tolist()}
response = requests.post(url, json=data)
