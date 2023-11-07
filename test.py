from concrete import fhe


def are_equal(x, y):
    return x == y


def search_substring(big, target):
    result = False
    target_length = len(target)
    big_length = len(big)
    # running from the beginning until there are target_length bits left to check
    for i in range(big_length - target_length):
        result = result or are_equal(big[i:i + target_length], target)

    return result

inputset = [("abcdef", "bcd"), ("545454", "45")]

compiler = fhe.Compiler(search_substring, {"big": "encrypted", "target": "encrypted"})
circuit = compiler.compile(inputset)

diary = "abcdef"
target = "bcd"

print(search_substring(diary, target))

clear_evaluation = search_substring(diary, target)
homomorphic_eval = circuit.encrypt_run_decrypt(diary, target)

print(homomorphic_eval)
