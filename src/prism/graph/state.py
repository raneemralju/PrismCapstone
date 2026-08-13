from typing import TypedDict

from prism.schemas.assessments import AgentAssessment, SynthesisResult

class PRISMState(TypedDict):
    project_idea: str

    novelty: AgentAssessment | None
    feasibility: AgentAssessment | None
    impact: AgentAssessment | None
    risk_ethics: AgentAssessment | None

    synthesis: SynthesisResult | None

    status: str
    errors: list[str]
