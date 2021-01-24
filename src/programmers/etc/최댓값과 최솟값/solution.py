def solution(s):
    mylist = list(map(int, s.split()))

    mylist.sort()

    answer = str(mylist[0]) + " "+ str(mylist[-1])
    return answer
