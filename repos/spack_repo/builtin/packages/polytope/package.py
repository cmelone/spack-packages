# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Polytope(CMakePackage):
    """A library for generating Voronoi and Voronoi-like tessellations for
    computational domains with nontrivial boundaries."""

    homepage = "https://github.com/LLNL/polytope"
    git = "https://github.com/LLNL/polytope.git"

    license("BSD-3-Clause")

    version("main", branch="main")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.1:", type="build")

    variant("shared", default=False, description="Build shared libraries")
    variant("boost", default=True, description="Enable Boost Voronoi tessellator")
    variant("python", default=False, description="Build Python bindings")
    variant("silo", default=False, description="Enable Silo I/O support")
    variant("header_only", default=False, description="Install headers only, skip library build")

    depends_on("boost@1.50:", when="+boost")
    depends_on("python@3:", type=("build", "link", "run"), when="+python")
    depends_on("py-pybind11", type="build", when="+python")
    depends_on("hdf5", when="+silo")
    depends_on("silo", when="+silo")
    depends_on("zlib-api", when="+silo")

    def patch(self):
        # CMakeLists.txt hard-codes C++11 via set(); boost geometry headers
        # require C++14 in modern Boost releases, so bump the standard.
        filter_file(
            r"set\(CMAKE_CXX_STANDARD 11\)",
            "set(CMAKE_CXX_STANDARD 14)",
            "CMakeLists.txt",
        )

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("USE_BOOST", "boost"),
            self.define_from_variant("USE_PYTHON", "python"),
            self.define_from_variant("USE_SILO", "silo"),
            self.define_from_variant("HEADER_ONLY", "header_only"),
            self.define("USE_MPI", False),
        ]
        return args
