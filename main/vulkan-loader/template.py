pkgname = "vulkan-loader"
pkgver = "1.3.262"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    f"-DVULKAN_HEADERS_INSTALL_DIR={self.profile().sysroot / 'usr'}",
    "-DBUILD_TESTS=OFF",  # needs gtest
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = [
    "vulkan-headers",
    "libxcb-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "wayland-devel",
]
pkgdesc = "Vulkan Installable Client Driver (ICD) loader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Loader/archive/v{pkgver}.tar.gz"
)
sha256 = "3bbaa5ee64058a89949eb777de66ce94bfe3141892514172cfc9451c756802d5"
# FIXME cfi
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]
