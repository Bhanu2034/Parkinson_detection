import React from "react";

function ResultCard({ result }) {
    if (!result) return null;

    const riskPercent = (result.risk * 100).toFixed(2);

    const riskColor =
        riskPercent < 40 ? "success" :
            riskPercent < 70 ? "warning" :
                "danger";

    return (
        <div className="card shadow-sm mb-5">
            <div className="card-body">
                <h5 className="card-title mb-4">
                    <i className="bi bi-graph-up-arrow me-2"></i>
                    Prediction Summary
                </h5>

                <span className="badge bg-info text-dark mb-3">
                    Model: {result.model}
                </span>

                <div className="text-center my-4">
                    <h2 className={`fw-bold text-${riskColor}`}>
                        {riskPercent}%
                    </h2>
                    <p className="text-muted mb-0">
                        Estimated Parkinson’s Risk
                    </p>
                </div>

                <p>
                    <strong>Model Confidence:</strong>
                    <span className="badge bg-success ms-2">
                        {result.confidence}
                    </span>
                </p>

                <div className="alert alert-warning small mt-4">
                    <i className="bi bi-exclamation-triangle me-2"></i>
                    This system provides risk estimation only and should not be
                    considered a medical diagnosis.
                </div>
            </div>
        </div>
    );
}

export default ResultCard;
