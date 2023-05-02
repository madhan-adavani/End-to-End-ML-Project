from setuptools import find_packages,setup


def get_requirements(file_path:str):
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    return requirements

setup(
name='EndToEndMLProject',
version='0.1',
author='madhan-adv',
author_email='madhan.adavani96@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)