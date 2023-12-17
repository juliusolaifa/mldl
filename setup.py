from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:

    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements=[line.strip() for line in file_obj.readlines() 
                      if not line.strip().startswith('-e ')]
    return requirements


setup(
    name='mldl',
    version='0.1',
    packages=find_packages(),
    description="""ML/DL Accelerator""",
    url='https://github.com/juliusolaifa/mldl',
    author='Julius Olaifa',
    author_email='jbolaifa@gmail.com',
    license='MIT',
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.8',
)
