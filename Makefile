.PHONY: init shell remove

init:
	export PIPENV_VENV_IN_PROJECT=1 && \
	pipenv install --python 3.8 --dev

shell:
	pipenv shell

remove:
	pipenv --rm
