import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TinyAPI",
    version="0.1",
    author="TinyAPI",
    author_email="email@xarty.xyz",
    description="A fast and lightweight WSGI Framework for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xArty4/tinyapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
        "Operating System :: MacOS",
        "Operating System :: Unix",
    ],
    install_requires=['urllib3','python-multipart','mako'],
    packages=setuptools.find_packages('.'),
    python_requires=">=3.6",
)
