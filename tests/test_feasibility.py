from prism.agents.feasibility import assess_feasibility


idea = """
An AI-powered platform that helps university students find internships.
It analyzes their CV, matches them with available internship opportunities,
identifies missing skills, and recommends which opportunities they should
apply to.
"""


result = assess_feasibility(idea)

print("Score:", result.score)
print("Assessment:", result.assessment)
print("Strengths:", result.strengths)
print("Concerns:", result.concerns)
print("Evidence:", result.evidence)
print("Confidence:", result.confidence)
