import numpy as np
import hashlib

def hyperloglog_estimate_flow_spread(m, flow_spreads):
    results = []
    for flow_spread in flow_spreads:
        registers = np.zeros(m, dtype=int)

        for element in range(flow_spread):
            # Hashing the element and determining the register index
            hash_value = hash(str(element))
            register_index = hash_value % m

            # Shifting hash value and calculating leading zeros
            shifted_hash = hash_value // m
            leading_zeros = 32 if shifted_hash == 0 else len(bin(shifted_hash)) - bin(shifted_hash).rfind('1') - 1

            registers[register_index] = max(registers[register_index], leading_zeros + 1)

        # HyperLogLog estimation formula
        alpha_m = 0.7213 / (1 + 1.079 / m)
        estimate = alpha_m * m * m * (1 / np.sum(np.power(2.0, -registers)))

        # Small range correction
        if estimate < (5/2) * m:
            num_zeros = np.count_nonzero(registers == 0)
            if num_zeros > 0:
                estimate = m * np.log(m / num_zeros)

        results.append((flow_spread, estimate))

    return results

m = 256
flow_spreads = [1000, 10000, 100000, 1000000]
hyperloglog_estimates = hyperloglog_estimate_flow_spread(m, flow_spreads)

# Writing the results to a file
output_file_path = './hyperloglog_output.txt'
with open(output_file_path, 'w') as file:
    for true_spread, estimated_spread in hyperloglog_estimates:
        file.write(f"{true_spread} {estimated_spread}\n")
