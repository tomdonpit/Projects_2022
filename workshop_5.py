import random

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
""" random.shuffle(my_list)
y = my_list.pop()
print(y) """


def guess_linear_search(tries, start, stop):
    """Linear search"""
    guess = random.randrange(start, stop)
    print("Target number is: ", guess)
    index = 0
    for x in my_list:
        print("Current guess is: ", x)
        if x == guess:
            print("Found at index", index)
            return x
        index += 1
        tries -= 1
        if tries == 0:
            print("No more tries left")
            return
    print("Target is not in the list")
    return -1

guess_linear_search(0, 0, 10)