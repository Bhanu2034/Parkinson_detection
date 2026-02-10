function UploadForm({ onPredict }) {
    const handleSubmit = (e) => {
        e.preventDefault();

        // 🔹 MOCKED RESPONSE (replace with backend later)
        const mockResult = {
            prediction: "Parkinson’s Detected",
            probability: 0.8693,
            severity: 3.86
        };

        onPredict(mockResult);
    };

    return (
        <div className="card">
            <h3>Upload Voice Feature File</h3>
            <form onSubmit={handleSubmit}>
                <input type="file" accept=".csv" required />
                <br />
                <button type="submit">Analyze Voice</button>
            </form>
        </div>
    );
}

export default UploadForm;
