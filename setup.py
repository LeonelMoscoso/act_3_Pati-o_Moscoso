from setuptools import setup, find_packages

setup(
    name="actividad_3",
    version="0.0.1",
    author="Leonel Moscoso patino Yovany",
    author_email="",
    description="",
    py_modules=["actividad_3"],
    install_requires=[
        "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "numpy",
        "openpyxl",
        "requests"
    ]
) 