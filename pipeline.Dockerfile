FROM gpuci/miniconda-cuda:11.1-base-ubuntu20.04

WORKDIR /

COPY environment.yml .

RUN conda env update -n base -f environment.yml --prune \
    && pip install kfp==1.8.2 \
    && conda clean --all -y

COPY src /tmp

SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]