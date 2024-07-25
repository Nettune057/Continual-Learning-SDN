# Makefile for common tasks

ENV_FILE=.env
VENV_DIR=CL
REQ_FILE=requirements.txt
# Export environment variables from .env file
# export $(shell grep -v '^#' $(ENV_FILE) | xargs)

# Create a conda environment
venv:
	python -m venv $(VENV_DIR)

# Install Python dependencies in the virtual environment
install_deps: venv
	$(VENV_DIR)\Scripts\activate && pip install -r $(REQ_FILE)

# Run unit tests in the virtual environment
test:
	$(VENV_DIR)\Scripts\activate && pytest tests/

# Build Docker image
docker_build:
	docker build -t $(DOCKER_IMAGE) -f docker/Dockerfile .

# Run Docker container
docker_run:
	docker run -it --rm -p 8888:8888 --name $(DOCKER_CONTAINER) --env-file $(ENV_FILE) $(DOCKER_IMAGE)

# Clean up Docker image
docker_clean:
	docker rmi $(DOCKER_IMAGE)

# Jupyter Notebook
notebook:
	$(VENV_DIR)\Scripts\activate && jupyter notebook

# Clean the environment
clean:
	rm -rf __pycache__ */__pycache__
	rm -rf .ipynb_checkpoints

.PHONY: venv install_deps test docker_build docker_run docker_clean notebook clean