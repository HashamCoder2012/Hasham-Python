import numpy as np
data_type=[('name','S15'),('class',int),('height',float)]
student_detail=[('Chris',5,41.5),('Nail',6,52.9),('Chandler',5,40.45),('Pit',5,40.51)]
students=np.array(student_detail,dtype=data_type)
print("Original array:")
print(students)
print("Sort it by height")
print(np.sort(students,order='height'))

