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
    python3 run.py [options]
    
Example:
    python3 run.py --m 0.01 --r 0.0001 --lNe 100 --uNe 500 --i 300 --o output/sim_output.txt
"""

# Default Parameters
minAlleleFreq = 0.05
mutationRate = 0.000000012
lowerNe = 150
upperNe = 250
lowerTheta = 0.000048
upperTheta = 0.0048
lowerDuration = 2
upperDuration = 8
loci = 160
individuals = 200
filename = "output.txt"

# Initialize Argument Parser
parser = argparse.ArgumentParser(description="Run population genetics simulation with configurable parameters.")

# Define Arguments with Default Values
parser.add_argument("--m", type=float, help="Minimum Allele Frequency", default=minAlleleFreq)
parser.add_argument("--r", type=float, help="Mutation Rate", default=mutationRate)
parser.add_argument("--lNe", type=int, help="Lower limit of Ne Range", default=lowerNe)
parser.add_argument("--uNe", type=int, help="Upper limit of Ne Range", default=upperNe)
parser.add_argument("--lT", type=float, help="Lower limit of Theta Range", default=lowerTheta)
parser.add_argument("--uT", type=float, help="Upper limit of Theta Range", default=upperTheta)
parser.add_argument("--lD", type=float, help="Lower limit of Duration Range", default=lowerDuration)
parser.add_argument("--uD", type=float, help="Upper limit of Duration Range", default=upperDuration)
parser.add_argument("--i", type=int, help="Number of individuals", default=individuals)
parser.add_argument("--l", type=int, help="Number of loci", default=loci)
parser.add_argument("--o", type=str, help="Output file path", default=filename)

# Parse Arguments
args = parser.parse_args()

if args.lNe > args.uNe:
    print("ERROR: Lower Ne value (--lNe) cannot be greater than Upper Ne value (--uNe).")
    exit(1)

if args.lNe < 1 or args.uNe < 1:
    print("ERROR: Ne values (--lNe, --uNe) must be positive integers.")
    exit(1)

rangeNe = (args.lNe, args.uNe)
rangeDuration = (args.lD, args.uD)
rangeTheta = (args.lT, args.uT)

output_dir = os.path.dirname(args.o)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Redirect Output to File
output_path = os.path.abspath(args.o)
with open(output_path, "w") as file:
    sys.stdout = file
    simulate_population(args.l, rangeNe, rangeTheta, args.i, args.m, args.r, rangeDuration)

sys.stdout = sys.__stdout__

print(f"Simulation completed. Results saved to: {os.path.abspath(args.o)}")
