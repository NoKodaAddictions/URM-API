python3 setup.py sdist

python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*