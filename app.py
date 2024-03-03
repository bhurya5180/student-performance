from flask import Flask, render_template, request
from utils import get_predicted_score

# Initialize Flask Application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        hours_studied = float(request.form['hours_studied'])
        previous_scores = float(request.form['previous_scores'])
        extracurricular_activities = float(request.form['extracurricular_activities'])
        sleep_hours = float(request.form['sleep_hours'])
        sample_question_papers = float(request.form['sample_question_papers'])

        # Make a prediction using the function
        predicted_score = get_predicted_score(hours_studied, previous_scores, extracurricular_activities, sleep_hours, sample_question_papers)
        print("predicted_score:", predicted_score)

        # Render template with predicted score
        return render_template('index.html', predicted_score=predicted_score)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 , debug=False)
