import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RawProc",
    version="0.0.1",
    author="Aleksey Kuchkov",
    author_email="biblbroxxx@gmail.com",
    description="RAW image converter",
    long_description=long_description,
    url="https://github.com/Biblbrox/RawConverter",
    packages=["RawProc"],
    scripts=['./scripts/rawproc'],
    depency_links=["https://github.com/letmaik/rawpy"],
    install_requires=[
        'numpy',
        'cython',
        'imageio'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
