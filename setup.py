from setuptools import find_packages, setup

setup(
    name="discussion-board",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.12",
    install_requires=[
        "Flask>=3.0.0",
        "PyMySQL>=1.1.0",
        "gunicorn>=21.2.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
        ],
    },
)