hour = int(input("Enter your hour:"))
rate = int(input("Enter your rate:"))

def salary(time , money):
    return time * money


def over_pay(time , money):
    over_time = (time - 160)
    money_test = (money * 1.5)
    return over_time * money_test


def regular(time , money):
    t = 160
    b = salary(t , money)
    print("Your salary payment is :" ,b)
    if time > 160 :
        a = over_pay(time , money)
        print("your overpayment is :" , a)
    else :
        c = salary(time , money)
        print("Your regular payment is :" , c)
regular(hour , rate)
