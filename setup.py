'''
The setup file is an esssential part of packaging and distributing python projects. It is used by setuptools
to define configuration of out project, such as its metadata, dependencies and more. 
'''

## find_packages scan all out folder and which all contains __int__.py consider that folder as a package
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
  '''
  This function returns list of requirements
  '''

  requirement_list:List[str]=[]
  try:
    with open('requirements.txt','r') as file:
      #Read lines from the file
      lines=file.readlines()
      #Process each line
      for line in lines:
        requirement=line.strip()
        ## ignore empty lines and -e .
        if requirement and requirement!='-e .':
          requirement_list.append(requirement)
  except FileNotFoundError:
    print("requirements.txt file not found")

  return requirement_list

print(get_requirements())

setup(
  name="NetworkSecurity",
  version="0.0.1",
  author="Anant Sureka",
  packages=find_packages(),
  intsall_requires=get_requirements()
)