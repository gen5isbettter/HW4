import math
import random

#elliptic addition
def elliptic_addition(p, q, mod, a):
    lda = 0
    if p == q:
        inv = pow(2*p[1], mod-2, mod)
        lda = (3*(p[0]**2) + a)*inv % mod
    else:
        inv = pow((q[0]-p[0]), mod-2, mod)
        lda = (q[1]-p[1])*inv % mod
    new_point = [0,0]
    new_point[0] = (lda**2 - p[0] - q[0]) % mod
    new_point[1] = (lda*(p[0]-new_point[0]) - p[1]) % mod
    return new_point

def main(mod, a, b):
    #part a
    max = int((mod-1)/2)
    #gather residues
    residues = [0]*max
    for i in range(1,max+1):
        residues[i-1] = i*i % mod
    residues = sorted(residues)

    #evaluate the function from 0 to the modulus and see if y^2 is in the residual set

    y_2 = [0]*mod
    y_2_valid = []
    for i in range(mod):
        y_2[i] = (i**3 + a*i + b) % mod


    for i in range(len(y_2)):
        for j in range(len(residues)):
            if y_2[i] == residues[j]:
                #add coordinates
                y_2_valid.append([i, y_2[i]])
                temp = -y_2[i]
                while temp < 0:
                    temp = temp + mod
                    if temp > 0:
                        y_2_valid.append([i, temp])
                break
    print(y_2_valid)

    #verify that each point satisfies the equation

    for point in y_2_valid:
        y = (point[1] ** 2) % mod
        x = (point[0] ** 3 + point[0] + 7) % mod
        if x != y:
            y_2_valid.remove(point)

    #pick any point
    alpha = y_2_valid[int(random.randint(0, len(y_2_valid)-1))]
    print('alpha: ',alpha)

    #part b

    #2a
    alpha2 = elliptic_addition(alpha, alpha, mod, a)
    print('alpha2: ', alpha2)

    #3a
    alpha3 = elliptic_addition(alpha2, alpha, mod, a)
    print('alpha3: ',alpha3)

    #4a
    alpha4 = elliptic_addition(alpha3, alpha, mod, a)
    print('alpha4: ',alpha4)

    #5a
    alpha5 = elliptic_addition(alpha4, alpha, mod, a)
    print('alpha5: ',alpha5)

    #part c
    #8a

    alpha35 = elliptic_addition(alpha3, alpha5, mod, a)
    print("alpha3 + alpha5 = ",alpha35)

    alpha44 = elliptic_addition(alpha4, alpha4, mod, a)
    print("alpha4 + alpha4 = ",alpha44)

    #part d
    #find the number of points |E| of the curve
    num_points = print(f'total number of valid points on the curve: {len(y_2_valid)} + point at infinity = {len(y_2_valid) + 1}')
    #exception! There are 8 points where a3 + a5 != a4 + a4