import numpy as np
from concrete import fhe

def equal(x, y):
    return x == y
    # return bin(xored)[3:]

    # for bit in binary_rep[::-1]:
    #     binary_rep_int.append(int(bit))
    #
    # result = 1
    # for i in binary_rep_int:
    #     result = result & i
    # return result

def g(x, y):
    return x & y
# inputset = [(1,1), (1,2)]

# compiler = fhe.Compiler(f, {"x": "encrypted", "y": "encrypted"})
# circuit = compiler.compile(inputset)

x = 1
y = 14
# print(x & y)
res = (x,y)
print(bin(x))
print(bin(y))
print(res)
print(bin(res))

# print(bin(x))
# print(bin(1))
# print(bin(0b1))
# print(type(bin(x)))
# clear_evaluation = f(x, y)
# homomorphic_eval = circuit.encrypt_run_decrypt(x, y)

# print(x, "==", y, "=", clear_evaluation, "=?")#, bool(homomorphic_eval))
