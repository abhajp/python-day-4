
student_name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

if marks >= 40:
    status = "PASS"
else:
    status = "FAIL"

print("--- Student Result ---")
print("Student Name:", student_name)
print("Marks:", marks)
print("Status:", status)