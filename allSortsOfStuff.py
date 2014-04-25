# clean up later

#github.com/ericmanlol/googlecodejam
def bubble_sort(list):
    for num in range(len(list) - 1, 0, -1):
        for i in range(num):
            if list[i] > list[i + 1]:
                tmplist = list[i]
                list[i] = list[i + 1]
                list[i + 1] = tmplist


def selection_sort(list):
    for fillslot in range(len(list) - 1, 0, 1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if list[location] > list[position_of_max]:
                position_of_max = location

        tmplist = list[fillslot]
        list[fillslot] = list[position_of_max]
        list[position_of_max] = tmplist




if __name__ == "__main__":
    print 'allSortsOfStuff being run directly'
else:
    print 'allSortsOfStuff loaded as module'
