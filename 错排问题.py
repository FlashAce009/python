def derangement(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return (num-1)*(derangement(num-1)+derangement(num-2))
num=int(input())
print(derangement(num))