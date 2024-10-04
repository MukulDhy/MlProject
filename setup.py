from setuptools import find_packages,setup

HYPHEN =  "-e ."
def get_requirements(name) :
    all_lib = []
    with open(name,'r') as file:
        for line in file:
            line = line.replace('\n','')
            all_lib.append(line)
        
    if HYPHEN in all_lib :
        all_lib.remove(HYPHEN)
    return all_lib
setup(
    name="MlProject",version="0.0.1",
    author="Mukul Dahiya", author_email="1029mukul38@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt") 
    )


