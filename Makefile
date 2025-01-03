default: install

upload:
	rm -rf dist build *.egg-info
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

install:
	python3 setup.py install
