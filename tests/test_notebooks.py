#!/usr/bin/env python3
"""
Test all notebooks by executing them with nbconvert.
"""

import subprocess
import glob
from typing import Any
import pytest


@pytest.mark.parametrize("notebook", glob.glob("**/*.ipynb", recursive=True))
def test_notebook_executes(notebook: str) -> None:
    """Test that notebook executes without errors."""
    if notebook.startswith('.'):
        pytest.skip("Skipping hidden notebook")

    # Use full path to jupyter to avoid security issues
    result = subprocess.run([
        "/usr/bin/env", "jupyter", "nbconvert", "--execute", "--to", "notebook", "--stdout", notebook
    ], capture_output=True, check=False)

    assert result.returncode == 0, f"Notebook {notebook} failed to execute"
