docker run --rm -p 8889:8888 -v $(pwd)/notebooks:/home/jovyan/work/ --gpus all local-kubeflow-pipeline-mnist-notebook