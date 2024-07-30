# Ollama is a platform for deploying LLMs
# download Ollama program from the website
# run the Phi 3 Mini LLM on your laptop with the following command: ollama run phi3
# pip install ollama

import pickle # allows you to save data structures and load them back later
# Save the list to a file
#with open('doc_txt.pkl', 'wb') as file:
#    pickle.dump(doc_txt, file)
with open('data/doc_txt.pkl', 'rb') as file:
    doc_txt = pickle.load(file)

paras_list = []
paragraphs = doc_txt[0].split('\n\n')
for p in paragraphs:
    if len(p.strip())>50:  
        p.replace('\n', '')
        paras_list.append(p.strip())

ids_list = list(range(1, len(paras_list) + 1))

# print(paras_list,ids_list)

import ollama
keyword_list = []
for para in paras_list:
    prompt = f"summarize {para} in a maximum of 2 words separated by ,"
    try:
        response = ollama.generate(model="phi3", prompt=prompt)
        summary = response.get("response", "Error: No response")
        keyword_list.append(summary)
        print(summary)
    except Exception as e:
        keyword_list.append(f"Error: {e}")

print(ids_list,paras_list,keyword_list)

# Save the lists to a file
with open('lists.pkl', 'wb') as file:
    pickle.dump((ids_list,paras_list,keyword_list), file)



