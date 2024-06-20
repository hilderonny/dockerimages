# Requires NVidia driver 531.41 on Windows https://www.nvidia.de/download/driverResults.aspx/200389/de which includes CUDA 12.1
# Does not work with newer NVidia drivers because PyTorch is not compatible with CUDA > 12.1.

FROM hilderonny2024/ubuntu22cuda121-python3-argostranslate

# https://techoverflow.net/2021/01/13/how-to-use-apt-install-correctly-in-your-dockerfile/
# https://docs.docker.com/build/building/best-practices/
# https://stackoverflow.com/a/74616730

WORKDIR /app

ARG SOURCELANGUAGE=en
ARG TARGETLANGUAGE=de
ARG ARGOSPATH=/app/argosmodels

COPY argosupdate.py /app

RUN mkdir -p ${ARGOSPATH}/packages

RUN python3 argosupdate.py --argospath ${ARGOSPATH} --sourcelanguage ${SOURCELANGUAGE} --targetlanguage ${TARGETLANGUAGE}

# docker build -t hilderonny2024/ubuntu22cuda121-python3-argostranslate-en-de .