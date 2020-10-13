# Plotting time complexity of three sorting algorithms using matplotlib
# @author Scott! Williams

import sys
import random
import time
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

swapCount = 0
comparisonCount = 0

# Randomly generate and populate lists of digits to a specified size
def generate(s: int) -> list:
    array = []
    for i in range(s):
        array.append(random.randrange(0,10000))
    return array

# Function to perform swap and track swap count
def swap(list, i, j):
    global swapCount
    swapCount += 1
    if i != j:
        list[i], list[j] = list[j], list[i]

# Bubble Sort
def bubble(list: list) -> list:
    global comparisonCount
    # Traverse list
    for i in range(len(list)-1):
        # Traverse to len(list)-i-1
        for j in range(0, len(list)-i-1):
            # If found element is larger make the swap with element + 1
            comparisonCount += 1
            if list[j] > list[j+1]:
                #list[j], list[j+1] = list[j+1], list[j]
                swap(list, j, j+1)
    # Return the sorted list
    return list

# Selection Sort
def selection(list: list) -> list:
    global comparisonCount
    # Traverse list
    for i in range(len(list)):
        # Find minimim element
        min = i
        for j in range(i+1, len(list)):
            comparisonCount += 1
            if list[min] > list[j]:
                min = j
        # Swap found min with first element
        #list[i], list[min] = list[min], list[i]
        swap(list, i, min)
    # Return sorted list
    return list

# Insertion Sort
def insertion(list: list) -> list:
    global comparisonCount
    # Traverse list
    for i in range(1, len(list)):
        key = list[i]
        j = i -1
        # Move elements greater than the key ahead of the key
        while j >= 0 and key < list[j]:
            comparisonCount += 1
            #list[j+1] = list[j]
            swap(list, j+1, j)
            j -= 1
        list[j+1] = key
    # Return the sorted list
    return list


# Driver code
def main():
    global swapCount
    global comparisonCount

    # Prompt user for list size
    genValue = int(input('Size of list to sort > '))

    # Generate lists of the same size for each algorithm to sort
    list0 = generate(genValue)
    list1 = generate(genValue)
    list2 = generate(genValue)
    
    '''
    list0.sort()
    list1.sort()
    list2.sort()
    list0.reverse()
    list1.reverse()
    list2.reverse()
    '''

    # Bubble sort
    print('bubble sort')
    t0 = time.time()
    bubble(list0)
    t1 = time.time()

    # Print values to console for review
    print('comparisons: ' + str(comparisonCount))
    print('swaps: ' + str(swapCount))
    print('time: ' + str(t1-t0))
    print()
    # Store values and reset global variables
    bubbleSwaps, bubbleComps = swapCount, comparisonCount
    bubbleTime = t1 - t0
    swapCount, comparisonCount = 0, 0

    # Selection sort
    print('selection sort')
    t0 = time.time()
    selection(list1)
    t1 = time.time()

    # Print values to console for review
    print('comparisons: ' + str(comparisonCount))
    print('swaps: ' + str(swapCount))
    print('time: ' + str(t1-t0))
    print()
    # Store values and reset global variables
    selectionSwaps, selectionComps = swapCount, comparisonCount
    selectionTime = t1 - t0
    swapCount, comparisonCount = 0, 0

    # Insertion sort
    print('insertion sort')
    t0 = time.time()
    insertion(list2)
    t1 = time.time()

    # Print values to console for review
    print('comparisons: ' + str(comparisonCount))
    print('swaps: ' + str(swapCount))
    print('time: ' + str(t1-t0))
    print()
    # Store values
    compSwaps, compComps = swapCount, comparisonCount
    compTime = t1 - t0

    # Define values for plotting
    names = ['Bubble', 'Selection', 'Insertion']
    swapValues = [bubbleSwaps, selectionSwaps, compSwaps]
    compValues = [bubbleComps, selectionComps, compComps]
    timeValues = [bubbleTime, selectionTime, compTime]

    # Set size
    plt.figure(figsize=(15, 5))

    # Swap count subplot
    plt.subplot(131)
    plt.ylabel('Swaps')
    plt.bar(names, swapValues)

    # Comparison count subplot
    plt.subplot(132)
    plt.ylabel('Comparisons')
    plt.bar(names, compValues)

    # Time plot
    plt.subplot(133)
    plt.ylabel('Time (Seconds)')
    plt.bar(names, timeValues)

    # Format and display figure
    plt.suptitle('Sorting ' + str(genValue) + ' Values')
    plt.show()



if __name__ == "__main__":
    main()
