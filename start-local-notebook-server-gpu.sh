docker run --rm -p 8889:8888 \
                -v $(pwd)/notebooks:/home/jovyan/ \
                --gpus all local-kubeflow-pipeline-mnist-notebook