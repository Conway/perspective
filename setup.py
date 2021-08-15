import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="perspective",
    version="1.0.0",
    author="Jake Conway",
    author_email="jake.h.conway@gmail.com",
    description="A package for interacting with the Perspective API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/conway/perspective",
    project_urls={
        "Bug Tracker": "https://github.com/conway/perspective/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir=setuptools.find_packages(exclude=['tests']),
    packages=['perspective'],
    python_requires=">=3.8",
)
