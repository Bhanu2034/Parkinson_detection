import React from "react";

function Header() {
    return (
        <div className="text-center mb-5">
            <h1 className="fw-bold text-primary display-6">
                Parkinson’s Risk Assessment System
            </h1>
            <p className="text-muted fs-6">
                Hybrid Deep Learning (CNN–GRU) based Voice Analysis
            </p>
            <hr className="w-25 mx-auto" />
        </div>
    );
}

export default Header;
