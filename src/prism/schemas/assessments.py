from pydantic import BaseModel, Field


class AgentAssessment(BaseModel):
    score: int = Field(ge=0, le=10)
    assessment: str
    strengths: list[str]
    concerns: list[str]
    evidence: list[str]
    confidence: float = Field(ge=0.0, le=1.0)


class SynthesisResult(BaseModel):
    overall_assessment: str
    strengths: list[str]
    weaknesses: list[str]
    tensions: list[str]
    key_assumptions: list[str]
    recommendation: str
