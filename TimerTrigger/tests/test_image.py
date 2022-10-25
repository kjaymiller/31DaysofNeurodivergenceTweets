import pathlib

import pytest


def test_assets_exist():
    """error if the necessary files are not present in the assets folder"""
    assert pathlib.Path("./assets/Adhd Awareness Month-6.png").exists()
    assert pathlib.Path("./assets/Lato-BoldItalic.ttf").exists()
