hour = int(input("Enter your hour:"))
rate = int(input("Enter your rate:"))

def salary(time , money):
    return time * money


def over_pay(time , money):
    over_time = time - 160
    return over_time * (money * 1.5)


def regular(time , money):
    if time > 160 :
        a = over_pay(time , money)
        b = salary(time , money)
        print("Your regular payment is :" , a+b)
    else :
        c = salary(time , money)
        print("Your regular payment is :" , c)

regular(hour , rate)
