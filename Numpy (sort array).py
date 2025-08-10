import numpy as np
data_type=[('name','S15'),('class',int),('height',float)]
student_detail=[('James',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.11)]
students=np.array(student_detail,dtype=data_type)
print("Original array:")
print(students)
print("Sort it by height")
print(np.sort(students,order='height'))


import numpy as np
arr=np.array([1,2,4,3,5,76])
print(arr)
print(type(arr))


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])
print(arr.dtype)

import numpy as np
arr=np.array([1,2,3,4],dtype='S')
print(arr)
print(arr.dtype)