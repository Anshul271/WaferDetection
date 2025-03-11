from setuptools import find_packages,setup
# A setuptools is a package that mainly provides setup for python package(to build and distribute packages)
from typing import List
Hypen_E_Dot="-e."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements
    
setup(
    name='Fault_detection',
    version='0.0.1',
    author='Anshul',
    author_email='sonakiyaanshul1127gmblast@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)
# artifacts-->output of ML pipeline