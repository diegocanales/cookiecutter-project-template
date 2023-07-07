DOCKER_IMAGE = {{ cookiecutter.docker_image }}
DEV_CONTAINER_NAME = {{ cookiecutter.docker_image }}_dev
CONDA_ENV_NAME = {{ cookiecutter.conda_env }}
PACKAGE_NAME = {{ cookiecutter.package_name }}

define VSCODE_SETTINGS
{\n
\t"python.defaultInterpreterPath": "$(shell dirname $(shell dirname $(shell which conda)))/envs/$(CONDA_ENV_NAME)/",\n
\t"python.linting.pylamaEnabled": true,\n
\t"python.linting.pylamaPath": "$(shell dirname $(shell dirname $(shell which conda)))/envs/$(CONDA_ENV_NAME)/bin/pylama",\n
\t"python.formatting.provider": "autopep8",\n
\t"python.formatting.autopep8Path": "$(shell dirname $(shell dirname $(shell which conda)))/envs/$(CONDA_ENV_NAME)/bin/autopep8",\n
\t"editor.rulers": [80,120],\n}\n
endef

define TAGS_COMMITS_MSG
Format -> git commit -m "<TAG>: <COMMIT DESCRIPTION>"\n\n
- feat: a new feature.\n
- fix: a bug fix.\n
- docs: changes to documentation.\n
- data: data transformations or adding (DVCs repos).\n
- style: formatting, missing semi colons, etc; no code change.\n
- refactor: refactoring production code.\n
- test: adding tests, refactoring test; no production code change.\n
- chore: updating build tasks, package manager configs, etc; no production code change.\n
- env: update conda environment, requirements.txt, dockerfile.\n
- clean: remove unused files.\n
endef

PACKAGE_MANAGER = conda
ifeq (,$(shell which mamba))
	PACKAGE_MANAGER = conda
else
	PACKAGE_MANAGER = mamba
endif

.PHONY: help
help: ## List the command help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/:.*##/ ->/'

.PHONY: env
env: ## Create/update the environment.
ifeq (base,$(CONDA_DEFAULT_ENV))
	$(PACKAGE_MANAGER) env update -f environment.yaml --prune
	@echo "!!!RUN THE conda activate COMMAND ABOVE RIGHT NOW!!!"
else
	@echo "Activate the base environment: conda activate base"
endif

.PHONY: env-rm
env-rm: ## Remove the environment.
ifeq (base,$(CONDA_DEFAULT_ENV))
	$(PACKAGE_MANAGER) env remove --name $(CONDA_ENV_NAME)
else
	@echo "Activate the base environment: conda activate base"
endif

.PHONY: env-f
env-f: env-rm env ## Remove and create the environment.

.PHONY: docs-clean
docs-clean: ## Clean the documentation folders.
	rm -drf docs/html/
	rm -f docs/source/notebooks/*.ipynb
	rm -f docs/source/api/*

.PHONY: docs-nb
docs-nb: ## Add notebooks to documentation folder.
	cp notebooks/**.ipynb docs/source/notebooks/
	sed -i 6q docs/source/notebooks/index.rst
	ls -1 docs/source/notebooks/ | grep .ipynb | sed -e 's/\.ipynb$$//' | sed -e 's/^/   /' >> docs/source/notebooks/index.rst

.PHONY: docs-api
docs-api: ## Creates the package documentation.
	sphinx-apidoc -f --separate --doc-project "Python API Reference" --tocfile "index" -o docs/source/api . setup.py --ext-viewcode --ext-todo --ext-autodoc

.PHONY: docs-build
docs-build: ## Build the HTML documentation files.
	sphinx-build -b html docs/source docs/html/

.PHONY: docs
docs: docs-clean docs-api docs-nb docs-build  ## Create the Sphinx documentation.
	echo "Build finished"

.PHONY: docs-serve
docs-serve: ## Serve the documentation and rebuilt on changes.
	sphinx-autobuild docs/source/ docs/html --watch $(PACKAGE_NAME) --pre-build 'sphinx-apidoc -f --separate --doc-project "Python API Reference" --tocfile "index" -o docs/source/api . setup.py --ext-viewcode --ext-todo  --ext-autodoc --extensions "sphinx.ext.autosummary"'

export VSCODE_SETTINGS
.PHONY: vscode-settings
vscode-settings: ## Create the base VSCode settings file.
	mkdir -p .vscode/
	echo $${VSCODE_SETTINGS} > .vscode/settings.json

.PHONY: image
image: ## Create the docker image.
	docker build -f Dockerfile -t $(DOCKER_IMAGE) .

.PHONY: container
container: image ## Run the docker container.
	docker run --rm -it -p 8888:8888 $(DEV_CONTAINER_NAME) conda run --no-capture-output -n $(DOCKER_IMAGE) /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8888 --allow-root"

export TAGS_COMMITS_MSG
.PHONY: tags-commits
tags-commits: ## Tags commits reminder.
	@echo $${TAGS_COMMITS_MSG}

