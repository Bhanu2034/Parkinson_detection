import React from "react";

function UploadForm({ onPredict }) {

    const handleDemoPrediction = () => {
        const demoResult = {
            model: "CNN–GRU",
            risk: 0.73,
            severity: 3.86,
            confidence: "High"
        };
        onPredict(demoResult);
    };

    return (
        <div className="card shadow-sm mb-5">
            <div className="card-body">
                <h5 className="card-title mb-3">
                    <i className="bi bi-upload me-2"></i>
                    Upload Voice Feature File
                </h5>

                <p className="text-muted small">
                    CSV containing extracted voice features (jitter, shimmer, pitch, etc.)
                </p>

                <input
                    type="file"
                    className="form-control mb-3"
                    disabled
                />

                <button
                    className="btn btn-primary px-4"
                    onClick={handleDemoPrediction}
                >
                    <i className="bi bi-play-circle me-2"></i>
                    Run Risk Analysis
                </button>

                <p className="text-muted small mt-3">
                    * Backend integration pending
                </p>
            </div>
        </div>
    );
}

export default UploadForm;
