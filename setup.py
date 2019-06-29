from setuptools import setup

setup(
    name="switch-cluster-admin",
    version="0.1",
    py_modules=["switch_cluster"],
    install_requires=[
        "kubernetes",
        "Click",
    ],
    entry_points='''
        [console_scripts]
        switch-cluster=switch_cluster:cli
    ''',
)