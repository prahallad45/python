#1 simple way for replace
str1 = "prahallad"
x=str1.replace('a','o',1)
print(x)

#2 using for loop
str2="prahallad"
result = ''
for i in str2:
        if i == 'a':
                i = 's'
        result += i
print(result)

#3 using function
def slicing(str3):
    result = '' 
    for i in str3:
        if i == 'a':
                i = 's'
        result += i
    print(result)
          
str3 =input("Enter the string:")
slicing(str3)

#4 using class 
class slicing:
    def __init__(self,x):
        self.x=x

    def show(self):
        print(self.x.replace('a','o',1)) #it will print from start to 9 index
pg=slicing("salman khan")
pg.show()


