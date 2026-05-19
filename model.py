import pickle

model = pickle.load(open("model.pkl", "rb"))

def predict(data):
    prob = model.predict_proba([data])[0][1]
    glucose = data[1]

    if glucose < 140:
        status = "Normal"
        risk = "Low"
        suggestion = "Maintain healthy lifestyle"
    elif glucose < 200:
        status = "Prediabetic"
        risk = "Medium"
        suggestion = "Reduce carbs & walk daily"
    else:
        status = "Diabetic"
        risk = "High"
        suggestion = "Consult doctor immediately"

    return glucose, status, risk, suggestion, round(prob*100,2)