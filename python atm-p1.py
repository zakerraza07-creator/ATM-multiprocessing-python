## Atm system using python Multiprocessing ##

from multiprocessing import Process,Lock,Value

def check_bank_balance(balance,lock):
    with lock:
        print("your bank balance is:",balance.value)

def deposit(balance,lock):

    with lock:
        amount=3000
        balance.value += amount
        print("balance after deposit=",balance.value)



def withdraw(balance,lock):

    with lock:
        amount=4000
        if balance.value>amount:
            balance.value=balance.value-amount
            print("balance after withdraw=",balance.value)

        else:
            print("insufficient balance")

if __name__=="__main__":

    lock=Lock()
    bank_balance=Value('i',7000)

    p1=Process(target=check_bank_balance,args=(bank_balance,lock))
    p2=Process(target=deposit,args=(bank_balance,lock))
    p3=Process(target=withdraw,args=(bank_balance,lock))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("final balance=",bank_balance.value)