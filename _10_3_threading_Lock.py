import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            donation = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()
            self.balance += donation
            print(f'Пополнение: {donation}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            withdraw = random.randint(50, 500)
            print(f'Запрос на {withdraw}')
            if withdraw <= self.balance:
                self.balance -= withdraw
                print(f'Снятие: {withdraw}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


