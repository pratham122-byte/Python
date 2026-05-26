total_cls = 100
attended = int(input("Enter the number of classes attended: "))
def attendance_percentage():
    attendance = (attended / total_cls) * 100
    print("Attendance percentage:", attendance)
    return attendance
def eligibility():
    attendance = attendance_percentage()
    if attendance < 75:
        print("Not eligible for exam")
    else:
        print("Eligible for exam")
eligibility()

