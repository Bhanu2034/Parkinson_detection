function SeverityMeter({ severity }) {
    if (severity === null) return null;

    return (
        <div className="card">
            <h3>Voice Abnormality Severity</h3>
            <progress value={severity} max="10" style={{ width: "100%" }}></progress>
            <p>{severity}% severity detected</p>
        </div>
    );
}

export default SeverityMeter;
