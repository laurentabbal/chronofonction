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
    long_description=open('README.txt').read(),
)
