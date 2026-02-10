from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

def preprocess(data):
    X = data.drop("status", axis=1)
    y = data["status"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, "../models/scaler.pkl")

    # Stratified split (accuracy critical)
    X_train, X_temp, y_train, y_temp = train_test_split(
        X_scaled, y, test_size=0.3, stratify=y, random_state=42
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
    )

    return X_train, X_val, X_test, y_train, y_val, y_test, X.columns
