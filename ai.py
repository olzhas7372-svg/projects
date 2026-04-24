from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def ai_search(query, ads):
    texts = [a["title"] + " " + a["description"] for a in ads]

    q = model.encode([query])
    t = model.encode(texts)

    scores = (q @ t.T)[0]

    return [x for _, x in sorted(zip(scores, ads), reverse=True)]
