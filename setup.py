from setuptools import setup, find_packages


HYPHEN_E_DOT='-e.'
def get_requirements(file_path):
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements :
            requirements.remove(HYPHEN_E_DOT)

    

setup(
name='mlproject',
version='0.0.1',
author='mahesh',
author_email='maheshkunjir12@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)