PYTHON = python
SETUP = $(PYTHON) setup.py
RUNTESTS = PYTHONHASHSEED=random PYTHONPATH=.:$(PYTHONPATH) nosetests $(TEST_OPTIONS)

build::
	$(SETUP) build
	$(SETUP) build_ext -i

check:: build
	$(RUNTESTS) tests/
