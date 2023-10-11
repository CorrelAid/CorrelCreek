from setuptools import find_packages, setup

setup(
    name="creek_control",
    packages=find_packages(exclude=["creek_control_tests"]),
    install_requires=[
        "dagster",
        "dagster-meltano"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
