import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bigquery-sql-parser",
    version="0.1.4",
    author="Muhamad Tohir",
    author_email="maztohir@gmail.com",
    description="Simple and out of the box Bigquery SQL Parser for python. Convert your SQL into python object which you can modify programatically.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maztohir/bigquery-sql-parser",
    project_urls={
        "Bug Tracker": "https://github.com/maztohir/bigquery-sql-parser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)