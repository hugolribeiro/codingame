import sys
import math

n = int(input())
result = 0

cards_log2 = math.floor(math.log2(n))
pow_cards_log2 = int(math.pow(2, cards_log2))

if n == pow_cards_log2:
    result = n
else:
    result = (n - pow_cards_log2) * 2

print(result)


# "Brute force" way. It will timeout at large numbers

# n = int(input())

# stack = [n for n in range(1, n+1)]

# while len(stack) > 1:
#     stack.remove(stack[0])
#     top_card = stack[0]
#     stack.remove(stack[0])
#     stack.append(top_card)


# print(stack[0])
