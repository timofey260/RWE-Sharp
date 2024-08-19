from colorsys import rgb_to_hls

colors = ['#2A2A2A', '#E0E0E0', '#444444', '#2A2A2A', '#444444', '#3D3D3D', '#444444', '#2A2A2A', '#E0E0E0', '#444444',
          '#2A2A2A', '#444444', '#2A2A2A', '#444444', '#E0E0E0', '#3D3D3D', '#E0E0E0', '#555555', '#505050', '#E0E0E0',
          '#555555', '#2A2A2A', '#3D3D3D', '#2A2A2A', '#3D3D3D', '#E0E0E0', '#555555', '#505050', '#151a1e', '#151a1e',
          '#222b2e', '#d3dae3', '#222b2e', '#d3dae3', '#444444', '#d3dae3', '#3D3D3D', '#444444', '#d3dae3', '#505050',
          '#d3dae3', '#222b2e', '#d3dae3', '#d3dae3', '#4d9b87', '#d3dae3', '#52595d', '#214037', '#151a1e', '#d3dae3',
          '#151a1e', '#252a2e', '#FFFFFF', '#151a1e', '#252a2e', '#FFFFFF', '#d3dae3', '#151a1e', '#d3dae3', '#151a1e',
          '#050a0e', '#1e282c', '#9B9B9B', '#C2C7CB', '#050a0e', '#050a0e', '#050a0e', '#d3dae3', '#151a1e', '#050a0e',
          '#050a0e', '#050a0e', '#FFFFFF', '#1e282c', '#d3dae3', '#808086', '#1e282c', '#d3dae3', '#1e282c', '#027f7f',
          '#d3dae3', '#222b2e', '#16a085', '#a9b7c6', '#222b2e', '#a9b7c6', '#222b2e', '#FFFFFF', '#222b2e', '#555555',
          '#222b2e', '#3d4d53', '#2f3a3f', '#3d4d53', '#3d4d53', '#16a085', '#3d4d53', '#3d4d53', '#3d4d53', '#16a085',
          '#3d4d53', '#3d4d53', '#2f3a3f', '#3d4d53', '#3d4d53', '#2A2A2A', '#3D3D3D', '#2A2A2A', '#222b2e', '#151a1e',
          '#d3dae3', '#151a1e', '#222b2e', '#d3dae3', '#214037', '#151a1e', '#d3dae3', '#151a1e', '#222b2e', '#222b2e',
          '#214037', '#214037', '#a9b7c6', '#222b2e', '#222b2e', '#222b2e']

# Convert the list to a set to remove duplicates
unique_colors = set(colors)

# Print the number of unique colors
print(f'There are {len(unique_colors)} unique colors in the list.')

# Print each unique color
for color in unique_colors:
    print("'"+color+"'"+",")







def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_lightness(rgb):
    """Convert RGB to lightness value using the HLS color model."""
    return rgb_to_hls(*[x/255.0 for x in rgb])[1]

def sort_hex_colors_by_lightness(hex_colors):
    """Sort a list of hex colors by their lightness."""
    return sorted(hex_colors, key=lambda x: rgb_to_lightness(hex_to_rgb(x)))

# Example usage
hex_colors = ['#3D3D3D',
'#52595d',
'#2A2A2A',
'#a9b7c6',
'#16a085',
'#444444',
'#1e282c',
'#808086',
'#d3dae3',
'#3d4d53',
'#4d9b87',
'#555555',
'#C2C7CB',
'#505050',
'#E0E0E0',
'#214037',
'#222b2e',
'#FFFFFF',
'#9B9B9B',
'#151a1e',
'#252a2e',
'#027f7f',
'#050a0e',
'#2f3a3f',]
sorted_colors = sort_hex_colors_by_lightness(hex_colors)

print("Original colors:")
print(hex_colors)

print("\nSorted colors by lightness:")
print(sorted_colors)

['#050a0e', '#151a1e', '#1e282c', '#222b2e', '#252a2e', '#2A2A2A', '#214037', '#2f3a3f', '#3D3D3D', '#027f7f',
 '#444444', '#3d4d53', '#505050', '#555555', '#52595d', '#16a085', '#4d9b87', '#808086', '#9B9B9B', '#a9b7c6',
 '#C2C7CB', '#d3dae3', '#E0E0E0', '#FFFFFF']
