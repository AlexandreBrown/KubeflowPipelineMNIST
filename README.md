# KubeflowPipelineMNIST  
## Local setup
1. `./install-docker.sh`
2. `./setup-nvidia-container-toolkit.sh`
3. `./build-local-notebook-server.sh`
4. `./start-local-notebook-server.sh`
5. Access jupyter lab via `http://127.0.0.1:8889/lab?token=YOUR_TOKEN` where YOUR_TOKEN is the token create in step 4. (check the output from step 4 to know your token).