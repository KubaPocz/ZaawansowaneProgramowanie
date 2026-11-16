import uuid
with open("data.txt", "a", encoding="utf-8",) as file:
    file.writelines(f"{uuid.uuid1()}; pending\n")