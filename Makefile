default: install

upload:
	rm -rf dist build *.egg-info
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

install:
	python3 setup.py install

osx_pack:
	pyinstaller --onefile --name pyrc4 rc4/__init__.py
	chmod +x ./dist/pyrc4
	tar -czvf rc4-macos.tar.gz ./dist/pyrc4
