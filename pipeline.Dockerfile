FROM gpuci/miniconda-cuda:11.1-runtime-ubuntu20.04

WORKDIR /

COPY environment.yml .
COPY src .

RUN conda env update -n base -f environment.yml --prune && \
    pip3 install kfp==1.8.2

SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]