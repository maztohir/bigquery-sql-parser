build:
	python3 setup.py bdist_wheel --universal

# Upload to PyPI
upload:
	twine upload dist/*

# Upload to test PyPI
upload_test:
	twine upload -r testpypi dist/*