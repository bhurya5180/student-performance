import pickle
import numpy as np

def get_predicted_score(Hours_Studied, Previous_Scores, Extracurricular_Activities,
                        Sleep_Hours, Sample_Question_Papers_Practiced):
    model_file_path = r"D:\MACHINE LERNING\LINEAR RIGRESSION\linear_reg_model.pkl"
    with open(model_file_path, 'rb') as f:
        model = pickle.load(f)

    test_array = np.array([[Hours_Studied, Previous_Scores, Extracurricular_Activities,
                            Sleep_Hours, Sample_Question_Papers_Practiced]])
    performance_score = model.predict(test_array)
    return performance_score
