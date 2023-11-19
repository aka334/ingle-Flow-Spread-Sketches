import random
import math

def estimate_flow_spread(m, flow_spread):
    # Initialize the bitmap
    bitmap = [0] * m

    # Simulate the flow by setting bits in the bitmap
    for _ in range(flow_spread):
        bit_index = random.randint(0, m - 1)
        bitmap[bit_index] = 1

    # Count the number of zero bits
    zero_bits = bitmap.count(0)

    # Handle the case where zero_bits is 0
    if zero_bits == 0:
        print(zero_bits)
        estimated_spread = m 
    else:
        # Estimate the flow spread based on the proportion of zero bits
        estimated_spread = -m * math.log(zero_bits / m)

    return (flow_spread, estimated_spread)


# Bitmap size
m = 10000

# Flow spreads to simulate
flow_spreads = [100, 1000, 10000, 100000, 1000000]

# Estimating the spread for each flow
estimates = [estimate_flow_spread(m, spread) for spread in flow_spreads]

# Writing the results to a file
output_file_path = './bitmap_output.txt'
with open(output_file_path, 'w') as file:
    for true_spread, estimated_spread in estimates:
        file.write(f"{true_spread} {estimated_spread:.2f}\n")