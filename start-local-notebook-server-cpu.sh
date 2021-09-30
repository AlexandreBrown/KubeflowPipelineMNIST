docker run --rm -p 8889:8888 \
                -v $(pwd)/notebook-env:/home/jovyan/ \
                local-kubeflow-pipeline-mnist-notebook