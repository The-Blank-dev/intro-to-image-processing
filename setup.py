import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_package-the-Blank-dev", # Replace with your own username
    version="0.0.1",
    author="Ashwamegh_Rathore",
    author_email="ashwameghrathorejsr@iitkgp.ac.in",
    description="Assignment3_19CS30009",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)