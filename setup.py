import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setuptools.setup(
    name="scienlib", 
    version="1.0",
    author="dylan14567",
    author_email="",
    description="scienlib is a scientific python library that adds math functions and adds other functions such as physics",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dylan14567/scienlib",
    project_urls={
        "Bug Tracker": "https://github.com/dylan14567/scienlib/issues",
        "Documentation": "https://dylan14567.github.io/2021/04/28/scienlib-documentation.html",
    },
    install_requires=[
        "wheel",
        "requests",
        "python-nmap",
        "speedtest-cli",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="server",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
)
