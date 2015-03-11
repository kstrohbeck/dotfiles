import json
import os


class BaseInstaller:
    """
    Base class for the various dotfiles installers. Implements low-level file
    handling, without specifying what exactly gets installed. Also manages
    the .installed manifests.
    """

    def install(install_info):
        """Installs a set of files."""

        # If the matching install entry isn't in the manifest, add it.
        with open('.installed', 'rw') as installed_file:
            installed = json.load(installed_file)
            if not any(entry.path == install_info.path for entry in installed):
                installed.append(install_info)

        # For each file, install it.
        for file in self.files:
            pass
