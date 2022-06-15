from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="dna-report",
    version="0.0.1",
    author="Philipp Kudrov",
    author_email="kudrovpn@yandex.com",
    description="Report handler electrophoresis-based genotyping systems",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/drPonihvost/dna-report-handler",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
