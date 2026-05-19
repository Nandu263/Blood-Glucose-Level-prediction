import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("diabetes.csv")

if df.shape[0] == 0:
    print("Dataset empty!")
    exit()

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained!")