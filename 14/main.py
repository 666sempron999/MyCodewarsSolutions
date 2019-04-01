

def find_nb(m):
    totalSumm = 0
    it = 1
    while(totalSumm < m):
        totalSumm += it ** 3
        it += 1
        
    print(m)
    print(totalSumm)
    print(it)

    if totalSumm == m:
        return it - 1
    else:
        return -1

def main():
    it = find_nb(24723578342962)
    print(it)

if __name__ == '__main__':
    main()