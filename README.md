# WFsim

+++++++++++++++++++++++++++

ABSTRACT

WFSim generates SNP data in Wright-Fisher populations, forward in time. 

Supports customizable parameters such as effective population size, number of loci, mutation rate, theta, bottleneck duration etc

Output is generated in GENEPOP format

It is strongly recommended that users read the accompanying manuscript before using WFsim. 


USAGE OVERVIEW
1. The application could be run on any OS.

2. Python 3.8 or later is required to run the program

INSTALLATION
1. Make a new WFsim directory

        mkdir WFsim
        cd WFsim
   
3. Clone the repository

        git clone https://github.com/NiharaDeSilva/WFsim.git
   
HOW TO RUN

usage: python3 run.py [--m Minimum Allele Frequency] [--r Mutation Rate] [--lNe Lower of Ne Range] [--uNe Upper of Ne Range] [--i Lower of Theta Range] [--o Upper of Theta Range] [--lD  Lower of Duration Range] [--uD Upper of Duration Range] [--i Number of individuals] [--l Number of Loci] [--o output/sim_output.txt]


```
positional arguments:     
    --m     Minimum Allele Frequency (size: 0-1)
    --r     Mutation Rate (size: 0-1)
    --lNe   Lower of Ne Range (size: 10-)
    --uNe   Upper of Ne Range (size: -500)
    --lT    Lower of Theta Range (size: 1-)
    --uT    Upper of Theta Range (size: -10)
    --lD    Lower of Duration Range (size: 1-)
    --uD    Upper of Duration Range 
    --i     Number of individuals
    --l     Number of Loci
    --o     Output Filenme
```

Run the program

        python3 run.py --m 0.01 --r 0.0001 --lNe 100 --uNe 500 --i 300 --o output/sim_output.txt



 
