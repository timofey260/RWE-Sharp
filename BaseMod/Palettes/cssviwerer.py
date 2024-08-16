import re
from PIL import Image


def find_hex_colors(input_string):
    hex_pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'

    # Find all matches of the pattern in the input string
    hex_colors = re.findall(hex_pattern, input_string)

    return hex_colors


# Example usage
input_string = """['#3B3B3B', '#3A3A3A', '#3A3A3A', '#3A3A3A', '#3D3D3D', '#333333', '#333333', '#333333', '#333333', '#333333', '#2B2B2B', '#2B2B2B', '#2B2B2B', '#2B2B2B', '#2B2B2B', '#252525', '#252525', '#252525', '#252525', '#252525', '#252525', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#1E1E1E', '#505050', '#505050', '#505050', '#505050', '#505050', '#505050', '#505050', '#505050', '#505050', '#555555', '#666666', '#666666', '#7B7B7B', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#D6D6D6', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#388E3C']"""
result = find_hex_colors(input_string)

# Print the list of colors
print("Found hex colors:", result)

# Print the number of colors
print("Number of hex colors found:", len(result))


def hex_to_rgb(hex_color):
    """Convert a HEX color to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def create_image(hex_colors, size=(41, 2)):
    """Create an image from a list of HEX colors."""
    # Ensure the number of colors matches the required size
    if len(hex_colors) != size[0] * size[1]:
        raise ValueError(f"Number of colors ({len(hex_colors)}) does not match the image size ({size[0]}x{size[1]}).")

    # Create a new image with the specified size
    img = Image.new('RGB', size)
    pixels = img.load()

    # Convert HEX colors to RGB and populate the image
    for i, hex_color in enumerate(hex_colors):
        x = i % size[0]
        y = i // size[0]
        pixels[x, y] = hex_to_rgb(hex_color)

    return img



hex_colors = find_hex_colors(input_string)

# Create the image
image = create_image(hex_colors)

# Save or show the image
image.show()  # To display the image
image.save("hex_colors_image.png")
