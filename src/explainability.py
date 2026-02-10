import shap

def explain(model, X_train, X_test, feature_names):
    explainer = shap.Explainer(model, X_train)
    values = explainer(X_test)
    shap.summary_plot(values, X_test, feature_names=feature_names)
