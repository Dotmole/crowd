import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'pyfacy_dlib_models',
    'imutils',
    'dlib>=19.7',
    'numpy',
    'scipy',
    'sklearn'
]


setuptools.setup(
    name="crowd",
    version="0.1",
    author="Shravankumar Shetty",
    author_email="socialmedia@dotmole.co",
    description="Face Clustering with Deep Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dotmole/crowd",
    packages=[
        'crowd',
    ],
    package_dir={'crowd': 'crowd'},
    package_data={
        'crowd': ['face_clust/*.py']
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pyfacy',
    classifiers=(
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
