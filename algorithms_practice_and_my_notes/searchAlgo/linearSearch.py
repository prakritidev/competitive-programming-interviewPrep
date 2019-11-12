'''
Linear search is a linerar algo(statine the obvious). We go to each element and check if it's same as the query input or not.

Time complexity if this algo is O(n), because we use a for loop and check each element, if n are number of element then loop will run n time.

TADA! simple shit.

Q: given an array or list find the given element.
A: Apply a for loop over the array and compare the elements to the input.

'''
import time
start_time = time.time()

# Remove the print statements and other fancy stuff, you can reduce the execution time.


def linear_search(input_array, query_input):
    output = []
    if (len(input_array) == 0):
        return "Oh common! do you really think that I'm dumb? "
    for i in range(len(input_array)-1):
        if (input_array[i] == query_input):
            result_query = "Found item @ index " + str(i)
            output.append(result_query)
    return output


if __name__ == "__main__":
    query_input = 8
    input_array = [4, 5, 6, 8, 7, 8, 6, 5, 3, 2, 2, 1, 1, 3, 5, 6, 8, 8, 8, 8, 7, 6, 6, 5, 4, 3, 3, 2, 3, 5, 6, 7,
                   8, 9, 0, 8, 3, 2, 2, 1, 2, 2, 3, 4, 5, 67, 6, 5432, 12, 3456, 78, 765, 432, 12, 3456, 7, 654, 32, 345, 67, 87]
    # input_array = []
    result = linear_search(input_array, query_input)
    print(result)
    print("Execution time : --- %s milliseconds ---" %
          (time.time() - start_time))
