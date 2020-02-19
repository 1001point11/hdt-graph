import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hdtgraph",
    version="0.0.1",
    author="David Schaller",
    author_email="david@0x002A.com",
    description="Implementation of the dynamic graph data structure described by Holm, de Lichtenberg and Thorup in 2001 (HDT algorithm).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/david-schaller/hdt-graph",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
