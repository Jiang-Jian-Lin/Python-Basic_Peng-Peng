#有序列表 List
grades=[12, 60, 15, 70, 90]
grades[-1]= 87  ##把87放到最後一個
grades[0]= 78
grades[1:4] = []  ## Contunute Delete index 1~3 location
grades = grades + [66,77]  ##列表串接 
length = len(grades)  ## 取得列表的長度 len(列表資料)
print(grades[0:4])
print(length)

#巢狀
data = [[3,4,5],[6,7,8]]
print(data)
data[0][0:2] = [5,5,6]  ## [5, 5, 6, 5]
print(data)

##有序不可變動列表 Tuple
data=(3,4,5)
data[0] = 87   ＃＃error, Tuple的資料不可移動
print(data)
