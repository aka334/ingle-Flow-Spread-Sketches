---
Title: Implementation of Single-Flow Spread Sketches
Author: Aayush Karki
Date: 11/18/2023
---

# Bitmap and HyperLogLog Flow Spread Estimation

This project includes three Python scripts designed to estimate the spread of a flow in a network. The scripts use different methods to simulate and analyze network flow, offering a range of approaches from basic bitmap counting to advanced probabilistic models and HyperLogLog estimation.

## Bitmap Flow Spread Estimation (`Bitmap.py`)

### Overview
- `Bitmap.py` contains a Python script for estimating flow spread using a bitmap-based approach.
- The script simulates the flow by setting bits in the bitmap and estimates the spread based on the proportion of zero bits.

### Usage
- Modify the `m` variable to set the size of the bitmap.
- Adjust the `flow_spreads` list to include the flow spreads you want to simulate.
- Run the script to obtain estimates for each flow spread.
- The results are written to a file named `bitmap_output.txt`.

## Probabilistic Bitmap Flow Spread Estimation (`prob_bitmap.py`)

### Overview
- `prob_bitmap.py` is an extension of the Bitmap technique with a sampling probability `p`.
- It simulates the flow with sampling and estimates the spread considering the sampling probability.

### Usage
- Modify the `m` and `p` variables to set the size of the bitmap and the sampling probability, respectively.
- Adjust the `flow_spreads` list to include the flow spreads you want to simulate.
- Run the script to obtain estimates for each flow spread with sampling.
- The results are written to a file named `prob_bitmap_output.txt`.

## HyperLogLog Flow Spread Estimation (`hyperlog.py`)

### Overview
- `hyperlog.py` contains a Python script for estimating flow spread using the HyperLogLog technique.
- It uses a probabilistic data structure to estimate the number of distinct elements in a flow.

### Usage
- Modify the `m` variable to set the number of registers in the HyperLogLog data structure.
- Adjust the `flow_spreads` list to include the flow spreads you want to simulate.
- Run the script to obtain estimates for each flow spread using HyperLogLog.
- The results are written to a file named `hyperloglog_output.txt`.

## Output Files
- The estimated flow spreads are written to output files in the following formats:
  - `bitmap_output.txt`: True spread and estimated spread (for Bitmap).
  - `prob_bitmap_output.txt`: True spread and estimated spread (for Probabilistic Bitmap).
  - `hyperloglog_output.txt`: True spread and estimated spread (for HyperLogLog).

## Dependencies
- These scripts use standard Python libraries and NumPy for efficient array manipulation.