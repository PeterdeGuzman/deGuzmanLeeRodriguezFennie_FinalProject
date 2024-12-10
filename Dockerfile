# Stage 1: Build environment
FROM python:3.9-slim-bullseye AS build-env

# Install required tools and dependencies
RUN apt-get update && apt-get -y install --no-install-recommends \
    python3-venv gcc git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up arguments and environment variables
ARG VENV_PATH="/opt/venv"
ENV VENV_PATH=${VENV_PATH}
ENV PATH="${VENV_PATH}/bin:$PATH"

# Copy dependencies
COPY requirements.txt /tmp/

# Set up virtual environment, upgrade pip, and install dependencies
RUN python3 -m venv $VENV_PATH \
    && ${VENV_PATH}/bin/pip install --upgrade pip \
    && ${VENV_PATH}/bin/pip install --no-cache-dir -r /tmp/requirements.txt \
    && ${VENV_PATH}/bin/pip install git+https://github.com/google/generative-ai-python

# Stage 2: Runtime environment
FROM python:3.9-slim-bullseye

# Copy virtual environment and project files
WORKDIR /deGuzmanLeeRodriguezFennie_FinalProject
COPY . /deGuzmanLeeRodriguezFennie_FinalProject

# # Copy virtual environment and project files
# COPY --from=build-env /opt/venv /opt/venv
# WORKDIR /workspace
# COPY app.py /workspace
# COPY mylib/ /workspace/mylib
# COPY templates/ /workspace/templates
# COPY static/ /workspace/static

# Set PATH for the virtual environment
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/workspace/mylib:$PYTHONPATH"

# Run the application
CMD ["python3", "app.py"]



# # Stage 1: Build environment
# FROM python:3.8-slim-bullseye AS build-env

# # Install required tools
# RUN apt-get update --allow-releaseinfo-change && apt-get -y install --no-install-recommends \
#     python3-venv \
#     gcc \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # Set up arguments and environment variables
# ARG USER="codespace"
# ARG VENV_PATH="/home/${USER}/venv"
# ENV VENV_PATH=${VENV_PATH}
# ENV PATH="${VENV_PATH}/bin:$PATH"

# # Copy dependencies
# COPY requirements.txt /tmp/
# COPY Makefile /tmp/

# # Set up virtual environment and install dependencies
# RUN python3 -m venv $VENV_PATH \
#     && ${VENV_PATH}/bin/pip install --disable-pip-version-check --no-cache-dir -r /tmp/requirements.txt \
#     && rm -rf /tmp/requirements.txt

# # Stage 2: Distroless runtime
# FROM gcr.io/distroless/python3

# # Copy virtual environment from build stage
# COPY --from=build-env /home/codespace/venv /home/codespace/venv

# # Copy project files
# WORKDIR /workspace
# COPY . /workspace

# # Set PATH for the virtual environment
# ENV PATH="/home/codespace/venv/bin:$PATH"

# # Run the application
# CMD ["python3", "/workspace/app.py"]



# # See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/codespaces-linux/.devcontainer/base.Dockerfile

# FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal

# # [Optional] Uncomment this section to install additional OS packages.
# # RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
# #     && apt-get -y install --no-install-recommends <your-package-list-here>
# RUN apt-get update && apt-get -y install --no-install-recommends \
#    python3.8-venv \
#    gcc 
   
# ARG USER="codespace"
# ARG VENV_PATH="/home/${USER}/venv"
# COPY requirements.txt /tmp/
# COPY Makefile /tmp/
# RUN su $USER -c "/usr/bin/python3 -m venv /home/${USER}/venv" \
#    && su $USER -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
#    && rm -rf /tmp/requirements.txt 