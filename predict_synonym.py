import pickle
from sklearn.metrics.pairwise import cosine_similarity



first_10=[]

def similar_one_out(words,synonym_of, word_vectors):
    """Accepts a list of words and returns the odd word"""

    avg_vector = word_vectors[synonym_of]
    
    #Iterate over every word and find similarity
    similar_one_out = None
    min_similarity = 0.0 #Very high value
    
    for w in words:  
        try:
            temp=word_vectors[w]
        except:
            continue
            
        sim = cosine_similarity([temp],[avg_vector])

        sim=round(float(sim),2)

        if sim<0.5:
            continue
        
        t=[w,sim]
        
        first_10.append(t)
    
        #print("Similarity btw %s and avg vector is %.2f"%(w,sim))
            
    return first_10