#!/bin/bash
#SBATCH --job-name=WFSim                       # Job name
#SBATCH --mail-type=ALL                        # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=suhashidesilva@ufl.edu     # Where to send mail
#SBATCH --ntasks=1		                         # Number of tasks
#SBATCH --cpus-per-task=1	                     # Number of cores per task
#SBATCH --mem=10gb                             # Job memory request
#SBATCH --time=24:00:00                        # Time limit hrs:min:sec
#SBATCH --output=serial_test_%j.log            # Standard output and error log
pwd; hostname; date

module load R/4.1
chmod +rwx /blue/boucher/suhashidesilva/WFSim/WFSim/

echo "Running script on single CPU core"

#python /blue/boucher/suhashidesilva/ONeSAMP_3.1/ONeSAMP_3/main.py --s 20000 --o /blue/boucher/suhashidesilva/ONeSAMP_3.1/ONeSAMP_3/exampleData/genePop5Ix5L > /blue/boucher/suhashidesilva/ONeSAMP_3.1/ONeSAMP_3/genePop5Ix5L.out

folder="/blue/boucher/suhashidesilva/WFSim/WFSim/"
output="/blue/boucher/suhashidesilva/WFSim/WFSim/output"
logFile="/blue/boucher/suhashidesilva/WFSim/WFSim/output/execution_stats.log"


lociList=(40 80 160 320)
#individualSizeList=(50 100 200)
#effectivePopulationRangeList=((50,100),(50,150),(50,250))
#durationRangeList=((2,2),(4,4),(16,16))
numReps=10

echo "Loci,Iteration,Execution Time (s),Memory Used (MB)" > "$logFile"

for loci in "${lociList[@]}"; do
#for sampleSize in "${individualSizeList[@]}"; do
#for effectivePopulation in "${effectivePopulationRangeList[@]}"; do
  for ((i=1; i<=$numReps; i++)); do
    outputFileName="genePop${loci}L_${i}"
#    loci=160
    rangeNe="150 250"            # Space-separated range for Ne
    rangeTheta="0.000048 0.0048" # Space-separated range for Theta
    individualsDirectInput=100   # Number of individuals
    minAlleleFreq=0.05           # Minimum allele frequency
    mutationRate=0.000000012     # Mutation rate
    rangeDuration="2 8"          # Space-separated range for Duration

    start_time=$(date +%s)
    /usr/bin/time -f "%e %M" -o time_mem.log python main.py \
      --l "$loci" \
      --lNe $(echo $rangeNe | cut -d' ' -f1) \
      --uNe $(echo $rangeNe | cut -d' ' -f2) \
      --lT $(echo $rangeTheta | cut -d' ' -f1) \
      --uT $(echo $rangeTheta | cut -d' ' -f2) \
      --i "$individualsDirectInput" \
      --m "$minAlleleFreq" \
      --r "$mutationRate" \
      --lD $(echo $rangeDuration | cut -d' ' -f1) \
      --uD $(echo $rangeDuration | cut -d' ' -f2) \
      > /blue/boucher/suhashidesilva/WFSim/WFSim/output/"$outputFileName"

        # End time and memory used
    execution_time=$(cut -d' ' -f1 time_mem.log) # Execution time in seconds
    memory_used=$(cut -d' ' -f2 time_mem.log)    # Memory used in KB

    # Convert memory to MB
    memory_used_mb=$(echo "scale=2; $memory_used / 1024" | bc)

    # Write to the log file
    echo "$loci,$i,$execution_time,$memory_used_mb" >> "$logFile"

    # Sleep to prevent overloading
    sleep 1
  done
done

# Clean up temporary files
rm -f time_mem.log


date

