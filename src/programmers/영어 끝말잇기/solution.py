def solution(n, words):

    for idx in range(len(words)):
        if (len(words[idx]) == 1):
            return [idx%n +1, idx//n+1] 
        if(idx != 0 and words[idx][0] != words[idx-1][-1]):
            return [idx%n +1, idx//n+1] 
        for i in range(idx):
            if(words[idx] == words[i]):
                return [idx%n +1, idx//n+1] 

    return [0, 0]
