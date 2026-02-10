import { useState } from "react";
import Header from "../components/Header";
import UploadForm from "../components/UploadForm";
import ResultCard from "../components/ResultCard";
import SeverityMeter from "../components/SeverityMeter";

function Home() {
    const [result, setResult] = useState(null);

    return (
        <div className="container">
            <Header />
            <UploadForm onPredict={setResult} />
            <ResultCard result={result} />
            <SeverityMeter severity={result ? result.severity : null} />
        </div>
    );
}

export default Home;
