
def python_sort(array):
    print("sorting array")
    array.sort()
    return array

def check_is_sorted(l):
    l = l[0]
    return all(a <= b for a, b in zip(l, l[1:]))