import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
df = pd.read_csv("insurance.csv")

# Create Label Encoder
encoder = LabelEncoder()

# Convert text into numbers
df["sex"] = encoder.fit_transform(df["sex"])
df["smoker"] = encoder.fit_transform(df["smoker"])
df["region"] = encoder.fit_transform(df["region"])

# Feature (X)
X = df.drop("charges", axis=1)

# Target (y)
y = df["charges"]

# Create the model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Train the model
model.fit(X,y)

# Save the trained model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")