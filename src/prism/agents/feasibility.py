from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

from prism.schemas.assessments import AgentAssessment

load_dotenv()


SYSTEM_PROMPT = """
You are PRISM's Feasibility Agent.

Your job is to evaluate whether a proposed project can realistically
be built and implemented.

Analyze:

- Technical complexity
- Required technologies and infrastructure
- Required data, APIs, or other resources
- Implementation difficulty
- Time and development constraints
- Skills and expertise likely required
- Dependencies and assumptions
- Major technical or practical blockers

Do not evaluate whether the idea is novel or impactful.
Focus specifically on whether it is realistically buildable.

Do not invent specific technical resources or requirements that are
not supported by the project description. If information is missing,
identify it as an assumption or uncertainty.

Return a structured assessment with:

- score: 0 to 10
- assessment
- strengths
- concerns
- evidence
- confidence from 0.0 to 1.0

A high score means the project appears realistic and achievable
with reasonable resources and constraints.

A low score means the project has significant technical, resource,
time, or implementation barriers.
"""


def create_feasibility_agent():
    return ChatOpenAI(
        model="deepseek/deepseek-chat-v3-0324",
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    ).with_structured_output(AgentAssessment)


def assess_feasibility(project_idea: str) -> AgentAssessment:
    agent = create_feasibility_agent()

    response = agent.invoke(
        [
            ("system", SYSTEM_PROMPT),
            (
                "user",
                f"Evaluate the feasibility of this project idea:\n\n{project_idea}",
            ),
        ]
    )

    return response
