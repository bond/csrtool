# csrtool
python version of gen-csr (Ruby version available at github.com/bond/gen-csr).

## Installation
Can be installed from PyPi: `pip install csrtool`

## Usage
First domain is used as Common-name in addition to DNS-name: `csr --org MyOrg my.org www.my-org`

For more help: `csr --help`

## Development
To test the development version use command in repository dir: `pip install -e $(pwd)`

Pull requests are welcome :)

### Uploading package
Uploading package to PyPi

- Build package for upload: `python setup.py bdist_wheel`
- Upload package: `twine upload dist/package-version.whl`
