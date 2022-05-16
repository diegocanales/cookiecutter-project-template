FROM continuumio/miniconda3 as upstream

# Update, change owner
RUN groupadd -r conda --gid 900 \
    && chown -R :conda /opt/conda \
    && chmod -R g+w /opt/conda \
    && find /opt -type d | xargs -n 1 chmod g+s

FROM ubuntu:20.04
COPY --from=upstream /opt /opt/

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH=/opt/conda/bin:$PATH

# create user
ARG USERNAME=diego
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME


# install basic libs
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    build-essential \
    make \
    git \
    && apt-get upgrade -y \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate base" >> ~/.bashrc \
    && groupadd -r conda --gid 900 \
    && usermod -aG conda ${USERNAME} \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# set the user
USER $USERNAME

RUN conda install -c conda-forge mamba
WORKDIR /home/$USERNAME/envs
COPY environment.yaml environment.yaml
SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

RUN mamba env create -f environment.yaml

ENV SHELL /bin/bash

# activate {{ cookiecutter.conda_env }} environment
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
   && echo "conda activate {{ cookiecutter.conda_env }}" >> ~/.bashrc

WORKDIR /home/$USERNAME/workspace
