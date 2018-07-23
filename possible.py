# possible.py
def main():
    pass
    n=input()
    user=input().split()
    k=list(user)
    k.sort()
    q=k[::-1]
    l=''.join(q)
    print(l)

if __name__ == '__main__':
    main()
