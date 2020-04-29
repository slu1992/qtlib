import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qtlib", # Replace with your own username
    version="0.0.2",
    author="slu",
    author_email="1@slu1992.com",
    description="A library for quantitative trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slu1992/qtlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)