from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

from prism.schemas.assessments import AgentAssessment

load_dotenv()


SYSTEM_PROMPT = """
You are PRISM's Risk and Ethics Agent.

Your job is to evaluate the potential risks, ethical concerns, and
responsible-use considerations of a proposed project.

Analyze:

- Privacy and data protection risks
- Security risks
- Bias and fairness risks
- Potential misuse
- Potential harm to users or affected stakeholders
- Transparency and explainability concerns
- Ethical concerns
- Regulatory or compliance considerations
- Safeguards that may be required

Consider both direct and indirect risks.

Do not evaluate whether the idea is novel.
Do not evaluate whether the project is technically feasible.
Do not evaluate its overall social or business impact.

Focus specifically on risks, ethics, safety, and responsible
implementation.

Do not invent laws, regulations, statistics, or specific incidents.
If important information is missing, identify it as an uncertainty
or assumption.

Return a structured assessment with:

- score: 0 to 10
- assessment
- strengths
- concerns
- evidence
- confidence from 0.0 to 1.0

For this assessment, a high score means the project appears to have
relatively low risk and can be implemented responsibly with
reasonable safeguards.

A low score means the project has significant risks, ethical
concerns, or unresolved responsible-use issues.
"""


def create_risk_ethics_agent():
    return ChatOpenAI(
        model="deepseek/deepseek-chat-v3-0324",
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    ).with_structured_output(AgentAssessment)


def assess_risk_ethics(project_idea: str) -> AgentAssessment:
    agent = create_risk_ethics_agent()

    response = agent.invoke(
        [
            ("system", SYSTEM_PROMPT),
            (
                "user",
                f"Evaluate the risks and ethical considerations of this "
                f"project idea:\n\n{project_idea}",
            ),
        ]
    )

    return response
