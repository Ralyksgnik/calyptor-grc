from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Calyptor Control Test Evaluator Demo")

class ControlTestResult(BaseModel):
    controlId: str = Field(..., example="AC.1.001")
    evidenceIds: Optional[List[str]] = Field(default_factory=list, example=["EVID-001"])
    testResult: str = Field(..., example="pass")
    testedAt: datetime = Field(..., example="2025-12-01T09:00:00Z")
    comments: Optional[str] = None

class EvaluationResponse(BaseModel):
    controlId: str
    status: str
    evaluatedAt: datetime
    details: dict = {}

@app.post("/evaluate-control", response_model=EvaluationResponse)
def evaluate_control(result: ControlTestResult):
    # Simple demo logic: pass => compliant, fail => non-compliant
    status = "compliant" if result.testResult.lower() == "pass" else "non-compliant"
    return {
        "controlId": result.controlId,
        "status": status,
        "evaluatedAt": datetime.utcnow().isoformat(),
        "details": {
            "evidenceIds": result.evidenceIds,
            "comments": result.comments
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
