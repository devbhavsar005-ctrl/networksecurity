"""
this setup.py file is very important for any project.
 It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
"""

from setuptools import find_packages,setup
from typing import List 

def get_requirements()->List[str]:
    " Thiss function will return list of requirements"

    requirement_list:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement !="-e .":
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")

setup(
    name="Network security",
    version="0.0.1",
    author="Bhavsar Dev",
    author_email="devbhavsar005@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements()
)        
