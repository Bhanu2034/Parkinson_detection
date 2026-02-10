import { useState } from "react";

import Header from "../components/Header";
import UploadForm from "../components/UploadForm";
import ResultCard from "../components/ResultCard";
import SeverityMeter from "../components/SeverityMeter";

function Home() {
    const [result, setResult] = useState(null);

    return (
        <div className="container py-4">
            <Header />
            <UploadForm onPredict={setResult} />

            {result && (
                <>
                    <ResultCard result={result} />
                    <SeverityMeter severity={result.severity} />
                </>
            )}
        </div>
    );
}

export default Home;
