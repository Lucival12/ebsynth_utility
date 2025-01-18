import launch
import platform

def update_transparent_background():
    from importlib.metadata import version as meta_version
    from packaging import version

# Check if user is running an M1/M2 device and, if so, install pyvirtualcam, which is required for updating the transparent_background package
# Note that we have to directly install from source because the prebuilt PyPl wheel does not support ARM64 machines such as M1/M2 Macs
if platform.system() == "Darwin" and platform.machine() == "arm64":
    if not launch.is_installed("pyvirtualcam"):
        launch.run_pip("install git+https://github.com/letmaik/pyvirtualcam", "requirements for Ebsynth Utility")

if not launch.is_installed("IPython"):
    launch.run_pip("install ipython", "requirements for Ebsynth Utility")

if not launch.is_installed("seaborn"):
    launch.run_pip("install ""seaborn>=0.11.0""", "requirements for Ebsynth Utility")

if not launch.is_installed("color_matcher"):
    launch.run_pip("install color-matcher", "requirements for Ebsynth Utility")

