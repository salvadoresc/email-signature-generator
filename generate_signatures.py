
import pandas as pd
import json
from jinja2 import Template
import os

# Load settings
with open('settings.json', 'r', encoding='utf-8') as f:
    settings = json.load(f)

# Convert disclaimer line breaks to <br>
settings['disclaimer'] = settings['disclaimer'].replace('\n', '<br />')

# Try reading CSV with utf-8-sig first, fallback to ISO-8859-1
try:
    df = pd.read_csv('staff.csv', encoding='utf-8-sig')
except UnicodeDecodeError:
    df = pd.read_csv('staff.csv', encoding='ISO-8859-1')

# Load the template
with open('signature_template.html', 'r', encoding='utf-8') as f:
    template = Template(f.read())

# Create output directory
output_dir = 'output_signatures'
os.makedirs(output_dir, exist_ok=True)

# Generate HTML files
for index, row in df.iterrows():
    context = row.where(pd.notnull(row), None).to_dict()
    context['settings'] = settings

    # Extract first part of name for filename
    full_name = row.get('name', '')
    name_parts = full_name.split(',')
    clean_name = name_parts[0].strip().lower().replace(' ', '_')
    filename = f"{clean_name}_signature.html"
    output_path = os.path.join(output_dir, filename)

    # Render and write to file
    html = template.render(**context)
    with open(output_path, 'w', encoding='utf-8') as f_out:
        f_out.write(html)
