from setuptools import find_packages, setup
from typing import List
import csv

REQUIREMENTS_FILE = "/config/workspace/requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()-> List[str]:
    """This Function returns list of requirements from the requirements file"""
    requirements_list = []
    
    with open(REQUIREMENTS_FILE,"r") as f:
        requirements = csv.reader(f)
        requirements_list = [requirement[0] for requirement in requirements]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
        return requirements_list

setup(
      name="news article classification",
      version="0.0.1",
      author="Vinod Kumar Jodu",
      author_email="vinodkumarjodu@gmail.com",
      find_packages=find_packages(include=['source', 'notebooks']),
      install_requires=get_requirements()
)