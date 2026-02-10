from load_data import load_dataset
from preprocess import preprocess
from baseline_models import train_baselines

from cnn_backbone import build_cnn_backbone
from cnn_gru_model import build_cnn_gru
from transformer_encoder import build_transformer

from autoencoder import build_autoencoder, severity_score
from training_utils import (
    get_classification_callbacks,
    get_autoencoder_callbacks
)

from explainability import explain

from sklearn.metrics import accuracy_score, roc_auc_score
import numpy as np
import joblib

# =========================
# 1. Load Dataset
# =========================
data = load_dataset("../data/parkinsons.data")

# =========================
# 2. Preprocessing
# =========================
X_train, X_val, X_test, y_train, y_val, y_test, feature_names = preprocess(data)

# =========================
# 3. Baseline Models
# =========================
baseline_results = train_baselines(X_train, X_test, y_train, y_test)
print("Baseline Accuracies:", baseline_results)

rf = joblib.load("../models/rf_model.pkl")
rf_probs = rf.predict_proba(X_test)[:, 1]
rf_preds = rf.predict(X_test)

rf_acc = accuracy_score(y_test, rf_preds)
rf_auc = roc_auc_score(y_test, rf_probs)

print("\nRandom Forest Test Metrics")
print(f"Accuracy: {rf_acc:.4f}")
print(f"ROC-AUC : {rf_auc:.4f}")

# =========================
# Reshape for DL
# =========================
X_train_seq = X_train.reshape(-1, X_train.shape[1], 1)
X_val_seq   = X_val.reshape(-1, X_val.shape[1], 1)
X_test_seq  = X_test.reshape(-1, X_test.shape[1], 1)

# =========================
# 4. CNN Backbone
# =========================
cnn = build_cnn_backbone((X_train.shape[1], 1))

cnn.fit(
    X_train_seq, y_train,
    validation_data=(X_val_seq, y_val),
    epochs=80,
    batch_size=16,
    callbacks=get_classification_callbacks("cnn_backbone"),
    verbose=1
)

cnn_probs = cnn.predict(X_test_seq).ravel()
cnn_preds = (cnn_probs >= 0.5).astype(int)

cnn_acc = accuracy_score(y_test, cnn_preds)
cnn_auc = roc_auc_score(y_test, cnn_probs)

print("\nCNN Test Metrics")
print(f"Accuracy: {cnn_acc:.4f}")
print(f"ROC-AUC : {cnn_auc:.4f}")

# =========================
# 5. CNN–GRU (FINAL MODEL)
# =========================
cnn_gru = build_cnn_gru((X_train.shape[1], 1))

cnn_gru.fit(
    X_train_seq, y_train,
    validation_data=(X_val_seq, y_val),
    epochs=80,
    batch_size=16,
    callbacks=get_classification_callbacks("cnn_gru"),
    verbose=1
)

cnn_gru_probs = cnn_gru.predict(X_test_seq).ravel()
cnn_gru_preds = (cnn_gru_probs >= 0.5).astype(int)

cnn_gru_acc = accuracy_score(y_test, cnn_gru_preds)
cnn_gru_auc = roc_auc_score(y_test, cnn_gru_probs)

print("\nCNN–GRU Test Metrics (FINAL)")
print(f"Accuracy: {cnn_gru_acc:.4f}")
print(f"ROC-AUC : {cnn_gru_auc:.4f}")

# =========================
# 6. Transformer Encoder
# =========================
transformer = build_transformer((X_train.shape[1], 1))

transformer.fit(
    X_train_seq, y_train,
    validation_data=(X_val_seq, y_val),
    epochs=80,
    batch_size=16,
    callbacks=get_classification_callbacks("transformer"),
    verbose=1
)

tr_probs = transformer.predict(X_test_seq).ravel()
tr_preds = (tr_probs >= 0.5).astype(int)

tr_acc = accuracy_score(y_test, tr_preds)
tr_auc = roc_auc_score(y_test, tr_probs)

print("\nTransformer Test Metrics")
print(f"Accuracy: {tr_acc:.4f}")
print(f"ROC-AUC : {tr_auc:.4f}")

# =========================
# 7. Autoencoder (Severity)
# =========================
autoencoder = build_autoencoder(X_train.shape[1])

autoencoder.fit(
    X_train, X_train,
    validation_data=(X_val, X_val),
    epochs=80,
    batch_size=16,
    callbacks=get_autoencoder_callbacks("autoencoder"),
    verbose=1
)

severity = severity_score(autoencoder, X_test)
print("\nVoice Abnormality Severity:", severity, "%")

# =========================
# 8. SHAP Explainability
# =========================
explain(rf, X_train, X_test, feature_names)

# =========================
# 9. Save Final Results
# =========================
with open("../models/final_results.txt", "w") as f:
    f.write("MODEL PERFORMANCE SUMMARY\n")
    f.write(f"Random Forest  - Acc: {rf_acc:.4f}, AUC: {rf_auc:.4f}\n")
    f.write(f"CNN            - Acc: {cnn_acc:.4f}, AUC: {cnn_auc:.4f}\n")
    f.write(f"CNN-GRU (Final)- Acc: {cnn_gru_acc:.4f}, AUC: {cnn_gru_auc:.4f}\n")
    f.write(f"Transformer    - Acc: {tr_acc:.4f}, AUC: {tr_auc:.4f}\n")
    f.write(f"Severity Score : {severity}%\n")
