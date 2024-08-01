def notalwaysaverangemoney(money,people):
    if people>money:
        return 0
    if people==1:
        return 1
    total=0
    for i in range(1,money-people+2):
        total+=notalwaysaverangemoney(money-i,people-1)
    return total

people=int(input())
money=int(input())
print(notalwaysaverangemoney(money,people))