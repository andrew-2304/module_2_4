# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
#
# print(sum_)



# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} х {j} = {i * j}')


# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i, k in dict_.items():
#     print(i, k)






numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n <= 1:
        print(n, '- не простое и не сложное число')
        continue
    else:
        f = n ** (1 / 2)
    for a in range(2, int(f + 1)):
        if n % a == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
print('Простые числа ', primes)
print('Составные числа', not_primes)


