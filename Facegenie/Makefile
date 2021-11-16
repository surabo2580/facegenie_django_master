CONDA_NAME := facegenie_dynamic_master
PYTHON_VERSION := 3.8

DOCKER_TAG := facegenie_dynamic_master

build-docker:
	docker build . -t $(DOCKER_TAG)

run-docker:
	docker run --gpus all -it --rm -d -p 50001:50001 --name facegenie_dynamic_master $(DOCKER_TAG)

# create-conda:
# 	conda env create -f environment.yml -n $(CONDA_NAME)

# delete-conda:
# 	conda env remove -y -n $(CONDA_NAME)