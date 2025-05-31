import matplotlib.pyplot as plt
student_names=["sanjay","Rafay","Arham","Wasim","Hassan","Shadab","Shoib","Hafeez"]
students_marks=[35,50,20,45,25,40,25,30]
marks_perc=[]
for x in students_marks:
    res=(x/50)*100
    marks_perc.append(res)
print(marks_perc)

def marks_line_chart():
    plt.plot(student_names,students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("student_names")
    plt.ylabel("students_marks")
    plt.show()
marks_line_chart()

def percentage_bar_chart():
    plt.bar(student_names,marks_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Student Percentage")
    plt.show()
percentage_bar_chart()

