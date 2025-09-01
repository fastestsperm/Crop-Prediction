


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv(r'C:\MLP1\Crop_recommendation.csv')

print("Columns:", df.columns.tolist())
print("Sample data:", df.head())
print("Unique labels:", df['label'].unique())

x = df.drop('label', axis=1)
y = df['label']

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(xtrain, ytrain)

test_features = [[90, 42, 43, 20.8, 82.0, 6.5, 202.9]]  # Sample input
print("Test prediction:", model.predict(test_features))

pickle.dump(model, open("model.pkl", "wb"))
