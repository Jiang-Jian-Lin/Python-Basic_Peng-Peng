#定義涵式
#涵式內部的程式碼, 若是沒有做涵式呼叫, 就不會執行
def multiply(n1, n2):
    print(n1*n2)
    return n1*n2   #函式執行完,系統就會自動return(可不寫出來,不帶回傳值)回傳None
#呼叫函式
#multiply(5, 8)
value=multiply(3, 4)+multiply(10, 5) # (3*4)+(10*5)
print(value)
#程式的包裝
def calculate(max):
    sum = 0
    for n in range(1,max+1):
        sum = sum+n
    print(sum)
calculate(2)
calculate(3)
