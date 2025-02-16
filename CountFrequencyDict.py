test_dict={'Codingal':2,'is':2,'best':2,'for':2,'Coding':3,}
print("The original dictionary:"+str(test_dict))
two=2
res=0
for key in test_dict:
    if test_dict[key]==two:
        res=res+1
print("Frequency of two is:"+str(res))