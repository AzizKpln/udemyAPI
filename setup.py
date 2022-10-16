from setuptools import setup,find_packages


setup(
    name="udemyAPI",
    version="0.0.1",
    packages=find_packages(),
    url="https://github.com/AzizKpln/udemyAPI",
    license="MIT license",
    author="Aziz Kaplan",
    author_email="AzizKpln@protonmail.com",
    description="You can find everything you need in README.MD",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7, <4",
    install_requires=["playwright"],
    classifiers=[ 
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
)