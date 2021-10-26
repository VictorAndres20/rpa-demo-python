from setuptools import setup

setup(
    name="rpa",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Real Python",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["src/tests"],
    include_package_data=True,
    install_requires=[
        "rpaframework"
    ],
    entry_points={"console_scripts": ["__main__"]},
)