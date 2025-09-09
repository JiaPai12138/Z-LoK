import re
import base64
import os

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read().decode('utf-8')

def write_file(file_path, content: str):
    with open(file_path, 'wb') as file:
        file.write(content.encode('utf-8'))

def png_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        base64_str = base64.b64encode(image_file.read()).decode('utf-8')
    return f'data:image/png;base64,{base64_str}'

def gif_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        base64_str = base64.b64encode(image_file.read()).decode('utf-8')
    return f'data:image/gif;base64,{base64_str}'

def replace_image_paths(html_content: str):
    pattern_png = re.compile(r'Docs/[^"]+\.png')
    matches_png = pattern_png.findall(html_content)

    for match in matches_png:
        if os.path.exists(match):
            base64_str = png_to_base64(match)
            html_content = html_content.replace(match, base64_str)

    pattern_gif = re.compile(r'Docs/[^"]+\.gif')
    matches_gif = pattern_gif.findall(html_content)

    for match in matches_gif:
        if os.path.exists(match):
            base64_str = gif_to_base64(match)
            html_content = html_content.replace(match, base64_str)

    return html_content

def process_html_file(html_file_path):
    html_content = read_file(html_file_path)
    updated_html_content = replace_image_paths(html_content)
    write_file(html_file_path, updated_html_content)

# Usage
html_file_path = 'README.html'
process_html_file(html_file_path)
