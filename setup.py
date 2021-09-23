setup(
    name="chronocode",
    version="0.0.1",
    description="Module Chronocode",
    long_description=parent_dir.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/laurentabbal/module-chrono",
    author="xxx",
    author_email="xxx@gmail.com",
    license="MIT License",
    packages=find_packages(exclude=("assets", "notebooks", "prints", "script")),
    install_requires=parent_dir.joinpath("requirements.txt").read_text().splitlines(),
    classifiers=[
        "Intended Audience :: Science/Research",
    ],
)

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='chronofonction',
    url='https://github.com/laurentabbal/chronofonction',
    author='Laurent Abbal',
    author_email='laurent@abbal.com',
    # Needed to actually package something
    packages=['chronofonction'],
    # Needed for dependencies
    install_requires=['time'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Mesure du temps d\'execution d\'une fonction',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
