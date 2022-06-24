#python3 setup.py build develop #--no-deps
# export PYTHONPATH=$PYTHONPATH:`pwd`
# export CUDA_LAUNCH_BLOCKING=1 # for debug

# conda activate bcnet
# cd Projects/BCNet

CUDA_VISIBLE_DEVICES=0 python3 demo/demo.py --config-file configs/fcos/fcos_imprv_R_101_FPN.yaml \
  --input 'test_img/' \
  --output 'result_img/' \
  --opts MODEL.WEIGHTS /home/zjrandom/BCNet/models/model_0001999.pth

