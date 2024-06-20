# Docker images

This repository contains the Dockerfiles for all Docker Hub images provided by
[hilderonny2024](https://hub.docker.com/u/hilderonny2024).

## ubuntu22cuda121-python3

Based on Ubuntu 22.04 with NVidia CUDA 12 libraries
`nvidia/cuda:12.1.0-base-ubuntu22.04`.
Additionally installed Python 3 (3.10) and PyTorch with CUDA 12 support.

Used as base image for AI and LLM applications.

Requires NVidia driver 531.41 on Windows https://www.nvidia.de/download/driverResults.aspx/200389/de which includes CUDA 12.1.
Does not work with newer NVidia drivers because PyTorch is not compatible with CUDA > 12.1.

To test the functionality of the GPUs you can run:

```sh
docker run --gpus all hilderonny2024/ubuntu22cuda121-python3 python3 -c "import torch;print(torch.cuda.is_available())" && nvidia-smi
# You should see a "True" in the first line and a table with NVidia driver information
```

## ubuntu22cuda121-python3-argostranslate

Based on `hilderonny2024/ubuntu22cuda121-python3`.
Additionally installed python packages `argostranslate` (includes `ctranslate2`)
and `requests`.

Used as base image for translation apps.

Requires NVidia driver 531.41 on Windows https://www.nvidia.de/download/driverResults.aspx/200389/de which includes CUDA 12.1.
Does not work with newer NVidia drivers because PyTorch is not compatible with CUDA > 12.1.

## ubuntu22cuda121-python3-argostranslate-en-de

Based on `hilderonny2024/ubuntu22cuda121-python3-argostranslate`.
Installs a translation model for translating from english (en) to german (de).

Used as base image for english-german translation apps.

Requires NVidia driver 531.41 on Windows https://www.nvidia.de/download/driverResults.aspx/200389/de which includes CUDA 12.1.
Does not work with newer NVidia drivers because PyTorch is not compatible with CUDA > 12.1.

# Building

```sh
docker build -t hilderonny2024/ubuntu22cuda121-python3 ubuntu22cuda121-python3
docker build -t hilderonny2024/ubuntu22cuda121-python3-argostranslate ubuntu22cuda121-python3-argostranslate
docker build -t hilderonny2024/ubuntu22cuda121-python3-argostranslate-en-de ubuntu22cuda121-python3-argostranslate-en-de
```