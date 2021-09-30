# KubeflowPipelineMNIST  
## Local Jupyter Lap Setup
0. OPTIONAL : If you don't have docker installed, you can install it by running `./install-docker.sh`
### GPU
1. `./setup-nvidia-container-toolkit.sh`
2. `./build-local-notebook-server.sh`
3. `./start-local-notebook-server-gpu.sh`  
4. Access jupyter lab via `http://127.0.0.1:8889/lab?token=YOUR_TOKEN` where `YOUR_TOKEN` is the token created in step 3. (check the output from step 3 to know your token).
5. Inside jupyter lab, click File->New->Terminal
6. Clone this git repo (eg: `git clone https://github.com/AlexandreBrown/KubeflowPipelineMNIST.git`)
### CPU
1. `./build-local-notebook-server.sh`
2. `./start-local-notebook-server-cpu.sh`
3. Access jupyter lab via `http://127.0.0.1:8889/lab?token=YOUR_TOKEN` where `YOUR_TOKEN` is the token created in step 2. (check the output from step 2 to know your token).    
4. Inside jupyter lab, click File->New->Terminal
5. Clone this git repo (eg: `git clone https://github.com/AlexandreBrown/KubeflowPipelineMNIST.git`)
### Local Setup Result
![JupyterLabSetupResult](https://i.ibb.co/DtLWvRn/jupyter-lab.png)  
  
## Pipeline  
- Execute the cells from the notebook (see `/notebooks`)
- Upload the generated pipeline yaml file to the Kubeflow pipeline UI
### Pipeline Result  
![PipelineResult](https://i.ibb.co/mB6r2HD/pipeline-result.png)  
