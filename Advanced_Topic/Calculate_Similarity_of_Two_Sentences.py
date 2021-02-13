import pandas as pd
import numpy as np
import string

exclude = set(string.punctuation)

def sentence_cosine_similarity(n):
    """
    This function calcuate the cosine similarity of input sentence. The argument is the number of 
    input sentences.
    """
    sentences = []
    for i in range(n):
        line = input("Please enter the #{} sentence: ".format(i+1))
        sentences.append(''.join([ch for ch in line.strip().lower() if ch not in exclude]).split())
    
    sentences_word_count=[]
    for sen in sentences:
        word_cnt = {}
        for word in sen:
            if word in word_cnt:
                word_cnt[word]+=1
            else:
                word_cnt[word] = 1
        sentences_word_count.append(word_cnt)
    
    print (sentences_word_count)
    
    sentences_count_vectorized = pd.DataFrame(sentences_word_count)
    
    sentences_count_vectorized = sentences_count_vectorized.fillna(0)
    print (sentences_count_vectorized)
    
    sentences_count_vectorized_array = sentences_count_vectorized.values  
    
    results = dict()
    
    for i in range(sentences_count_vectorized_array.shape[0]-1):
        array_1 = sentences_count_vectorized_array[i,]
        array_2 = sentences_count_vectorized_array[i+1,]
        
        temp = round(np.dot(array_1,array_2)/np.sqrt(np.dot(array_1,array_1))/np.
                 sqrt(np.dot(array_2,array_2)),3)
        
        print("The cosine similarity of sentence #{} and sentence #{} is: ".format(i+1,i+2),temp)
        
        results["Sentence #{} and Sentence #{}".format(i+1,i+2)] = temp
    
    return results

if __name__ == "__main__":
  
    cosine_similarity = sentence_cosine_similarity(3)
    print(cosine_similarity)