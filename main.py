from orchestrator import orchestrator_agent
import asyncio
# from rich import print

user_query = "Pick top 5 wellness retreat options, structure it to Option + City Name"

# Orchestrator sends the query to TravelCrew via its tool
final_response = orchestrator_agent.kickoff(user_query)

asyncio.sleep(3)

print("\n================================================ FINAL RESPONSE ================================================\n")
print(final_response.messages[-1]['content'])
# print(final_response['messages'][-1])
