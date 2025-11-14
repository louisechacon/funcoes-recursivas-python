def junta(l1, l2):

    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    
    ultimo_l1 = l1[-1]
    ultimo_l2 = l2[-1]
    l3 = []
    if ultimo_l1 > ultimo_l2:
        l3 = [ultimo_l2, ultimo_l1]
    else:
        l3 = [ultimo_l1, ultimo_l2]
    return junta(l1[:-1], l2[:-1]) + l3

x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(junta(x,y))