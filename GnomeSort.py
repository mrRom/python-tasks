def gnomeSort(llist):
    size = len(llist)
    i = 1
    while i < size:
        if (llist[i - 1] <= llist[i]):
            i += 1
        else:
            tmp = llist[i]
            llist[i] = llist[i - 1]
            llist[i - 1] = tmp
            i-= 1
            if (i == 0):
                i = 1
    return llist

if __name__ == '__main__':
    lists = [2, 8, 6, 1, 32, 7, 51, 44]
    print lists
    newlists = gnomeSort(lists)
    print newlists 