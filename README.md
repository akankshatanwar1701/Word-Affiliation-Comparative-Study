# Word-Affiliation-Comparative-Study

#### A Comparative Study to Compare Performance of Static Word Embeddings   

Given an extensive auxiliary text file (could be web-scrapped from any website) which has been cleaned using regular expressions, we aim to   
build an end-to-end framework, with the input from the user being a word or a set of words (word analogy relation task) and our goal to extract relevant 
words from the auxiliary text file directly correspond to the input, i.e., words which are either synonyms or antonyms of the input or fit best  
into the word analogy relation. Word analogy task can be explained by,   
‘x is to y what w is to ________’. An example would be ‘red is to apple what yellow is to banana’.  


![alt text](https://github.com/akankshatanwar1701/Word-Affiliation-Comparative-Study/blob/main/assets/word2vec.png)    

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Word Embeddings Being Tested
- [x] **word2vec**     
- [x] **GloVe**    
- [x] **fastText**    
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
   
| Programming Language  | Python |  
| Operating System | Windows 10 |
| Library Packages | pickle, flask, numpy, pandas, gensim, sklearn.metrics.pairwise, re, nltk |  
| Interface Design | Web Application hosted locally |  
| Web App Framework | Flask |
| Datasets/Models Used | GoogleNews-vectors-negative300.bin, glove.6B.100d.txt.word2vec, wiki-news-300d-1M.vec |
| Word Embeddings | Word2Vec, GloVe, fastText |

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## WorkFlow:

The whole project can be accessed in terms of a web application. The web application requires the user to upload a **web scrapped file in .csv format.**  
The backend python code cleans the csv file provided by the user and stores the words thereby left in a list format. The user is asked to either  
provide a word for calculation of synonyms, antonyms of word analogy from the list of words thus received above. A list is then output everytime containing  
the desired results.  
  

![alt text](https://github.com/Anima108/My-Codes/blob/master/src/MVT%20Diagram%20(2).png "MVT")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Model View Template Diagram:  

![alt text](https://github.com/akankshatanwar1701/Word-Affiliation-Comparative-Study/blob/main/assets/MVT.png)  
  

----------------------------------------------------------------------

