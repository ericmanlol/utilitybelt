# clean up later

# github.com/ericmanlol/googlecodejam


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


def insertion_sort(list):
    """O(n^2)"""
    for index in range(1, len(list)):
        current_value = list[index]
        position = index

        while position > 0 and list[position - 1] > current_value:
            list[position] = list[position - 1]
            position = position - 1

        list[position] = current_value


def shell_sort(list):
    # double forward slash //divides and rounds towards minus infinity
    sublistcount = len(list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(list, startposition, sublistcount)

        print("after increments of size", sublistcount,
              "The List is", list)

    sublistcount = sublistcount // 2


def gap_insertion_sort(list, start, gap):
    for i in range(start + gap, len(list), gap):

        current_value = list[i]
        position = i

        while position >= gap and list[position - gap] > current_value:
            list[position] = list[position - gap]
            position = position - gap

        list[position] = current_value


if __name__ == "__main__":
    print 'allSortsOfStuff being run directly'
else:
    print 'allSortsOfStuff loaded as module'
