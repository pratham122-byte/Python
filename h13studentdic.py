students = {101: "Pratham",102: "aditya",103: "vinay"}
key = int(input("Enter student number to search: "))
if key in students:
    print(f"Student {key} is found {students[key]}")
else:
    print(f"Student {key} not found.")
