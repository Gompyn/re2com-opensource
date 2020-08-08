#!/bin/bash
#SBATCH -o ./job.%j.%N.out
#SBATCH --partition=GPU
#SBATCH --qos=high
#SBATCH -J re2com-opensource
#SBATCH --get-user-env
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=120:00:00

module load anaconda/3-4.4.0.1
source activate liyongmin
python __main__.py challenge.yaml --train -v
module purge
