#!/usr/bin/env python3
"""
Pytest configuration for testing Jupyter notebooks.

This file enables nbmake to automatically discover and test all .ipynb files.
No explicit test functions needed - nbmake handles notebook execution testing.
"""

import pytest

# Configure nbmake settings
def pytest_configure(config):
    """Configure pytest for notebook testing."""
    # Set default timeout for notebook execution (10 minutes)
    config.option.nbmake_timeout = 600


if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main(["--nbmake", ".", "-v"])