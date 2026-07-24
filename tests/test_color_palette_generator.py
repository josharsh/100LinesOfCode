"""Unit tests for the Color Palette Generator (``Color Palette Generator/main.py``)."""
import re

import pytest

from conftest import load_module

palette = load_module("Color Palette Generator/main.py", "color_palette_generator")

HEX_COLOR = re.compile(r"^#[0-9a-f]{6}$")


@pytest.mark.parametrize("num_colors", [1, 5, 12])
def test_palette_has_requested_length(num_colors):
    assert len(palette.generate_color_palette(num_colors)) == num_colors


def test_default_palette_length_is_five():
    assert len(palette.generate_color_palette()) == 5


def test_all_colors_are_valid_hex():
    colors = palette.generate_color_palette(50)
    assert all(HEX_COLOR.match(color) for color in colors)


def test_zero_colors_returns_empty_list():
    assert palette.generate_color_palette(0) == []
