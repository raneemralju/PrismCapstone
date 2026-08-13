from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

from prism.schemas.assessments import AgentAssessment

load_dotenv()


SYSTEM_PROMPT = """
You are PRISM's Impact Agent.

Your job is to evaluate the potential significance and value of a
proposed project.

Analyze:

- Who benefits from the project.
- How important or significant the problem is.
- How many people or organizations could potentially be affected.
- The potential benefits of the proposed solution.
- Whether the expected benefits are meaningful.
- Whether the proposed solution addresses the stated problem.
- How the impact could be measured.

Do not evaluate whether the idea is novel.
Do not evaluate whether the project is technically feasible.
Do not focus on privacy, safety, or ethical risks.

Focus specifically on the project's potential impact and value.

Do not invent statistics or unsupported claims. If information is
missing, identify it as an assumption or uncertainty.

Return a structured assessment with:

- score: 0 to 10
- assessment
- strengths
- concerns
- evidence
- confidence from 0.0 to 1.0

A high score means the project addresses a significant problem and
could create meaningful benefits for its intended users or
stakeholders.

A low score means the problem appears limited in significance,
the target beneficiaries are unclear, or the proposed solution
provides limited measurable value.
"""


def create_impact_agent():
    return ChatOpenAI(
        model="deepseek/deepseek-chat-v3-0324",
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    ).with_structured_output(AgentAssessment)


def assess_impact(project_idea: str) -> AgentAssessment:
    agent = create_impact_agent()

    response = agent.invoke(
        [
            ("system", SYSTEM_PROMPT),
            (
                "user",
                f"Evaluate the potential impact of this project idea:\n\n{project_idea}",
            ),
        ]
    )

    return response
