# Differential Power Analysis (DPA) Attack Implementation

## Overview
This repository contains the implementation of a Differential Power Analysis (DPA) attack using Python. DPA is a side-channel attack that exploits power consumption variations in cryptographic operations to extract secret keys. The implementation targets AES encryption, focusing on power consumption during the Substitution Box (S-Box) operation.

## Software and Tools
- **Python:** Programming language used for implementation.
- **NumPy:** Library for numerical computations.

## Repository Structure
- `calculateSboxOutput.py`: Contains a predefined S-Box array and functions to simulate the substitution step in cryptographic algorithms.
- `getInput.py`: Functions to load power consumption traces and additional cryptographic data.
- `Main.py`: Core script handling the DPA attack process, including data loading, key byte iteration, and trace analysis.

## Results
The implementation successfully reveals the AES secret key with a close resemblance to the original key, differing by only half a byte. Various conditions such as segment lengths and select bits were tested to evaluate their impact on key extraction efficiency.

## Conclusion
This project demonstrates a successful implementation of a DPA attack, highlighting the influence of different parameters on the efficiency of cryptographic key extraction.

---

For more detailed information please refer to the provided [report](https://github.com/fereshtehbaradaran/Differential_Power_Attack_Implementation/blob/main/report.pdf).
