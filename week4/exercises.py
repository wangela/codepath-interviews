# RECURSION / BACKTRACKING
## Subsets
### Combinations
def combine(A, B):
    # Parameters: A and B are integers
    # Perform: Return all possible combinations of B numbers out of 1 2 3...A.
    #   Make sure the elements in each combination are sorted and the combinations are sorted.
    # Output: An array of sorted combinations (in list form)
    # Clarification: A, B always positive?

    return combine_util(1, A+1, B)

def combine_util(start, end, B):
    # Parameters: start, end, and B are integers
    # Output: A list of every combination in A with B elements
    if end - start == B:
        return [list(range(start, start + B))]
    elif B == 0:
        return [[]]

    answer = []

    for i in range(start, end + 1 - B):
        for combo in combine_util(i + 1, end, B- 1):
            answer.append([i] + combo)

    return answer

def combine_util_alt(A, B):
    # Parameters: A is a list, B is an integer
    # Output: A list of every combination in A with B elements
    answer = []
    for i in range(len(A)):
        if B == 1:
            answer.append(A[i])
        else:
            for c in combine_util(A[i + 1:], B - 1):
                combo.append(A[i])
                combo.append(c)
                answer.append(combo)
    return answer

## Bruteforce Builder
### Letter Phone
digits = list(range(10))
for i, digit in enumerate(digits):
	digits[i] = str(digit)
letters = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
mappings = dict(zip(digits, letters))

def letterCombinations(A):
    # Parameters: A is a digit string
    # Output: A list of all letter combinations that the number could represent,
    #       lexigraphically sorted
    # Example:
    #   Input: "23"
    #   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    #   "0" -> "0"
    #   "1" -> "1"
    if len(A) == 1:
        letters = mappings[A]
        starter_list = []
        for letter in letters:
            starter_list.append(letter)
        return starter_list
    else:
        digits_tail = A[-1]
        digits_head = A[:-1]
        tail_mapping = mappings[digits_tail]
        combinations = []
        for each in letterCombinations(digits_head):
            for letter in tail_mapping:
                concat_maps = each + letter
                combinations.append(concat_maps)
        return combinations

## Permutations
### Permutations
def permute(A):
    # Parameters: A list of unique numbers
    # Output: All possible permutations of the numbers
    # Example:
    #   [1,2,3] -> [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
    permutations = []
    permute_util(A, permutations, 0, len(A))
    return permutations


def permute_util(A, combos, left, right):
    if left == right:
        print(A)
        combos.append(A)
    else:
        for i in range(left, right):
            A[i], A[left] = A[left], A[i]
            print(i)
            permute_util(A, combos, left+1, right)
            A[i], A[left] = A[left], A[i]

# BIT MANIPULATION
## Bit Play
### Number of 1 Bits
def numSetBits(A):
    # Parameter: A is an unsigned integer in binary representation
    # Output: Return an integer of the number of "1" bits in A
    # Example: 32-bit integer 11 has binary representation 00000000000000000000000000001011
    #   Return 3
    #  110110
    #  110101
    #  110100 +1
    #  110011
    #  110000 +2
    #  101111
    #  100000 +3
    #  011111
    #  000000 +4
    count = 0
    while(A):
        A &= A - 1
        count += 1
    return count

### Reverse Bits
def reverse(A):
    # Parameter: A is a 32-bit unsigned integer
    # Output: Reverse the bits of the 32-bit unsigned integer
    # Example:
    #   x = 3, 0000 0000 0000 0000  0000 0000 0000 0011
    #   ouput  1100 0000 0000 0000  0000 0000 0000 0000 = 3221225472
    answer = 0
    for n in range(32):
        if A & (1 << n):
            answer += 2 ** (31 - n)
    return answer


## Bit Manipulation
### Single Number
def singleNumber(A):
    # Input: A is a list of integers, where every element appears twice except for one. Find that single one
    # Perform: Linear time complexity, no extra memory
    # Output: The single integer that is not repeated in the list
    value = 0
    for i in range(0, len(A)):
        value ^= A[i]
    return value

## Bucketing
### Min XOR Value
def findMinXor(A):
    # Input: A is a list of integers (2 <= N <= 100,000) (0 <= A[i]<= 1,000,000,000)
    # Perform: Find the pair of integers with the smallest XOR value
    # Output: The minimum XOR value
    # Examples:
    #   Input [0, 2, 5, 7]
    #   Outuput 2 (0 ^ 2)
    #   Input [0, 4, 7, 9]
    #   Output 3 (4 ^ 7)
    A.sort()
    length = len(A)
    for i in range(0, length - 1):
        curr_xor = A[i] ^ A[i + 1]
        min_xor = min(min_xor, curr_xor)
    return min_xor

def findMinXor_naive(A):
    # Input: A is a list of integers (2 <= N <= 100,000) (0 <= A[i]<= 1,000,000,000)
    # Perform: Find the pair of integers with the smallest XOR value
    # Output: The minimum XOR value
    # Examples:
    #   Input [0, 2, 5, 7]
    #   Outuput 2 (0 ^ 2)
    #   Input [0, 4, 7, 9]
    #   Output 3 (4 ^ 7)
    min_xor = max(A)
    length = len(A)
    for i in range(0, length):
        for j in range(i+1, length):
            curr_xor = A[i] ^ A[j]
            if curr_xor < min_xor:
                min_xor = curr_xor
    return min_xor

