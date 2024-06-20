# Requires NVidia driver 531.41 on Windows https://www.nvidia.de/download/driverResults.aspx/200389/de which includes CUDA 12.1
# Does not work with newer NVidia drivers because PyTorch is not compatible with CUDA > 12.1.

FROM hilderonny2024/ubuntu22cuda121-python3

# https://techoverflow.net/2021/01/13/how-to-use-apt-install-correctly-in-your-dockerfile/
# https://docs.docker.com/build/building/best-practices/
# https://stackoverflow.com/a/74616730

ENV PYTHONDONTWRITEBYTECODE=1

RUN pip3 --no-cache-dir install \
    argostranslate \
    requests

# docker build -t hilderonny2024/ubuntu22cuda121-python3-argostranslate .