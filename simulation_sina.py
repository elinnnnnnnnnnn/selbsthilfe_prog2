from subaccounts import SavingAccount
from subaccounts import YouthAccount
import time
from datetime import datetime

def apply_interest(account, last_time):
    now = datetime.now()                                        # aktuelle Computerzeit
    months_passed = int((now-last_time).total_seconds()/10)     # berechnet vergangene sekunden
                                                                # Zeitdifferenz in Sekunden durch 10 = Anzahl Monate --> int: voller Monat

    for i in range(months_passed):                              # Loop für Anzahl vergangener Monate
        account.balance *= (1 + account.interest_rate)          # Zinsen werden auf den Kontostand gerechnet
                                                                # Bsp. 1000 * (1 + 0.02) = 1020
    return now


# -----------------------
# Simulation
# -----------------------
print("Simulation started")

konto = YouthAccount("Y001", 20)

last_time = datetime.now()                                      # aktueller Zeitpunkt wird gespeichert
                                                                # wie viel Zeit vergeht effektiv -> umgerechnet in simulierte Monate
print(konto.status())
print(konto.deposit(1000))

time.sleep(10)                                                  # Programm wartet 10 Sekunden
last_time = apply_interest(konto, last_time)                    # Funktionsaufruf: Welches Konto, alte gespeicherte Zeitpunkt
print("After 1 simulated month:")
print(konto.get_balance())

time.sleep(30)
last_time = apply_interest(konto, last_time)
print("After 3 more simulated months:")
print(konto.get_balance())

print(konto.deposit(500))

time.sleep(20)
last_time = apply_interest(konto, last_time)
print("After 2 more simulated months:")
print(konto.get_balance())

print(konto.withdraw(300))

time.sleep(10)
last_time = apply_interest(konto, last_time)
print("Final balance:")
print(konto.get_balance())
