export PYTHONPATH=$PYTHONPATH:`pwd`
CUDA_VISIBLE_DEVICES=0 python3 tools/train_net.py --num-gpus 1 \
        --config-file configs/fcos/fcos_imprv_R_101_FPN.yaml \
        --eval-only MODEL.WEIGHTS /home/zjrandom/Projects/BCNet/output/model_0129999.pth 2>&1 | tee log/test_log.txt
