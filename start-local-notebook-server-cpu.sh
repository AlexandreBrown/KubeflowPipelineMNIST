docker run --rm -p 8889:8888 \
                -v $(pwd)/notebooks:/home/jovyan/ \
                local-kubeflow-pipeline-mnist-notebook