default: install
upload:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
install:
	python3 setup.py install
