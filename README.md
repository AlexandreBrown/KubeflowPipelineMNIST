# KubeflowPipelineMNIST  
## Local setup
0. OPTIONAL : If you don't have docker installed, you can install it by running `./install-docker.sh`
### GPU
1. `./setup-nvidia-container-toolkit.sh`
2. `./build-local-notebook-server.sh`
3. `./start-local-notebook-server-gpu.sh`  
4. Access jupyter lab via `http://127.0.0.1:8889/lab?token=YOUR_TOKEN` where `YOUR_TOKEN` is the token created in step 4. (check the output from step 4 to know your token).
### CPU
1. `./build-local-notebook-server.sh`
2. `./start-local-notebook-server-cpu.sh`
3. Access jupyter lab via `http://127.0.0.1:8889/lab?token=YOUR_TOKEN` where `YOUR_TOKEN` is the token created in step 4. (check the output from step 4 to know your token).    
4. Access jupyter lab via `http://127.0.0.1:8889/lab?token=YOUR_TOKEN` where `YOUR_TOKEN` is the token created in step 4. (check the output from step 4 to know your token).  
### Result
![Result](https://i.ibb.co/tmpkXsX/Screenshot-from-2021-09-29-20-36-49.png)
