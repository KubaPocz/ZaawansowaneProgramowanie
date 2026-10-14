def CzyParzysta(liczba:int) ->bool:
    if liczba % 2 == 0:
        return True
    else:
        return False
liczba = 6
if CzyParzysta(liczba):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")