import pickle
import chromadb #0.5.4
import ollama

# Load the lists from the file
with open('lists.pkl', 'rb') as file:
    ids_list,paras_list,keyword_list = pickle.load(file)

# Print the lists to verify they were loaded correctly
# print(ids_list) 
# print(paras_list)
# print(keyword_list)

str_list = [str(i) for i in ids_list]
dict_list = [{"keywords": s} for s in keyword_list]

db = chromadb.Client()

collection_name = "psf"
collection = db.get_or_create_collection(name=collection_name, 
                embedding_function=chromadb.utils.embedding_functions.DefaultEmbeddingFunction())
collection.add(documents=paras_list, ids=str_list, metadatas=dict_list, images=None, embeddings=None)
#collection.peek(2)

query = "What is borrowing in April?"
res_db = collection.query(query_texts=[query],n_results=2)["documents"][0]
context = ' '.join(res_db).replace("\n", " ")
#print(context) 

res = ollama.chat(model="phi3",
                  messages=[{"role":"system","content":"Give the most accurate answer using your knowledge and the following information: \n"+context},
                            {"role":"user", "content":query}])
print(res["message"]["content"])