
# break 會直接離開迴圈。
n =0 
while n < 5:    
    if n == 3:
        break      #強制結束迴圈
    n+= 1
print(n)

#continue 只是跳過迴圈下面的程式，但會繼續下一次的迴圈流程。
n = 0
for x in [0, 1, 2, 3]:
    if x%2 == 0:
        continue   # 強制進行下一圈
    n+=1  
print(n)

#else 簡易範例
sum = 0
for n in range(11):
    sum+=n
else:
    print(sum)
# n = 1
# while n < 5:
#     print("變成n的資料是:", n)
#     n+=1
# else:
#     print(n) 

# for c in "Hello":
#     print("逐一取得字串中的字元", c)
# else:
#     print(c) 