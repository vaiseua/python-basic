

def power_numbers(*numbers, power=2):
    return [number ** power for number in numbers]
#power_numbers(1, 2, 5, 7)
#print(power_numbers(1, 2, 5, 7))


def is_prime(number):
    f = [0, 1]
    for i in number:
        for a in range(2, i):
            if i % a == 0: #or i == 0 or i == 1:
               f.append(i)
               break
    return list(filter(lambda x: x not in f, number))


#ODD = lambda x: x % 2 == 0
#EVEN = lambda x: x % 2 != 0



ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(number, filter_type):
    if filter_type == PRIME:
        return is_prime(number)
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, number))
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, number))


print(filter_numbers([0, 1, 2, 3, 4, 5, 7, 11], PRIME))

