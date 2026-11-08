from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
    

model  = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love Android development",
    # "I enjoy building mobile applications",
    "The weather is cold today",
]

embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print(f"Sentence: {sentence}")
    print(f"Embedding: {embedding}\n")
    

similarity = cosine_similarity([embeddings[0], embeddings[1]])
print(f"Cosine similarity between '{sentences[0]}' and '{sentences[1]}': {similarity[0][1]}")