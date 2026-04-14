from endee import Client

client = Client()

# Load notes
with open("data.txt", "r") as f:
    data = f.read()

client.add(data)

print("📚 Notes Search AI Ready!")

while True:
    query = input("\nAsk from notes: ")

    if query.lower() == "exit":
        break

    result = client.query(query)
    print("📖 Answer:", result)
