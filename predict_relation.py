import pickle
from sklearn.metrics.pairwise import cosine_similarity



first_10=[]


def predict_word(a,b,c,words, word_vectors):
    """ Accepts a triad of words, a,b,c and returns d such that 
    a is to b : c is to d"""
    a,b,c=a.lower(),b.lower(),c.lower()
    
    # similarity |b-a|=|d-c| should be max
    max_similarity=-100
    
    d=None
    
    
    wa,wb,wc = word_vectors[a],word_vectors[b],word_vectors[c]
    
    #to find d s.t similarity(|b-a|,|d-c|) should be max
    
    for w in words:
        if w in [a,b,c]:
            continue
        try:    
            wv= word_vectors[w]
        
        except:
            continue
        
        sim=cosine_similarity([wb-wa],[wv-wc])
        
        sim=round(float(sim),2)
        
        t=[w,sim]
        
        first_10.append(t)
    
            
    return first_10