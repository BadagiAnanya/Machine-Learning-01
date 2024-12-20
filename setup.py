from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip newlines and whitespace

        if '-e .' in requirements:  # Directly using '-e .'
            requirements.remove('-e .')

    return requirements

 
setup(
    name='Machine Learning Project',
    version='0.0.1',
    author='Ananya',
    author_email='ananya480badagi@gmail.com',  # Fixed spelling
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Dynamically fetch requirements
)
