#내풀이
def solution(id_list, report, k):
    L = []
    answer = []
    panswer = {i:0 for i in id_list}
    Dic = {i:[] for i in id_list}

    for i in report:
        a,b = i.split()
        if a not in Dic[b]:
            Dic[b].append(a)
    for i in Dic:
        if len(Dic[i]) >= k:
            L.append(i)
    for i in L:
        for j in Dic[i]:
            panswer[j] += 1
    for i in panswer:
        answer.append(panswer[i])


    return answer
    
#다른사람풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
