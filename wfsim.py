#!/usr/bin/env python3

import argparse
import os
import sys
from engine.main import simulate_population

"""
Population Simulation 
-------------------------------------
This script runs a population simulation using configurable parameters.

Usage:
    python3 wfsim.py [options]
    
Example:
    python3 wfsim.py --m 0.01 --r 0.0001 --lNe 100 --uNe 500 --i 300 --o output/sim_output.txt
"""
import argparse
import os
import sys

def run_simulation(minAlleleFreq=0.05, mutationRate=0.000000012, lowerNe=150, upperNe=250,
                    lowerTheta=0.000048, upperTheta=0.0048, lowerDuration=2, upperDuration=8,
                    loci=160, individuals=200, filename="output.txt"):
    # Validate input values
    if lowerNe > upperNe:
        raise ValueError("Lower Ne value cannot be greater than Upper Ne value.")
    if lowerNe < 1 or upperNe < 1:
        raise ValueError("Ne values must be positive integers.")

    rangeNe = (lowerNe, upperNe)
    rangeDuration = (lowerDuration, upperDuration)
    rangeTheta = (lowerTheta, upperTheta)

    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Redirect output to file
    output_path = os.path.abspath(filename)
    with open(output_path, "w") as file:
        sys.stdout = file
        simulate_population(loci, rangeNe, rangeTheta, individuals, minAlleleFreq, mutationRate, rangeDuration)

    # sys.stdout = sys.__stdout__
    # print(f"Simulation completed. Results saved to: {output_path}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run population genetics simulation with configurable parameters.")

    parser.add_argument("--m", type=float, help="Minimum Allele Frequency", default=0.05)
    parser.add_argument("--r", type=float, help="Mutation Rate", default=0.000000012)
    parser.add_argument("--lNe", type=int, help="Lower limit of Ne Range", default=150)
    parser.add_argument("--uNe", type=int, help="Upper limit of Ne Range", default=250)
    parser.add_argument("--lT", type=float, help="Lower limit of Theta Range", default=0.000048)
    parser.add_argument("--uT", type=float, help="Upper limit of Theta Range", default=0.0048)
    parser.add_argument("--lD", type=float, help="Lower limit of Duration Range", default=2)
    parser.add_argument("--uD", type=float, help="Upper limit of Duration Range", default=8)
    parser.add_argument("--i", type=int, help="Number of individuals", default=200)
    parser.add_argument("--l", type=int, help="Number of loci", default=160)
    parser.add_argument("--o", type=str, help="Output file path", default="output.txt")

    args = parser.parse_args()
    run_simulation(args.m, args.r, args.lNe, args.uNe, args.lT, args.uT, args.lD, args.uD, args.l, args.i, args.o)

if __name__ == "__main__":
    parse_arguments()
