from setuptools import setup

setup(
    name="clustercli",
    version="0.1",
    py_modules=["cluster_cli"],
    install_requires=[
        "kubernetes",
        "Click",
    ],
    entry_points='''
        [console_scripts]
        clustercli=cluster_cli:cli
    ''',
)