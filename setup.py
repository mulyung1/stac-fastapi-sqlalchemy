"""stac_fastapi: sqlalchemy module."""

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    desc = f.read()

install_requires = [
    "attrs",
    "pydantic",
    "stac_pydantic",
    "stac-fastapi.types==6.0.0",
    "stac-fastapi.api==6.0.0",
    "stac-fastapi.extensions==6.0.0",
    "sqlakeyset",
    "geoalchemy2",
    "sqlalchemy==1.3.23",
    "shapely",
    "psycopg2-binary",
    "alembic",
    "fastapi-utils",
    "typing_inspect",
]

extra_reqs = {
    "dev": [
        "httpx",  # for starlette's test client
        "orjson",
        "pystac[validation]",
        "pytest",
        "pytest-cov",
        "pre-commit",
        "requests",
        "twine",
        "wheel",
    ],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
    "server": ["uvicorn[standard]==0.35.0"],
}


setup(
    name="stac-fastapi.sqlalchemy",
    description="An implementation of STAC API based on the FastAPI framework.",
    long_description=desc,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="STAC FastAPI COG",
    author="Arturo Engineering",
    author_email="engineering@arturo.ai",
    url="https://github.com/stac-utils/stac-fastapi",
    license="MIT",
    packages=find_namespace_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
    entry_points={
        "console_scripts": ["stac-fastapi-sqlalchemy=stac_fastapi.sqlalchemy.app:run"]
    },
)
