from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(name='nornir_pyez',
      version='0.0.1',
      description='PyEZs library and plugins for Nornir',
      url='https://github.com/DataKnox/nornir_pyez',
      author='Knox Hutchinson',
      author_email='knox@knoxsdata.com',
      license='MIT',
      packages=['nornir_pyez'],
      keywords=['ping', 'icmp', 'network'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: System Administrators',
          'Natural Language :: English'
      ],
      long_description=long_description,
      long_description_content_type='text/markdown',
      entry_points={  # Optional
          'nornir.plugins.connections': "pyez = nornir_pyez.plugins.connections:Pyez"
      },
      zip_safe=False)
