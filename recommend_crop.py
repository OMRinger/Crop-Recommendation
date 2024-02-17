
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load and preprocess the data
def load_data(filepath):
    data = pd.read_csv(filepath)
    X = data[['soil_type', 'climate', 'precipitation']]
    y = data['crop_type']
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
def train_model(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)
    return clf

# Recommend a crop
def recommend_crop(clf, soil_type, climate, precipitation):
    input_data = pd.DataFrame([[soil_type, climate, precipitation]], columns=['soil_type', 'climate', 'precipitation'])
    return clf.predict(input_data)[0]

if __name__ == "__main__":
    # Example usage
    X_train, X_test, y_train, y_test = load_data('farming_data.csv')
    clf = train_model(X_train, y_train)
    print(f"Recommended crop: {recommend_crop(clf, 'loamy', 'temperate', 500)}")
