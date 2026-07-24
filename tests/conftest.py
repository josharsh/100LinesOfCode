"""Shared pytest helpers.

The projects in this repository are standalone scripts living in directories
whose names contain spaces and are not importable as normal Python packages.
`load_module` loads any of them from its path so they can be unit tested.
"""
import importlib.util
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_module(relative_path, module_name):
    """Load a module from a path relative to the repository root."""
    path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        raise ImportError(f"Could not load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
