import random

def rohanmulti(x):
    multiple = random.randint(2, 9)
    global list_ro
    list_ro = []

    for i in range(11):
        if i == multiple:
            a = random.randint(x * (i - 1), x * (i + 1))
            if a == x * i:
                v = (random.randint(1, x - 1))
                list_ro.append(a + v)
            elif a == x * (i-1):
                r = (random.randint(1, x - 1))
                list_ro.append(a + r)

            else:
                list_ro.append(a)
        else:
            b = x * i
            list_ro.append(b)

    return list_ro

def Incorrect(n):
    b = -1
    for i in list_ro:
        b += 1
        if (i != n*b):
            print(f"Be conscious about[{i}]. Here is a scam....\nIt should be {n*b}.")
        else:
            continue


if __name__ == "__main__":
    n = int(input("Enter the number to get it's multiplication table: \n"))
    print(rohanmulti(n))
    #This function prints statement if any output of table is wrong.
    Incorrect(n)
