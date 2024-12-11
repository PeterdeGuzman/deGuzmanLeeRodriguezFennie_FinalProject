
IMAGE_NAME = mystery-flask
DOCKER_ID_USER = kp14100164

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 8000:8000 $(IMAGE_NAME)

clean:
	docker rmi $(IMAGE_NAME)

image_show:
	docker images

container_show:
	docker ps

push:
	docker login
	docker tag $(IMAGE_NAME) $(DOCKER_ID_USER)/$(IMAGE_NAME)
	docker push $(DOCKER_ID_USER)/$(IMAGE_NAME):latest

login:
	docker login -u ${DOCKER_ID_USER}

# Make commands for GitHub Actions

install: 
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run tests in the main repository folder

test: 
	python -m pytest -vv mylib/test_*.py

# Format code in repository
format:
	black *.py

# Lint code in repository
lint:
	ruff check mylib/*.py 

# Lint Dockerfile 
container-lint:
	docker run --rm -i hadolint/hadolint < backend/Dockerfile

# All: Run all tasks
all: install lint test format deploy


# # Define the image name
# IMAGE_NAME = de_final_pjt
# DOCKER_ID_USER = kp14100164

# # Build the Docker image
# build:
# 	docker build -t $(IMAGE_NAME) .

# # Run the Docker container
# run:
# 	docker run -p 8000:8000 $(IMAGE_NAME)

# # run:
# # 	docker run -p 8000:80 $(IMAGE_NAME)

# # Remove the Docker image
# clean:
# 	docker rmi $(IMAGE_NAME)

# image_show:
# 	docker images

# container_show:
# 	docker ps

# push:
# 	docker login
# 	docker tag $(IMAGE_NAME) $(DOCKER_ID_USER)/$(IMAGE_NAME)
# 	docker push $(DOCKER_ID_USER)/$(IMAGE_NAME):latest

# login:
# 	docker login -u ${DOCKER_ID_USER}



# from Jeremy's repo
# install:
# 	pip install --upgrade pip &&\
# 		pip install -r requirements.txt

# test:
# 	python -m pytest -vv --cov=main --cov=mylib test_*.py

# format:	
# 	black *.py 

# lint:
# 	#disable comment to test speed
# 	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
# 	#ruff linting is 10-100X faster than pylint
# 	ruff check *.py 

# container-lint:
# 	docker run --rm -i hadolint/hadolint < Dockerfile

# refactor: format lint

# deploy:
# 	#deploy goes here
		
# all: install lint test format deploy

# generate_and_push:
# 	# Create the markdown file 
# 	python test_main.py  # Replace with the actual command to generate the markdown

# 	# Add, commit, and push the generated files to GitHub
# 	@if [ -n "$$(git status --porcelain)" ]; then \
# 		git config --local user.email "action@github.com"; \
# 		git config --local user.name "GitHub Action"; \
# 		git add .; \
# 		git commit -m "Add SQL log"; \
# 		git push; \
# 	else \
# 		echo "No changes to commit. Skipping commit and push."; \
# 	fi