from Q1 import elliptic_addition
from Q1 import main
from Square_and_multiply import square_and_multiply
#need to send the mod, a, b, and c
print("--------------------------Q1--------------------------")
main(29, 1, 7)

print("--------------------------Q2--------------------------")
alpha = [0,376]
a_bob = 5
a_alice = 3

a2 = elliptic_addition(alpha, alpha, 758, -1)
a3_alice = elliptic_addition(a2, alpha, 738, -1)
a4 = elliptic_addition(a2, a2, 738, -1)
a5_bob = elliptic_addition(a3_alice, a2, 738, -1)

print(f'alice\'s public key, {a_alice}*{alpha}= {a3_alice}')
print(f'bob\'s public key, {a_bob}*{alpha}= {a5_bob}')

a_10 = elliptic_addition(a5_bob, a5_bob, 738, -1)
common_key = elliptic_addition(a_10, a5_bob, 738, -1)

print(f'Bob & Alice\'s common key, bb*ba*alpha = {common_key} ')

print("--------------------------Q3--------------------------")
#compute a^b mod N using square and multiply

part_a = square_and_multiply(35973, 56872884723247, 83884)
#answer = square_and_multiply(15, 1, 11)
print(f'part 3a: {part_a}')

part_b = square_and_multiply(984327455683,1253489582, 94348472542)
#answer = square_and_multiply(15, 1, 11)
print(f'part 3b: {part_b}')

#test = square_and_multiply(439, 233, 713)
#print('test: ', test)