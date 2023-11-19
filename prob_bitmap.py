import random
import math

def estimate_flow_spread_with_sampling(m, flow_spread, p):
    # Initialize the bitmap
    bitmap = [0] * m

    # Simulate the flow with sampling
    for _ in range(flow_spread):
        if random.random() < p:  # Only record with probability p
            bit_index = random.randint(0, m - 1)
            bitmap[bit_index] = 1

    # Count the number of zero bits
    zero_bits = bitmap.count(0)

    # Handle the case where zero_bits is 0
    if zero_bits == 0:
        estimated_spread = m / p
    else:
        # Estimate the flow spread considering the sampling probability
        estimated_spread = (-m * math.log(zero_bits / m)) / p


    return (flow_spread, estimated_spread)

# Bitmap size and sampling probability
m = 10000
p = 0.1
# Flow spreads to simulate
flow_spreads = [100, 1000, 10000, 100000, 1000000]
# Estimating the spread for each flow with sampling
probabilistic_estimates = [estimate_flow_spread_with_sampling(m, spread, p) for spread in flow_spreads]

# Writing the results to a file
probabilistic_output_file_path = './prob_bitmap_output.txt'
with open(probabilistic_output_file_path, 'w') as file:
    for true_spread, estimated_spread in probabilistic_estimates:
        file.write(f"{true_spread} {estimated_spread:.2f}\n")

