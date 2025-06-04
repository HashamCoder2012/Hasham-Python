import matplotlib.pyplot as plt
student_names=["John","Micheal","Mitchell","Ronaldo","Virat","Baber"]
exam_marks=[81,46,66,22,99,67]
marks_perc={}
for x in exam_marks:
    res=(x/50)*100
    marks_perc.append(res)
print(marks_perc)

def marks_line_chart():
    plt.plot(student_names,exam_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("student_names")
    plt.ylabel("exam_marks")
    plt.show()
marks_line_chart()

def percentage_bar_chart():
    plt.bar(student_names,marks_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Student Percentage")
    plt.show()
percentage_bar_chart()

