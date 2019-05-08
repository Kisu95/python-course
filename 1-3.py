def lowest(array):
    low = min(array)
    arrIndex = array.index(min(array))
    for i in range(len(array)):
        if array[i] == low and i != arrIndex:
            print("Another lowest element index is: " + str(i))
    return low, arrIndex

while True:
    try:
        numbers = [float(x) for x in input("Give any amount of numbers separated by a space: ").split()]
        isinstance(numbers, float)
        assert(len(numbers) > 0)
        break
    except ValueError:
        print("That was no valid number!")
    except AssertionError:
         print("You should enter at least 1 number.")

print(lowest(numbers))
#comment