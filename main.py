from orchestrator import orchestrator_agent
import asyncio
# from rich import print

user_query = "Show me top 5 planes from Delhi to Hyderabad"

# Orchestrator sends the query to TravelCrew via its tool
final_response = orchestrator_agent.kickoff(user_query)

print("\n================================================ FINAL RESPONSE ================================================\n")
print(final_response.messages[-1]['content'])
# print(final_response['messages'][-1])
