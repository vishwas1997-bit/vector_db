import chromadb

# Create persistent database
client = chromadb.PersistentClient(
    path="./vector_db"
)

# Create collection
collection = client.create_collection(
    name ="my_documents"
)

# Insert documents
collection.add(
    ids=["1","2","3"],
    documents=[
        "Android is a mobile operating system",
        "Kotlin is used for android developer",
        "Python is popular for AI developement"
    ]
)


# Search documents
results = collection.query(
    query_texts=["What is Android?"],
    n_results=2
)

print(results["documents"])
