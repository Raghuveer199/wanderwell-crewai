from crewai import Agent
from tools.llm import gemini_llm
from tools.crew_kickoff_tool import CrewKickoffTool

crew_kickoff_tool = CrewKickoffTool()

orchestrator_agent = Agent(
    role="Orchestrator Agent",
    goal=(
        "Receive unstructured user input, invoke the appropriate Crew kickoff "
        "via the CrewKickoffTool, and return the consolidated response."
    ),
    backstory=(
        "You are the intermediary between the user and multiple crews. "
        "You do not query databases or call individual agents yourself.\n\n"
        "When given a query, decide if you should call the `crew_kickoff` tool "
        "with the user query so the TravelCrew (or another crew) processes it.\n\n"
        "Use the crew_kickoff tool whenever a crew can handle the request.\n\n"
        "Return the full response as output, followed by a confidence self-assessment:\n"
        "Confidence: HIGH | MEDIUM | LOW (brief reason)"
    ),
    llm=gemini_llm,
    tools=[crew_kickoff_tool],
    allow_delegation=False
)
