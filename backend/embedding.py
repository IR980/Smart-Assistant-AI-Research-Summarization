


import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    if not chunks:
        return []

    embeddings = model.encode(chunks)

    # ✅ FIX: ensure 2D array
    import numpy as np
    embeddings = np.array(embeddings)

    if len(embeddings.shape) == 1:
        embeddings = embeddings.reshape(1, -1)

    return embeddings


def create_faiss_index(embeddings):
    import numpy as np

    if len(embeddings) == 0:
        return None

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index


def search_index(index, query, chunks, k=3):
    import numpy as np

    if index is None or not chunks:
        return []

    query_vec = model.encode([query])

    # ensure correct shape
    query_vec = np.array(query_vec)
    if len(query_vec.shape) == 1:
        query_vec = query_vec.reshape(1, -1)

    distances, indices = index.search(query_vec, k)

    return [chunks[i] for i in indices[0] if i < len(chunks)]
