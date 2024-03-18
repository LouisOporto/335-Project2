# Project 2

>  Name - Louis Oporto
>
> Email - louisoporto042@csu.fullerton.edu
>
> Assignment - Project 1
>
> Github Link - https://github.com/LouisOporto/335-Project2
>

\* Contains Algorithm 1's & 2's:
    Pseudocode, Mathmematical Analysis, How It Works
\*

## Algorithm 1: Ensuring Convenient Schedules
### Pseudocode
Combine all student schedules and create a list of possible intervals. Ensuring that it fits the limit of the meeting in minutes and between the available time of students.

    function findSchedule(schedules size n, availableTime size n, limit):
    let list = []
    let n = length of schedules
    let min = "00:00" (Lower Bound)
    let max = "99:99" (Upper Bound)

    for every element in schedule do
        min = min < availableTime[element][0] ? availableTime[element][0] : min
        max = max > availableTime[element][1] ? availableTime[element][0] : max
        for interval in schedule[element] do
            list.append(interval)

    list.sort(key=lambda x: (First:HH, Second:MM)) (sort by HH first and then MM second)

    for element in list[::-1] do (iterate from back to front)
        if element[0] < min do
            if element[1] < min do
                list.remove(element)
            else do
                element[0] = min
        if element[1] > max do
            if element[0] > max do
                list.remvove(x)
            else do
                element[1] = max

    let list_avail = []
    let n = length of list

    for element in list do
        if x == 0 do
            list_avail.append([min, element[0]])
        else if x == n - 1 do
            list_avail.append([element[1], max])
        list_avail.append([(element - 1)[1], element[0]])

    for element in list_avail[::-1] do (iterate from back to front)
        let hr_diff = int(x[1][:2]) - int(x[0][:2])
        let min_diff = int(x[1][3:5]) - int(x[0][3:5])
        if limit >= (hr_diff * 60 + min_diff) do
            if element[1] == max and not limit > (hr_diff * 60 + min_diff) do
                pass
            else if element[0] == min and not limit > (hr_diff * 60 + min_diff) do
                pass
            else do
                list_avail.remove(element)

    return list_avail


###  Complexity and Efficiency Class
Proof by Step Count:
    T(n) = 4 + 3n + 2n^2 + n*logn + 6n + 2 + 4n + 9n + 1
        = 2n^2 + n*logn + 22n + 7
        = O(n^2) Quadratic Growth
        Therefore, T(n) exists in O(f(n^2))
    Proof by Induction
    1. Prediction
    T(n) looks similar to quaratic efficiency O(n^2)

    2. Solve for c
    T(n) <= c*f(n)
    2n^2 + n*logn + 22n + 7 <= c * n^2
    c >= (2n^2 + n*logn + 22n + 7) / n^2
    c >= 2 + logn/n + 22/n + 7/n^2
    let n = 1
    c >= 2 + log(1)/(1) + 22/(1) + 7/(1)^2
    c >= 32

    3. Prove base case
    T(n) <= c * f(n)
    T(1) = 2(1)^2 + (1)*log(1) + 22(1) + 7 = 32
    c * f(1) = 32 * (1)^2 = 32
    32 = 32

    Therefore, base case holds!

    4. Prove inductive step
    If base case holds then, T(n+1) <= c*f(n+1):
    2(n + 1)^2 + (n + 1)*log(n + 1) + 22(n + 1) + 7 <= 32(n + 1)^2
    2n^2 + 4n + 2 + nlog(n + 1) + log(n + 1) + 22n + 22 + 7 <= 32n^2 + 64n + 32
    2n^2 + 26n + 32 + nlog(n + 1) + log(n + 1) <= 32n^2 + 64n + 32
    nlog(n + 1) + log(n + 1) <= 30n^2 + 38n

    30n^2 is greather than nlog(n + 1)
    Therefore T(n + 1) <= c * f(n + 1)

    5. Conclude
    Therefore, T(n) exists in O()

### How It Works
To run this algorithm typpe `py algorithm1.py`
Will ask user to input how many students are in the group. Asking for each memebers schedules and available times. Lastly will ask for the minimum duration of the meeting in minutes.

Given this input the algorithm will combine all the members schedules together and create a list that consist of intervals that are not in the scedules and are between the minimum and maximum available time periods. It will then remove any intervals that go over the duration limit and return the list of possible meeting time intervals.

## Alogrithm 2
### Pseudocode
Combine all student schedules and create a list of possible intervals. Ensuring that it fits the limit of the meeting in minutes and between the available time of students.

    # Sub Function
    function sum(list of numbers): (external function to find sum of given list)
        let sum = 0

        for num in numbers do
            sum += num

        return sum

    # Main Function
    function longestSum(list of numbers):
    if length of numbers == 1 do return numbers[0]

    let n = length of numbers
    maxSum = -sys.maxsize (Lower Bound)
    let left = 0
    let right = 1

    for i in range(n - 1) do
        for j in range(i + 1, n) do
            if sum(numbers[i:j]) > maxSum do
                maxSum = sum(numbers[i:j])
                left = i
                right = j

    return left, right

###  Complexity and Efficiency Class
    Proof by Step Count:
    T(n) = 6 + n + n^2 + 8n^2 + 4n^3 + 1
        = 7 + n + 9n^2 + 4n^3
        = O(n^3) Cubic Growth
        Therefore, T(n) exists in O(n^3)

    Proof by Induction
    1. Prediction
    T(n) looks similar to quaratic efficiency O(n^3)

    2. Solve for c
    T(n) <= c*f(n)
    4n^3 + 9n^2 + n + 7 <= c * n^3
    c >= (4n^3 + 9n^2 + n + 7) / n^3
    c >=  4 + 9/n + 1/n^2 + 7/n^3
    let n = 1
    c >= 4 + 9/(1) + 1/(1)^2 + 7/(1)^3
    c >= 21

    3. Prove base case
    T(n) <= c * f(n)
    T(1) = 4(1)^3 + 9(1)^2 + 1 + 7 = 21
    c*f(1) = 21 * (1)^2 = 21
    21 = 21
    Therefore, base case holds!

    4. Prove inductive step
    If base case holds then, T(n+1) <= c*f(n+1):
    4(n + 1)^3 + 9(n + 1)^2 + n + 1 + 7 <= 21(n + 1)^3
    4(n^3 + 3n^2 + 3n + 1) + 9n^2 + 18n + 9 + n + 8  <= 21(n^3 + 3n^2 + 3n + 1)
    4n^3 + 12n^2 + 12n + 4 + 9n^2 + 18n + 9 + n + 8  <= 21n^3 + 63n^2 + 63n + 21
    4n^3 + 21n^2 + 31n + 21 <= 21n^3 + 63n^2 + 63n + 21
    0 <= 17n^3 + 42n^2 + 32n
    Therefore T(n + 1) <= c * f(n + 1)

    5. Conclude
    Therefore, T(n) exists in O(n^3)

### How It Works
To run this algorithm typpe `py algorithm2.py`
Will ask user input to create a list of numbers to run algorithm. Will also use the provided sample input and print results.

Given a list of numbers, using exhaustive optimization it searches for the best longest sum within the list returning a tuple of the starting index and ending index within the list.
