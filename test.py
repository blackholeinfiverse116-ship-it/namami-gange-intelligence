import json

with open("DEMO_INTELLIGENCE_PAYLOAD.json") as f:
    data = json.load(f)

for city in data:
    print(city["location"])
    print(city["score"])
    print(city["level"])
    print("------")