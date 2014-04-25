# clean up later


def bubbleSort(list):
    for num in range(len(list) - 1, 0, -1):
        for i in range(num):
            if list[i] > list[i + 1]:
                tmplist = list[i]
                list[i] = list[i + 1]
                list[i + 1] = tmplist

if __name__ == "__main__":
    print 'allSortsOfStuff being run directly'
else:
    print 'allSortsOfStuff loaded as module'
