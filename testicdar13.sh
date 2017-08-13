module purge
module load cuda/8.0.44 cudnn Anaconda/2.3.0
source activate tfcv
./flow --model cfg/tiny-yolo-txt.cfg --load -1 --threshold 0 
