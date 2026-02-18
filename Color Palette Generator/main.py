"""module for the color palette generator"""

import random

def generate_color_palette(num_colors=5):
    """Generate a color palette with the specified number of colors."""
    palette = []
    for _ in range(num_colors):
        color = f"#{random.randint(0, 0xFFFFFF):06x}"
        palette.append(color)
    return palette

if __name__ == "__main__":
    NUM_COLORS = 5  # You can change this to generate a different number of colors
    generated_palette = generate_color_palette(NUM_COLORS)
    print("Generated Color Palette:")
    for generated_color in generated_palette:
        print(generated_color)
