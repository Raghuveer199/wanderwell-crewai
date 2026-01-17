from google.genai import Client
client = Client(api_key="AIzaSyBZAeOFZfNN1kBeSWzm8JXcIVdn3zmhQH4")
models = client.models.list()
for m in models:
    print(m.name)
