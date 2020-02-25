

limit = int(input("Upto which number you want to know the prime number : "))
count = 2
prime_numbers = []
limit = limit + 1

while count != limit:
    prime_numbers = prime_numbers + [count]
    count += 1

for current in prime_numbers:
    multiples = 1
    multiple_limit = limit // current
    while multiples != multiple_limit:
        multiples += 1
        number_deleted = current * multiples
        if number_deleted in prime_numbers:
            prime_numbers.remove(number_deleted)
        else:
            continue
print(prime_numbers)
