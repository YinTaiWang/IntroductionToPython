def index_of_min(l, start_index):
    for i in range(start_index, len(l)):
        # print(i)
        if l[i] < l[start_index]:
            start_index = i
    return start_index

def selection_sort(l):
    for i in range(0, len(l)):
        min_index = index_of_min(l, i)
        # print(min_index)
        l[i], l[min_index] = l[min_index], l[i] # exchange the sort
    return l

# l = [16, 5, 10, 17, 18, 9]
# print(selection_sort(l))