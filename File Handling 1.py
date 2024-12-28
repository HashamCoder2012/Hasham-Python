file=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','r')
print(file.read())
file.close()

file=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','r')
print("\n Read in parts \n")
print(file.read(8))
print(file.readline())
file.close()

file=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','a')
file.write("Hi! I am Penguin and I am 1yr old.")
file.close()

file_write=open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file123.txt','w')
file_write.write("\n File in write mode....")
file_write.write("Hi!I am penguin.I am 1yr old.")
file_write.close()
