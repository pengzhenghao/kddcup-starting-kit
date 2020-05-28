time=$(date '+%Y-%m-%d_%H-%M-%S')
cd model
zip -r ../submission/submission_${time}.zip . -x '*.git*' -x '*__pycache__*'
