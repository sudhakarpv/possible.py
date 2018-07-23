# possible.py
def main():
    pass
    n=input()
    c=[]
    temp=0
    user=list(map(int,input().split()))
    user.sort()
    str_rev=user[::-1]
    for i in user :
        if i==0:
            c.append(i)
        if (len(c)==len(user)):
            temp=1
        else:
            out=str_rev
    if (temp>0):
        print(0)
    else:
        print(''.join(map(str,out)))
if __name__ == '__main__':
    main()
