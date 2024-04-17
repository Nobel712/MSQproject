from setuptools import  find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Nobel',
    author_email='smnuruzzaman712@gmail.com',
    intall_requires=['openai','langchain','streamlit','python-dotenv','pyPDF2'],
    packages=find_packages()
)