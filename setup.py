import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bigquery-sql-parser",
    version="0.1.4",
    author="Muhamad Tohir",
    author_email="maztohir@gmail.com",
    description="Python library to work with complicated nested dict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maztohir/python-nested-dict",
    project_urls={
        "Bug Tracker": "https://github.com/maztohir/python-nested-dict/issues",
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