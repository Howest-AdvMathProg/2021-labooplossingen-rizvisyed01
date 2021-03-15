def fibo(val):
    fibs = [0, 1]

    for i in range(2, val+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[val]

if __name__ == '__main__':
    print(fibo(80))