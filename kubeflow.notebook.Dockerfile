FROM public.ecr.aws/h3o0w0k1/jupyter-lab-notebook-cuda:latest
WORKDIR /
COPY environment.yml .
RUN conda env update -f environment.yml && \
    pip3 install kfp==1.8.2

CMD ["sh", "-c", \
     "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser \
      --allow-root --port=8888 --LabApp.token='' --LabApp.password='' \
      --LabApp.allow_origin='*' --LabApp.base_url=${NB_PREFIX}"]