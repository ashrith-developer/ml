from setuptools import find_packages,setup
from typing import List

h= "-e ."
def get_requirements(file)->List(str):
  """
  list oif requirements
  """
  requirements=[]
  with open(file) as f:
    requirements=f.readlines()
    [req.replace("\n"," ")for req in requirements]
    if h in requirements:
      requirements.remove(h)
  return requirements
    
setup (
name="ml",
version="0.0.1",
author="ashrith",
author_email="woonnaashrith@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)