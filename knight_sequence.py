isVowel = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0] 
 
validMoves =[[7,11],        #A
            [8,10,12],      #B
            [5,9,11,13],    #C
            [6,12,14],      #D
            [7,13],         #E
            [2,12,15],      #F
            [3,13,16],      #G
            [0,4,10,14,15,17], #H
            [1,11,16],      #I 
            [2,12,17],      #J
            [1,7,16],       #K
            [0,2,8,17],     #L
            [1,3,5,9],      #M
            [2,4,6,15],     #N
            [3,7,16],       #O
            [5,7,13],       #1
            [6,8, 10, 14],  #2
            [7,9,11]]       #3

       
def dfs(key_indices, remaining_keys, vowelsAllowed):          
    """Apply dfs (recursion) to return valid knight sequence path count"""
     
    sequences = 0      
    if remaining_keys > 0:
        remaining_keys = remaining_keys - 1 
        # Apply dfs to possible key press                    
        for key_index in key_indices: 
            value = 0                   
            if (vowelsAllowed or (not isVowel[key_index])):     
                if remaining_keys:   
                    value = dfs((validMoves[key_index]) , remaining_keys, vowelsAllowed - isVowel[key_index]) 
                else:                    
                    value = 1    
                     
            sequences += value
                            
    return sequences 

if __name__ == '__main__': 
    
    allowedVowels = 2                                                  
    totalKeysInSequence = 10                                           
    
    # First the key identity which makes the rest of the code easier to read.
    keyIdentity = [ {'A':0}, {'B':1}, {'C':2}, {'D':3}, {'E':4}, {'F':5}, {'G':6}, {'H':7}, {'I':8}, {'J':9}, {'K':10}, {'L':11}, {'M':12}, {'N':13}, {'O':14}, {'1':15}, {'2':16}, {'3' :17}]
    
    print ("Total number of valid "+str(totalKeysInSequence)+ " key sequences are: " + str(dfs(range(len(keyIdentity)), totalKeysInSequence, allowedVowels)))
