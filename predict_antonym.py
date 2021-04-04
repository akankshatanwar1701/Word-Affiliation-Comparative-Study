import pickle
from sklearn.metrics.pairwise import cosine_similarity



first_10=[]


def odd_one_out(words,antonym_of, word_vectors):
    """Accepts a list of words and returns the odd word"""
    all_word_vectors=[]
    # Generate all word embeddings for the given list
    
    for w in words:
        try:
            wv=word_vectors[w] 
        except:
            continue
        
        all_word_vectors.append(wv)
    
    avg_vector = word_vectors[antonym_of]
    
    
    #Iterate over every word and find similarity
    odd_one_out = None
    
    
    for w in words:  
        try:
            temp=word_vectors[w]
        except:
            continue
            
        sim = cosine_similarity([temp],[avg_vector])
        
        sim=round(float(sim),2)
        if(sim<=0):
            continue

        t=[w,sim]

        first_10.append(t)
    
        #print("Similarity btw %s and avg vector is %.2f"%(w,sim))
            
    return first_10