#!/usr/bin/env python3
"""
Test all notebooks by executing them with nbconvert.
"""

import subprocess
import glob
import pytest


@pytest.mark.parametrize("notebook", glob.glob("**/*.ipynb", recursive=True))
def test_notebook_executes(notebook):
    """Test that notebook executes without errors."""
    if notebook.startswith('.'):
        pytest.skip("Skipping hidden notebook")

    result = subprocess.run([
        'jupyter', 'nbconvert', '--execute', '--to', 'notebook', '--stdout', notebook
    ], capture_output=True)

    assert result.returncode == 0, f"Notebook {notebook} failed to execute"
