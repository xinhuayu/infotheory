import os
import sys
from distutils.core import setup, Extension
from infotheory.infotools import __version__

package_name = "infotheory"
readme = "README.md"
license = "LICENSE"

long_description = """# Package for Mulativariate Information theoretic analyses

## Website and docs

https://github.com/madvn/infotheory"""

# MacOS
# export CXXFLAGS="-mmacosx-version-min=10.9"
# export LDFLAGS="-mmacosx-version-min=10.9"

extra_compile_args = []
if sys.platform == "darwin":
    extra_compile_args = ["-stdlib=libc++", "-mmacosx-version-min=10.9", "-v"]

# python pip installation LINK2001 error: "PyInit_infotheoryClass" not found 
# fixed an error here, changing "infotheory" to "InfoTools" in the setup.py to match the actual class in CPP and header file
# not sure if it actually fixed the compliation error, but successfully installed 
info_ext_module = Extension(
    "InfoTools",
    sources=[os.path.join("./", package_name, "PyLinker.cpp")],
    # language = "c++",
    extra_compile_args=extra_compile_args,
)

setup(
    name=package_name,
    version=__version__,
    description="Information theoretic analysis tools",
    author="Madhavun Candadai and Eduardo J. Izquierdo",
    author_email="madvncv@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mcandadai.com/infotheory/",
    packages=[package_name],
    ext_modules=[info_ext_module],
)
