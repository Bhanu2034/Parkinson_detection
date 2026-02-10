function ResultCard({ result }) {
    if (!result) return null;

    return (
        <div className="card">
            <h3>Classification Result</h3>
            <p>
                <strong>Status:</strong>{" "}
                {result.prediction}
            </p>
            <p>
                <strong>Prediction Confidence:</strong>{" "}
                {(result.probability * 100).toFixed(2)}%
            </p>
        </div>
    );
}

export default ResultCard;
