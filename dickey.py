mydic={'a':'apple','b':'banana','c':'cherry','d':'date'}
print("dictionary:",mydic)
key=input("enter the key to be accessed:")
if key in mydic.keys():
    print("\n key exists in the dictionary")
    print("key:",key," and value :",mydic[key])
else:
    print("\n key does not exist in the dictionary")
