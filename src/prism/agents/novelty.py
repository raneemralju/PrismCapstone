from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

from prism.schemas.assessments import AgentAssessment

load_dotenv()


SYSTEM_PROMPT = """
You are PRISM's Novelty Agent.

Your job is to evaluate how original and differentiated a proposed
project idea appears.

Analyze:
- What makes the idea different from common or existing approaches.
- Whether similar solutions are likely to exist.
- What aspects could represent genuine differentiation.
- What claims about novelty are uncertain.

Do not invent specific existing products, papers, or companies.
If you are uncertain, say so.

Return a structured assessment with:
- score: 0 to 10
- assessment
- strengths
- concerns
- evidence
- confidence from 0.0 to 1.0

A high score means the idea appears strongly differentiated.
A low score means the idea appears common or closely aligned with
existing approaches.
"""


def create_novelty_agent() -> ChatOpenAI:
    return ChatOpenAI(
        model="deepseek/deepseek-chat-v3-0324",
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    ).with_structured_output(AgentAssessment)

def assess_novelty(project_idea: str) -> AgentAssessment:
    agent = create_novelty_agent()

    response = agent.invoke(
        [
            ("system", SYSTEM_PROMPT),
            (
                "user",
                f"Evaluate the novelty of this project idea:\n\n{project_idea}",
            ),
        ]
    )

    return response
