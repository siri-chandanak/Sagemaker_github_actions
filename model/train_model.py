import os
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Ensure inference directory exists
output_dir = os.path.join(os.path.dirname(__file__), "..", "inference")
os.makedirs(output_dir, exist_ok=True)

# Save model
model_path = os.path.join(output_dir, "iris_model.pkl")
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
