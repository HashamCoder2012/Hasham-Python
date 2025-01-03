file=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','r')
print(file.read())
file.close()

file=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','w')
print("\n Read in parts \n")
print(file.read(8))
print(file.readline())
file.close()

file=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','a')
file.write("Hi I am hasham and i am 12 yr old.")
file.close()

file_write=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file123.txt','w')
file_write.write("\n File in write mode....")
file_write.write("Hi I am Hasham and i am 12 yr old.")
file_write.close()
