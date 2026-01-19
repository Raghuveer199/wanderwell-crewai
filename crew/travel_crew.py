from crewai import Crew, Task, Process
from agents.intent_classifier_agent import intent_classifier_agent
from agents.destination_inference_agent import destination_inference_agent
from agents.accomodation_agent import accomodation_agent
from agents.transport_agent import transport_agent
from agents.crew_response_agent import crew_response_agent

# Define Tasks for each agent
intent_task = Task(
    description="Interpret overall intent from: {user_query}. Enrich shared context.",
    agent=intent_classifier_agent,
    expected_output="dynamic"
)

experience_task = Task(
    description="Gather experience-related insights for: {user_query} from DuckDB if relevant.",
    agent=destination_inference_agent,
    expected_output="dynamic"
)

stays_task = Task(
    description="Gather stays, rooms, and pricing info for: {user_query} from DuckDB if relevant.",
    agent=accomodation_agent,
    expected_output="dynamic"
)

travels_task = Task(
    description="Gather vehicles, tickets, and travel aggregation info for: {user_query} if relevant.",
    agent=transport_agent,
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
        intent_classifier_agent,
        destination_inference_agent,
        accomodation_agent,
        transport_agent,
        crew_response_agent
    ],
    tasks=[
        intent_task,
        experience_task,
        stays_task,
        travels_task,
        response_task
    ],
    process=Process.sequential,
    verbose=True
)
