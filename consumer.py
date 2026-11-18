from time import sleep


def zmien_status(id_pracy, nowy_status):
    with open("data.txt", "r", encoding="utf-8") as file:
        linie = file.readlines()

    with open("data.txt", "w", encoding="utf-8") as file:
        for linia in linie:
            id, status = linia.strip().split("; ")
            if id == id_pracy:
                status = nowy_status
            file.write(f"{id}; {status}\n")


while True:
    id_pracy = None

    with open("data.txt", "r", encoding="utf-8") as file:
        for linia in file:
            id, status = linia.strip().split("; ")
            if status == "pending":
                id_pracy = id
                break

    if id_pracy is None:
        print("Brak pracy, czekam 5s...")
        sleep(5)
        continue

    zmien_status(id_pracy, "in_progress")
    print(f"Wykonuję pracę {id_pracy}")
    sleep(5)
    zmien_status(id_pracy, "done")
    print(f"Zakończono pracę {id_pracy}")