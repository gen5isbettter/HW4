def square_and_multiply(a, b, N):
    b_bin = bin(b).replace("0b","")
    list_bin = list(b_bin)
    temp = 0
    for i in range(len(list_bin)):
        #square and multiply
        if i != len(list_bin):
            if int(list_bin[i]) == 1 and i != 0:
                temp = (((temp ** 2) % N) * a ) % N
                print(f'step {i + 1} - square and multiply - current value: {temp}')
            # square
            elif i != 0:
                temp = (temp ** 2) % N
                print(f'step {i + 1} - square - current value: {temp}')
            #base case
            elif i == 0:
                temp = a
                print(f'step {i + 1} - base case - current value: {temp}')

    return temp