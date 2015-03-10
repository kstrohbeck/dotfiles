import os


def get_redirect():
    """Get the redirect string that needs to be in the vimrc."""

    return 'source {base_path}{sep}vimrc\n'.format(
        base_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__))),
        sep = os.sep)


def is_installed(vimrc_path = '~/.vimrc'):
    """Check if the user already has this vimrc installed."""

    full_vimrc_path = os.path.abspath(os.path.expanduser(vimrc_path))

    # If the old vimrc already has our source string, 
    if os.path.exists(full_vimrc_path):
        with file(full_vimrc_path, 'r') as vimrc:
            content = vimrc.read()
            return get_redirect() in content

    return False


def install(vimrc_path = '~/.vimrc'):
    """Edit the user's local vimrc so that it sources the dotfiles vimrc."""

    full_vimrc_path = os.path.abspath(os.path.expanduser(vimrc_path))

    # Get the preexisting vimrc content.
    old_content = ''
    if os.path.exists(full_vimrc_path):
        with file(full_vimrc_path, 'r') as vimrc:
            old_content = vimrc.read()

    # Prepend the redirect info, then the other content (if any).
    with file(full_vimrc_path, 'w') as vimrc:
        vimrc.write(get_redirect() + old_content) 

    # Next, we have to get Vundle.


def uninstall():
    """Remove an install from the local vimrc."""
    pass


if __name__ == '__main__':
    if not is_installed():
        install()
