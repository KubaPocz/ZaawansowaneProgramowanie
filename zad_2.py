def PomnozPrzez2For(Numbers):
    result =[]
    for num in Numbers:
        result.append(num*2)
    print(result)

def PomnozPrzez2List(Numbers):
    print([2*num for num in Numbers])

Numbers=[1,2,3,4,5]

PomnozPrzez2For(Numbers)
PomnozPrzez2List(Numbers)