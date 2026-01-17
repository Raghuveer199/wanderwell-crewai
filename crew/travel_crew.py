from crewai import Crew, Task, Process
from agents.intent_planner_agent import intent_planner_agent
from agents.experience_agent import experience_agent
from agents.stays_agent import stays_agent
from agents.travels_agent import travels_agent
from agents.crew_response_agent import crew_response_agent

# Define Tasks for each agent
intent_task = Task(
    description="Interpret overall intent from: {user_query}. Enrich shared context.",
    agent=intent_planner_agent,
    expected_output="dynamic"
)

experience_task = Task(
    description="Gather experience-related insights for: {user_query} from DuckDB if relevant.",
    agent=experience_agent,
    expected_output="dynamic"
)

stays_task = Task(
    description="Gather stays, rooms, and pricing info for: {user_query} from DuckDB if relevant.",
    agent=stays_agent,
    expected_output="dynamic"
)

travels_task = Task(
    description="Gather vehicles, tickets, and travel aggregation info for: {user_query} if relevant.",
    agent=travels_agent,
    expected_output="dynamic"
)

response_task = Task(
    description="Consolidate all agent outputs for: {user_query} into a final user-facing reply.",
    agent=crew_response_agent,
    expected_output="final user facing response"
)

# Create the TravelCrew
travel_crew = Crew(
    agents=[
        intent_planner_agent,
        experience_agent,
        stays_agent,
        travels_agent,
        crew_response_agent
    ],
    tasks=[
        intent_task,
        experience_task,
        stays_task,
        travels_task,
        response_task
    ],
    process=Process.sequential,  # Conditional execution: each agent decides if it should run
    verbose=True
)
