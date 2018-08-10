from setuptools import find_packages, setup

setup(
    name="libthai-cffi",
    version="1.0.0",
    url="https://github.com/whs/libthai-cffi",
    author="Manatsawin Hanmongkolchai",
    author_email="manatsawin+pypi@gmail.com",
    description="CFFI Binding to libthai",
    license="LGPL",
    packages=find_packages(exclude=["test"]),
    setup_requires=["cffi~=1.11.5"],
    install_requires=["cffi~=1.11.5"],
    cffi_modules=["package/build_cffi.py:ffibuilder"],
)
