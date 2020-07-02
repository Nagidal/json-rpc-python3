from setuptools import setup
from setuptools import find_packages
import pathlib
import re


with open(pathlib.Path.cwd() / "README.md", encoding="utf-8") as file:
    long_description = file.read()


def get_property(property: str, path_to_init_file: pathlib.Path) -> str:
    """
    Reads a property from the project's __init__.py
    e.g. get_property("__version__" path_to_init_file) -> "1.2.3"
    """
    regex = re.compile(r"{}\s*=\s*[\"'](?P<value>[^\"']*)[\"']".format(property))
    try:
        with open(path_to_init_file) as initfh:
            try:
                result = regex.search(initfh.read()).group("value")
            except AttributeError:
                result = None
    except FileNotFoundError:
        result = None
    return result


project_name = "rdoclient"
package_root = "src"
path_to_init_file = pathlib.Path.cwd() / package_root / project_name / "__init__.py"


setup(
        name = project_name,
        version = get_property("__version__", path_to_init_file),
        description = f"RANDOM.ORG JSON-RPC API (Release {get_property('__release__', path_to_init_file)}) implementation.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author=get_property("__author__", path_to_init_file),
        author_email=get_property("__author_email__", path_to_init_file),
        classifiers=[
                     "Development Status :: 3 - Alpha",
                     "Intended Audience :: Developers",
                     "Topic :: Software Development :: Libraries :: Python Modules",
                     "License :: OSI Approved :: MIT License",
                     "Programming Language :: Python :: 3.8",
                    ],
        keywords = "RANDOM.ORG random client implementation",
        url = "http://packages.python.org/rdoclient_py38",
        download_url = "https://github.com/Nagidal/rdoclient_py38",
        # packages=['rdoclient'],
        package_dir = {"": package_root},
        packages=find_packages(where=package_root),
        package_data={},
        python_requires=">=3.8",
        install_requires=["requests"],
        entry_points = {},
        platforms=["Windows", "Linux"],
     )
