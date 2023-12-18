from jinja2 import Template
import os

TEMPLATE = 'template.html'
MATRIX = 'matrix'
OUTPUT = 'web/index.html'


def convert(file):
    with open(file) as file:
        lines = file.readlines()

    data = {'category': {}}
    category = ''
    for line in lines:
        if line.startswith('# '):
            data['header'] = line.strip('#').strip()
        elif line.startswith('## '):
            category = line.strip('##').strip()
            data['category'][category] = []
        elif line.startswith('- '):
            data['category'][category].append(line.strip('-').strip())
        elif line.startswith('  - '):
            data['category'][category].append(line.strip())
        else:
            data['description'] = line.strip()

    return data


if __name__ == '__main__':
    data = []
    files = os.listdir(MATRIX)
    for file in files:
        if file.endswith('.md'):
            data.append(convert(os.path.join(MATRIX, file)))
    template = Template(open(TEMPLATE).read())
    levels = ((1, 'Trainee'), (2, 'Junior'), (3, 'Middle'), (4, 'Senior'), (5, 'Expert'))
    with open(OUTPUT, 'w') as file:
        file.write(template.render(data=data, levels=levels))