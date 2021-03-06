FROM public.ecr.aws/h3o0w0k1/jupyter-lab-notebook-cuda:latest
WORKDIR /
COPY environment.yml .
RUN conda env update -f environment.yml \
    && pip install kfp==1.8.2 \
    && conda clean --all -y

CMD ["sh", "-c", \
     "jupyter lab --notebook-dir=/home/jovyan \
     --ip 0.0.0.0 \
     --port 8888 \
     --no-browser \
     --allow-root \
     --NotebookApp.iopub_data_rate_limit=1.0e10"]