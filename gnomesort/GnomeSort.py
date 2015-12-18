def gnome_sort(datalist):
    size = len(datalist)
    i = 1
    while i < size:
        if (datalist[i - 1] <= datalist[i]):
            i += 1
        else:
            tmp = datalist[i]
            datalist[i] = datalist[i - 1]
            datalist[i - 1] = tmp
            i-= 1
            if (i == 0):
                i = 1
    return datalist

if __name__ == '__main__':
    datalist = [2, 8, 6, 1, 32, 7, 51, 44]
    print datalist
    newdatalist = gnome_sort(datalist)
    print newdatalist