import os
print("Checking if my_file exists or not....")
if os.path.exists("C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt"):
    os.remove('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt')
else:
    print("The file does not exist")

#os.remove('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt')
os.rmdir('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham ')
