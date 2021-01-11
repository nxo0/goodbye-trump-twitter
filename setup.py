from setuptools import setup

def _ins_req():
    return open('requirements.txt').read().split('\n')

setup(
    install_requires=_ins_req(),
    )
