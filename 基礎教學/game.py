import random


isGuess = False
answer = random.randint(1, 10)
while isGuess == False:
    temp = input('不訪猜一下小甲魚現在的心裡想的是哪一個數字')
    guess = int(temp)

    if guess == answer:
        print('妳是小甲魚心理的蛔蟲麻?')
        print('亨, 猜中了也沒獎勵 ')
        print('遊戲結束，不完啦^_^')

        isGuess = True
        # break ,可跳出最近的循環語句
        
    else:
       if guess < answer:
           print('小啦~')
       else:
           print('大啦~')
        

 
