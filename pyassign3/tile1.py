#!/usr/bin/env python
# coding: utf-8

# In[25]:


m = int(input("墙长m = "))
n = int(input("墙宽n = "))
a = int(input("砖长a = "))
b = int(input("砖宽b = "))

qiang = [0]*m*n#初始设定一面长为m宽为n的待铺墙面
ans = []#用来记录铺法

def check(i,j,a,b):
    '''检查从(i,j)号砖开始，能否横着铺长a宽b的瓷砖，其中i表示从上到下横坐标，j表示从左到右纵坐标，(0,0)表示第一块砖的坐标'''
    if i+b>n or j+a>m: #超出墙的边界
        return False
    else:
        for x in range(i,i+b):
            for y in range(j,j+a):
                if qiang[x*m+y] == 1:#判断从(i,j)开始铺砖(a,b)是否有已铺过的地方
                    return False
    return True

def fill(nowans,i,j,a,b,val):
    '''从(i,j)号砖开始铺/拆砖(a,b),val为1时铺砖，val为0时拆砖'''
    tmp = []#用于记录可以铺的一块砖对应位置的墙面砖号
    for x in range(i,i+b):
        for y in range(j,j+a):
            qiang[x*m+y] = val
            tmp.append(x*m+y)
    if val == 1:
        nowans.append(tmp)#可以将铺好的砖的信息加入答案中（铺砖）
    else:
        nowans.remove(tmp)#将铺好的砖的信息从答案中移除（拆砖）

def puzhuan(nowans,i,j):
    '''从(i,j)开始铺砖'''
    if i == n-1 and j == m:
        #判断是否已铺完全部的墙（已铺到最后一块砖），若一条完整的铺法已记录完毕，copy此铺法到最终答案中，并可以开始重置nowans开始寻找下一种完整的铺法
        print(nowans)
        ans.append(nowans.copy)
        return
    
    elif j == m:
        #判断是否已讨论到一行最后一个砖的下一个砖，即是否已铺完一整行的砖，是否需要从新的一行的第一块砖开始铺
        puzhuan(nowans,i+1,0)
        return
    
    if qiang[i*m+j] == 1:
        #判断(i,j)是否已铺了砖，若已铺，则讨论(i,j+1)
        puzhuan(nowans,i,j+1)
        return
    
    if check(i,j,a,b):
        #判断是否能从(i,j)开始横铺
        fill(nowans,i,j,a,b,1)#如果能，将每个变为1，表示铺砖并记录
        puzhuan(nowans,i,j+a)#递归沿着这次铺好的继续往下铺（直至全部铺完）
        fill(nowans,i,j,a,b,0)#找到(i,j)开始横铺对应的所有铺法后，将它们都变为0，表示拆砖，至此横铺方法记录完毕，拆砖以便讨论从(i,j)开始竖铺
        
    if a!=b and check(i,j,b,a):
        #判断是否能从(i,j)竖铺，若为正方形砖（a = b）直接跳过该讨论
        fill(nowans,i,j,b,a,1)#如果能，铺砖并记录
        puzhuan(nowans,i,j+b)#递归沿着这次铺好的继续往下铺
        fill(nowans,i,j,b,a,0)#找到竖(i,j)开始竖铺对应的所有铺法后，拆砖
    return

puzhuan([],0,0)
print(ans)
        
    
        
    
    
        
    
    
    


# In[ ]:





# In[ ]:




