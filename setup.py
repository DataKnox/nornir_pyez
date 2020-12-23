import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

setuptools.setup(name='nornir_pyez',
                 version='0.0.10',
                 description='PyEZs library and plugins for Nornir',
                 url='https://github.com/DataKnox/nornir_pyez',
                 packages=setuptools.find_packages(),
                 author='Knox Hutchinson',
                 author_email='knox@knoxsdata.com',
                 license='MIT',
                 keywords=['ping', 'icmp', 'network'],
                 classifiers=[
                     'Development Status :: 5 - Production/Stable',
                     'Intended Audience :: System Administrators',
                     'Natural Language :: English'
                 ],
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 install_requires=INSTALL_REQUIRES,
                 entry_points={
                     'nornir.plugins.connections': "pyez = nornir_pyez.plugins.connections:Pyez"
                 },
                 zip_safe=False)
