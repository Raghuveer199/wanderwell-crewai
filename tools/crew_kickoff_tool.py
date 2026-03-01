from crewai.tools import BaseTool
from crewai import Crew
from crew.travel_crew import travel_crew  # TravelCrew
from typing import Any, ClassVar

# Use the imported Crew instance
travel_crew_instance: Crew = travel_crew


class CrewKickoffTool(BaseTool):
    """
    A tool that allows an agent to invoke a Crew kickoff.
    """

    name: ClassVar[str] = "crew_kickoff"
    description: str = "Invokes a Crew kickoff with a user query for processing.Expects user_query in the input."

    def _run(self, user_query: str) -> str:
        """
        user_query: raw string forwarded from the agent
        """
        # Kickoff the TravelCrew with the query
        try:
            result = travel_crew.kickoff(inputs={"user_query": user_query})
            return result.raw
        except Exception as e:
            return f"Error invoking Crew: {str(e)}"
