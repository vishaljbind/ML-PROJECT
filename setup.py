from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path: str) -> List[str]:
    ''' this function returns a list of'''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name='dsproject',
    version='1.0.0',
    description='A package for handling data in a database',
    author='Vishal',
    author_email="vishaljbind@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)