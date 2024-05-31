#!/bin/bash
#$ -S /bin/bash      # the shell language when run via the job scheduler
#$ -cwd               # job should run in the current working directory
#$ -j y               # STDERR and STDOUT should be joined
#$ -l mem_free=200G     # job requires up to 400 GiB of RAM per slot
#$ -l scratch=200G      # job requires up to 200 GiB of local /scratch space
#$ -l h_rt=12:00:00    # job requires up to 2 hours of runtime


# Mount the current directory to the container
# Any directory that needs to be accessed by the container should be mounted

module load cuda
module load CBI miniconda3
conda activate dscript 

echo "SGE_GPU: $SGE_GPU"
export CUDA_VISIBLE_DEVICES=$SGE_GPU
nvcc -V

directory=/wynton/home/yang/apennacchio/PPI

dscript predict --pairs $directory/data/protein_pairs.tsv --seqs $directory/data/database.fasta --model $directory/models/topsy_turvy_v1.sav  --device $SGE_GPU

[[ -n "$JOB_ID" ]] && qstat -j "$JOB_ID"
