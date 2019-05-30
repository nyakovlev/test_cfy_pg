from setuptools import setup

setup(
    name='test-plugin',
    version="1.0",
    author="niouk",
    packages=["wk"],
    install_requires=["cloudify-plugins-common>=3.3"]
)
