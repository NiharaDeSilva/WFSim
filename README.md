# WFsim

+++++++++++++++++++++++++++

ABSTRACT

WFSim generates SNP data in Wright-Fisher populations, forward in time. 

Supports customizable parameters such as Effective population size, number of loci, mutation rate, theta, bottleneck duration etc

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

usage: python main [--s number of trails] [--o input]

```
positional arguments:
    --n     Flag for Monomorphic loci (default: False)
    --m     Minimum Allele Frequency (size: 0-1)
    --r     Mutation Rate (size: 0-1)
    --lNe   Lower of Ne Range (size: 10-)
    --uNe   Upper of Ne Range (size: -500)
    --lT    Lower of Theta Range (size: 1-)
    --uT    Upper of Theta Range (size: -10)
    --lD    Lower of Duration Range (size: 2-)
    --uD    Upper of Duration Range (size: -8)
```

Run the program

        python main --s 1000 --o exampleData/genePop10Ix30L > output.txt



 
