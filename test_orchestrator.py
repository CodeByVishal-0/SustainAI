from agents.orchestrator import orchestrator

report = orchestrator(
    city="Delhi",
    question="How sustainable is Delhi today?"
)

print(report)