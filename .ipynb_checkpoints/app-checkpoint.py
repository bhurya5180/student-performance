from flask import Flask, jsonify

# Assuming your dataset is stored in a pandas DataFrame called 'df'
# You may need to import pandas and load your dataset into 'df'

# Example dataset
import pandas as pd
df = pd.DataFrame({
    'Hours Studied': [4, 6, 5],
    'Previous Scores': [85, 90, 88],
    'Extracurricular Activities': ['yes', 'no', 'yes'],
    'Sleep Hours': [7, 8, 6],
    'Sample Question Papers Practiced': [2, 3, 1],
    'Performance Index': [80, 85, 82]
})

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return 'Welcome to the Student Performance API!'

@app.route('/students', methods=['GET'])
def get_students():
    # Convert DataFrame to JSON and return
    return jsonify(df.to_dict(orient='records'))

@app.route('/students/<int:index>', methods=['GET'])
def get_student(index):
    # Get data for a specific student by index
    if index >= 0 and index < len(df):
        student_data = df.iloc[index].to_dict()
        return jsonify(student_data)
    else:
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

