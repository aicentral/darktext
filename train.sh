#!/bin/bash
#PBS -l procs=1,gpus=1
#PBS -l walltime=21:00:00
#PBS -q normal_q
#PBS -A DeepText
#PBS -W group_list=newriver
#PBS -M nady@vt.edu
#PBS -m bea
cd $PBS_O_WORKDIR
module purge
module load cuda/8.0.44 cudnn Anaconda/2.3.0
source activate tfcv
./flow --train --model cfg/tiny-yolo-txt.cfg --load -1
./flow --model cfg/tiny-yolo-txt.cfg --load -1 --threshold 0.1 
