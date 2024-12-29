with open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','w') as file:
   file.write("Hi!I am Penguin and i am 1yr old")
file.close()
count=0
with open('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham file.txt','r') as file:
   data=file.readlines()
   print("Word in this file are....")
   for line in data:
      word=line.split()
      count=count+len(word)
      print(len(word))
      print  (word)
file.close()

