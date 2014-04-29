# clean up later
    

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


def merge_sort(list):
    print "Splitting -> ", list
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[i]:
                list[k] = left_half[i]
                i = i + 1
            else:
                list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            list[k] = right_half[j]
            j = j + 1
            k = k + 1

        print "Merging ->", list

if __name__ == "__main__":
    print 'allSortsOfStuff being run directly'
else:
    print 'allSortsOfStuff loaded as module'
