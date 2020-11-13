# n = 5
# seq_text = "5 1 4 2 3"


def longest_subsequence(arr, f):
    dp = [1] * len(arr)
    choice = [None] * len(arr)
    max_index = 0
    max_value = 1
    for i in range(1, len(arr)):
        curr_choice = None
        for j in range(i - 1, -1, -1):
            if f(arr[i], arr[j]) and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
                curr_choice = j
        choice[i] = curr_choice
        if dp[i] > max_value:
            max_value = dp[i]
            max_index = i

    answer = []
    while max_index >= 0:
        answer.append(arr[max_index])
        max_index = choice[max_index]
        if max_index is None:
            break
    return " ".join(map(str, answer[::-1]))


f = open("rosalind_lgis.txt", "r")
num_text = f.readline()
n = int(num_text)
seq_text = ''
for x in f:
    seq_text += x

f.close()

seq = [int(x) for x in seq_text.split(' ')]

# print(n)
# print(len(seq))

sol_increment = longest_subsequence(seq, lambda x, y: x > y)
sol_decrement = longest_subsequence(seq, lambda x, y: x < y)

f2 = open("./sol_longest_seq.txt", "w")
f2.write(sol_increment)
f2.write('\n')
f2.write(sol_decrement)
f2.close()
