import random
import math
def number_is_prime(number):
    """проверка что число простое"""
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True
def generate_prime_p():
    """генерирует открытое простое число p"""
    p = random.randint(10, 100)
    is_prime = number_is_prime(p)
    while not is_prime:
        p = random.randint(10, 100)
        is_prime = number_is_prime(p)
    return p
def number_g(p):
    """возвращает g - первообразный корень по модулю р"""
    g = round(math.sqrt(p))
    is_prime = number_is_prime(g)
    while not is_prime:
        g = g - 1
        is_prime = number_is_prime(g)
    return g
p = generate_prime_p()
g = number_g(p)
print("p - ", p)
print("g - ", g)
a = random.randint(10, 100)
b = random.randint(10, 100)
print("Алиса сгенерировала число a: ", a)
print("Боб сгенерировал число b: ", b)
public_key_alice = int(pow(g, a)) % p
public_key_bob = int(pow(g, b)) % p
print("Публичный ключ Алисы: ", public_key_alice)
print("Публичный ключ Боба: ", public_key_bob)
private_key_alice = int(pow(public_key_bob, a)) % p
private_key_bob = int(pow(public_key_alice, b)) % p
print("Приватный ключи Алисы и Боба: ",private_key_alice, private_key_bob)
