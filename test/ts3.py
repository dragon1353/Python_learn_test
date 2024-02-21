


# 第三周練習
# x1=int(input())
# x2=int(input())
# y=int(input())
# if y >= x1:
    # x2 += x1
    # x1 = 0
# else:
    # x2 += y
    # x1 -= y
# print(x1, x2)


x=1000-int(input())
x500=x%500
x100=x500%100
x50=x100%50
x10=x50%10
x5=x10%5
x1=x5/1
strsum=""

strx500 = (str(500) + ", " + str(x//500) if x//500!=0 else "")
strsum += strx500

strx100 = (str(100) + ", " + str(x500//100) if x500//100!=0 else "")
if strsum != "" and strx100 != "":
    strsum += ("; " + strx100)
else:
    strsum += strx100
    
strx50 = (str(50) + ", " + str(x100//50) if x100//50!=0 else "")
if strsum != "" and strx50 != "":
    strsum += ("; " + strx50)
else:
    strsum += strx50
    
strx10 = (str(10) + ", " + str(x50//10) if x50//10!=0 else "")
if strsum != "" and strx10 != "":
    strsum += ("; " + strx10)
else:
    strsum += strx10
    
strx5 = (str(5) + ", " + str(x10//5) if x10//5!=0 else "")
if strsum != "" and strx5 != "":
    strsum += ("; " + strx5)
else:
    strsum += strx5
    
strx1 = (str(1) + ", " + str(x5//1) if x5//1!=0 else "")  
if strsum != "" and strx1 != "":
    strsum += ("; " + strx1)
else:
    strsum += strx1
    
    
print(strsum)

