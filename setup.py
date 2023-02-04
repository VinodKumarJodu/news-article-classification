from setuptools import setup, find_packages
from typing import List

FILE_PATH = "/home/v/news-article-classification/requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    """This Function returns list of requirements from the requirements file"""
    requirements_list = []
    with open(FILE_PATH, "r") as f:
        requirements = f.readlines()
        requirements_list = [requirement.strip() for requirement in requirements if requirement.strip() != HYPHEN_E_DOT]
    return requirements_list
# def get_requirements():
#     with open(FILE_PATH, 'r') as file:
#         requirements = [line.strip() for line in file if line.strip() and line.strip() != "-e ."]
#     return requirements

# def get_requirements():
#     requirements = []
#     with open(FILE_PATH, 'r') as file:
#         for line in file:
#             requirement = line.strip()
#             if requirement and requirement != "-e .":
#                 requirements.append(requirement)
#     return requirements

# def get_requirements()-> List[str]:
#     """This Function returns list of requirements from the requirements file"""
#     requirements_list = []
    
#     with open(FILE_PATH,"r") as f:
#         requirements = csv.reader(f)
#         requirements_list = [requirement[0].strip() for requirement in requirements]
#         if HYPHEN_E_DOT in requirements_list:
#             requirements_list.remove(HYPHEN_E_DOT)            
#         return requirements_list

setup(
    name="news article classification",
    version="0.0.1",
    author="Vinod Kumar Jodu",
    author_email="vinodkumarjodu@gmail.com",
    description='Classify news articles based on their content',
    packages=find_packages(),
    install_requires=get_requirements()
)
