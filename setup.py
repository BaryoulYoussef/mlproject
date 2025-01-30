from setuptools import find_packages,setup
from typing import List 

HYPEN ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will reurn the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj : 
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        
        if HYPEN in requirements :
            requirements.remove(HYPEN)
    return requirements


setup(
name="mlproject",
version="0.0.1",
author="baryoul",
author_email="baryouly@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
