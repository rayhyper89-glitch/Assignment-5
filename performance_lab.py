"""
COMPSV Assignment 5: Performance Lab
Solutions, tests, and complexity analyses for all five problems.
"""


# Problem 1: Find Most Frequent Element
def most_frequent(numbers):
    """Return the most frequent value, or None for an empty list."""
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(counts, key=counts.get)


"""
Performance Analysis - Problem 1

Best-case time: O(n), because every element must be counted.
Worst-case time: O(n) expected, assuming normal dictionary performance.
Average-case time: O(n), because each element is processed once.
Space complexity: O(k), where k is the number of unique elements.

I chose a dictionary because it efficiently counts occurrences without
repeatedly scanning the list. The algorithm is already asymptotically
optimal because every element must be examined. A Counter could simplify
the code, but it would have similar performance. The trade-off is that
the dictionary requires additional memory.
"""


# Problem 2: Remove Duplicates While Preserving Order
def remove_duplicates(nums):
    """Return unique elements in their original order."""
    seen = set()
    result = []

    for value in nums:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


"""
Performance Analysis - Problem 2

Best-case time: O(n), because every element must be checked.
Worst-case time: O(n) expected, assuming normal set performance.
Average-case time: O(n).
Space complexity: O(n), because the set and result list can grow
proportionally to the input size.

I chose a set for fast membership checks and a list to preserve order.
The algorithm is already optimal in expected time because every element
must be inspected. It could use less memory only with trade-offs, such
as modifying the input or using a slower approach. This solution requires
elements to be hashable.
"""


# Problem 3: Find Pairs That Sum to a Target
def find_pairs(nums, target):
    """Return pairs that sum to target, assuming unique input values."""
    seen = set()
    pairs = []

    for number in nums:
        complement = target - number

        if complement in seen:
            pairs.append((complement, number))

        seen.add(number)

    return pairs


"""
Performance Analysis - Problem 3

Best-case time: O(n) expected.
Worst-case time: O(n) expected under normal hash-set performance.
Average-case time: O(n) expected.
Space complexity: O(n) for the set and output list.

I chose a set because it allows quick lookups for each number's complement.
This avoids checking every possible pair with nested loops, which would
take O(n^2) time. If only one pair were needed, the function could return
as soon as it found one. Sorting could reduce auxiliary memory in some
implementations, but it would take O(n log n) time and change the input
if sorted in place. The set-based approach uses extra memory for speed.
"""


# Problem 4: Simulate Dynamic List Resizing
def add_n_items(n):
    """Simulate appending n items to an array that doubles in capacity."""
    if n < 0:
        raise ValueError("n must be non-negative")

    capacity = 2
    storage = [None] * capacity
    size = 0

    for value in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            new_storage = [None] * new_capacity

            for index in range(size):
                new_storage[index] = storage[index]

            print(
                f"Resizing from {capacity} to {new_capacity}; "
                f"copied {size} items"
            )

            storage = new_storage
            capacity = new_capacity

        storage[size] = value
        size += 1

    return storage[:size]


"""
Performance Analysis - Problem 4

Best-case total time: O(n) for n appends.
Worst-case time for one append: O(n), when resizing copies existing items.
Average/amortized time per append: O(1).
Total amortized time for n appends: O(n).
Space complexity: O(n).

I chose a doubling strategy because increasing capacity geometrically
reduces how often elements must be copied. Although an individual append
can take O(n) time during a resize, the total copying across all appends
is O(n). Therefore, the amortized cost per append is O(1).

The approach could reduce unused capacity by using a smaller growth
factor, but that would cause more frequent resizing. Doubling offers
good performance at the cost of sometimes allocating unused memory.
"""


# Problem 5: Running Totals - Original Version
def running_total_naive(nums):
    """Calculate each prefix sum by summing the prefix again."""
    totals = []

    for end in range(len(nums)):
        totals.append(sum(nums[:end + 1]))

    return totals


# Optimized Version
def running_total(nums):
    """Calculate running totals in one pass."""
    totals = []
    current_sum = 0

    for number in nums:
        current_sum += number
        totals.append(current_sum)

    return totals


"""
Performance Analysis - Problem 5

Best-case time: O(n).
Worst-case time: O(n).
Average-case time: O(n).
Space complexity: O(n) for the returned list, plus O(1) auxiliary
space for the running sum.

I chose a cumulative sum because each new total can be calculated using
the previous total and the next number. This avoids repeatedly summing
the same elements.

Optimization comparison:
The original running_total_naive() function takes O(n^2) time because
it recalculates each prefix sum. The optimized running_total() function
takes O(n) time by processing each element once. Both require O(n)
space for their output lists, but the optimized version avoids creating
repeated temporary slices and performing repeated sums.

The trade-off is that the optimized function maintains a running_sum
variable, but this small amount of state greatly improves performance.
"""


# TEST CASES FOR ALL FIVE PROBLEMS
if __name__ == "__main__":

    # Problem 1: Most Frequent Element
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([]) is None
    assert most_frequent([7]) == 7
    assert most_frequent([2, 2, 5, 5]) in (2, 5)

    # Problem 2: Remove Duplicates
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([3, 2, 1]) == [3, 2, 1]

    # Problem 3: Find Pairs
    assert set(find_pairs([1, 2, 3, 4], 5)) == {
        (1, 4), (2, 3)
    }
    assert find_pairs([], 5) == []
    assert find_pairs([1, 2, 3], 20) == []
    assert find_pairs([-2, 2, 0], 0) == [(-2, 2)]

    # Problem 4: Dynamic List Resizing
    assert add_n_items(0) == []
    assert add_n_items(2) == [0, 1]
    assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

    try:
        add_n_items(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative n should raise ValueError")

    # Problem 5: Running Totals
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([]) == []
    assert running_total([-1, 2, -3]) == [-1, 1, -2]
    assert running_total([5]) == [5]

    # Compare original and optimized implementations
    test_numbers = [1, 2, 3, 4, 5]
    assert running_total(test_numbers) == running_total_naive(test_numbers)

    print("All performance_lab.py tests passed.")
