def WyswietlParzyste(Liczby):
    for liczba in Liczby:
        if(liczba%2==0):
            print(liczba)

Liczby=range(10)
WyswietlParzyste(Liczby)