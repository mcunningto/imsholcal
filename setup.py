from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='imsholcal',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pandas', 'requests'],
    include_package_data=True,
    url='https://github.com/mcunningto/imsholcal',
    license='MIT',
    author='mcunningto',
    author_email='mcunningto@gmail.com',
    description='business day offset function with custom exchange based holiday calendar',
    long_description=long_description,
    long_description_content_type='text/x-rst'
)