### Mock Interview
# A xor B
#   110110
#   011001
#   101111
#   0101
#   1001
#   1100 --> 12
#   1111 --> 15
#   1001 --> 9
#   1000
#   0110 --> 6
#   0101 --> 5
#   0011
#   0110 --> 15 xor 9 is 6
#   1111 --> 6 xor 9 is 15
#   U >> 1
#   1110 --> 14
#   1010 --> 10
#   0010 --> 2
def max_xor(lower, upper):
    msb = get_msb(upper)
    lsbm = get_ls1(upper)
    lsbl = get_ls1(lower)
    lsb = lsbm
    if lsbl < lsb:
        lsb = lsbl
    target = max_bits(msb, lsb)
    return target

def get_msb(value):
    count = 0
    while value:
        value = value >> 1
        count += 1
    return count

def get_ls1(value):
    count = get_msb(value ^ (value - 1))
    return count

def max_bits(most, least):
    all_ones = 0
    power = 0
    for i in range(1, least):
        power += 1
    for j in range(least, most + 1):
        all_ones += 2**power
        power += 1
    return all_ones

### Challenge 1
def factorial(N):
    if N == 1:
        return 1
    else:
        return N * factorial(N - 1)

### Challenge 2
def gcd(A, B):
    greater = B
    lesser = A
    if A > B:
        greater = A
        lesser = B
    if lesser == 0:
        return greater
    else:
        return gcd(greater % lesser, lesser)

### Challenge 3
def permute(A):
    # Input: A is a list of 2 or more integers
    # Output: ALl permutations of the list. Assume all numbers are unique
    length = len(A)
    permutations = permute_util(A, 0, length)

def permute_util(A, start, end):
    permutations = []
    if end - start = 1:
        perm1 = []
        perm1.append(A[start])
        perm1.append(A[end])
        perm2 = []
        perm2.append(A[end])
        perm2.append(A[start])
        permutations.append(perm1)
        permutations.append(perm2)
        return permutations
    else:
        for each in A:
            permutations.append(each)
            for permutation in permute_util(A)

# HackerRank test
## Problem 1 - Pascal's Triangle
def pascalTriangle(k):
    # Parameter: k is an integer, 2 <= k <= 25
    # Output: Print the first k rows of Pascal's Triangle.
    #   Separate entries of the triangle with a space
    #   n = 0 to n = k-1
    line = ""
    if k == 1:
        line = "1"
    elif k == 2:
        pascalTriangle(1)
        line = "1 1"
    else:
        prev = pascalTriangle(k-1).split()
        line += "1"
        for r in range(1, k-1):
                line += " " + str(int(prev[r]) + int(prev[r - 1]))
        line += " 1"
    print(line)
    return line

1 4
5 4
5 9
14 9

1 2
3 2
3 5
3 8

## Problem 2 - Is Possible
def isPossible(a, b, c, d):
    # Parameters: a, b, c, d where 1 <= a, b, c, d <= 1000
    # Perform: Can (c, d) come from (a, b) by performing 0+ operations of (a + b, b) or (a, a + b)
    # Output: "Yes" or "No"
    # Example: (1, 4, 5, 14) -> "Yes" because (1, 4) -> (5, 4) -> (5, 9)
    #       (1, 4, 5, 9) -> (1, 4, 0, 9) -> (1, 4, 0, 4) OR (1, 4, 14, 14) -> (1, 4, 0, 4)
    # Example: (1, 2, 3, 6) -> "No" becuase (1, 2) -> (3, 2) -> (3, 5) and (1, 2) -> (1, 3)-> (1, 4...6)
    if c == a and d == b:
        return "Yes"
    elif c < a or d < b:
        return "No"
    elif (c % (a + b) == 0) and (d % (a + b) == a or d % (a + b) == b):
        return "Yes"
    elif (d % (a + b) == 0) and (c % (a + b) == a or c % (a + b) == b):
        return "Yes"
    elif (c % (a + b) == a or c % (a + b) == b) and (d % (a + b) == a or d % (a + b) == b):
        return "Yes"
    elif isPossible(a, b, c - (a + b), d) == "Yes" or isPossible(a, b, c, d - (a + b)) == "Yes":
        return "Yes"
    else:
        return "No"


## Problem 3 - Counter Game
def counterGame(tests):
    # Parameter: tests is a string array where tests[i] = N.
    # Perform: Louise goes first
    #       If N == 1 at the beginning, Richard wins
    #           If N is not a power of 2, reduce the counter by the largest power of 2 less than N
    #           If N is a power of 2, reduce the counter by half of N
    #       Next player takes the result as their N
    #       If N == 1 at the end of the turn, player wins
    # Output: For each i in tests, print the winner of that game
    # Example: N = 6. Louise 110 << 1 = 10 Richard << 1 = 1 -> Richard
    for input in tests:
        n = int(input)
        if n == 1:
            print("Richard")
            continue
        else:
            player = "Richard"
            while n > 1:
                if int(n) & int(n-1):
                    x = bitCount(n)
                    n -= 2 ** (x - 1)
                else:
                    n /= 2
                if player == "Louise":
                    player = "Richard"
                else:
                    player = "Louise"
            if n == 1:
                print(player)
                continue
    return


def bitCount(N):
    num_bits = 0
    N = int(N)
    while N >> num_bits:
        num_bits += 1
    return num_bits