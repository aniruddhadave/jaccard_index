import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jaccard_index",
    version="0.0.3",
    author="Aniruddha Dave",
    author_email="aniruddhadave@gmail.com",
    description="Jaccard Index for Two Strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aniruddhadave/jaccard_index",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)