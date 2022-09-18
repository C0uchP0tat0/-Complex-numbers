def get_result():
    l = list()
    for i in range(1, 1000000):
        j =list(str(i))
        v = list()
        for c in j:
            v.append(int(c))
        k = (sum(v))**2
        n = (3*i)/k
        try:
            if int(n)==n:
                l.append(int(n))
        except ValueError:
            pass
    for i in range(1, 1000):
        if not i in set(l):
            print(i)
            break
        

def main():
    get_result()
    
if __name__ == "__main__":
    main()