from primesieve import Iterator


def generate_primes(n, file_name):
    counter = 1

    with open(file_name, 'w') as f:
        it = Iterator()
        prime = it.next_prime()

        while prime < n:
            if counter < 10:
                f.write('{} '.format(prime))
                counter += 1
            else:
                f.write('{}\n'.format(prime))
                counter = 1
            prime = it.next_prime()
