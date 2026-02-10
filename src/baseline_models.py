from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_baselines(X_train, X_test, y_train, y_test):
    results = {}

    models = {
        "LR": LogisticRegression(max_iter=1000),
        "SVM": SVC(probability=True),
        "RF": RandomForestClassifier(n_estimators=100)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
        results[name] = acc

        if name == "RF":
            joblib.dump(model, "../models/rf_model.pkl")

    return results
