
import  threading
import  random
import time

def impar():
    x =0
    while x < 10:
        print("1")
        x += 1
        time.sleep(1)
def par():
    y = 0
    while y < 10:
        print("2")
        y += 1
        time.sleep(1)

threading.Thread(target=impar).start()
par()
print(f'-=-'*5)
rand = random.randint(0,10)
if rand %2==0:
    print('FUNÇÃO PAR  VENCEU')
else:
     print('FUNÇÃO IMPAR VENCE')


