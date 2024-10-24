from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function is designed to read a list of requirements (like things you need to install for a project) from a file and
      return them as a list of strings.  

    '''
    requirements=[]                          # creates an empty list called requirements to hold the things it will read from the file.
    with open(file_path) as file_obj:        # It opens the file located at file_path
        requirements=file_obj.readlines()    # It reads all the lines in the file and stores them in the requirements list.
        requirements=[req.replace("\n","") for req in requirements] #read and removes any extra spaces or characters at the end of the lines.

        if HYPEN_E_DOT in requirements:      # Special item called HYPEN_E_DOT: If this item is found in the list, function removes it
            requirements.remove(HYPEN_E_DOT) # if '-e .' is present in req., then it will remove it 
    
    return requirements                      # Finally, the function gives back the cleaned-up list of requirements

# Setup has all the list of paramteters, this is also metadata information of entire project. 
setup(
name='myfirstmlproject',
version='0.0.1',
author='Bivor',
author_email='bb@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') # or you can add manually here. eg: ['pandas','numpy','seaborn']

)