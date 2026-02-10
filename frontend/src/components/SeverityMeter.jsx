import React from "react";

function SeverityMeter({ severity }) {
    if (severity === null || severity === undefined) return null;

    const level =
        severity < 3 ? "Low" :
            severity < 6 ? "Moderate" :
                "High";

    const barColor =
        severity < 3 ? "bg-success" :
            severity < 6 ? "bg-warning" :
                "bg-danger";

    return (
        <div className="card shadow-sm mb-5">
            <div className="card-body">
                <h5 className="card-title mb-3">
                    <i className="bi bi-speedometer2 me-2"></i>
                    Voice Abnormality Severity
                </h5>

                <div className="progress mb-3" style={{ height: "22px" }}>
                    <div
                        className={`progress-bar ${barColor}`}
                        role="progressbar"
                        style={{ width: `${severity * 10}%` }}
                    >
                        {severity.toFixed(2)}
                    </div>
                </div>

                <p>
                    <strong>Severity Level:</strong>
                    <span className={`badge ${barColor} ms-2`}>
                        {level}
                    </span>
                </p>

                <p className="text-muted small">
                    Derived from autoencoder-based reconstruction error
                </p>
            </div>
        </div>
    );
}

export default SeverityMeter;
