import os
import yaml


def extract_info_from_yaml(file_path):
    with open(file_path, 'r') as file:
        content = yaml.safe_load(file)

    names = []
    dependencies = []

    for item in content:
        name = item.get('name', '')
        dep = item.get('dependencies', [])

        if name:
            names.append(name)

        for d in dep:
            if d:
                dependencies.append(d)

    # Remove duplicates
    names = list(set(names))
    dependencies = list(set(dependencies))

    return names, dependencies


def write_to_file(file_path, names, dependencies):
    with open(file_path, 'w') as file:
        for name in names:
            file.write(f'"{name}",\n')
        for dependency in dependencies:
            file.write(f'"{dependency}",\n')


file_path = 'mods.yml'  # Path to your YAML file
names, dependencies = extract_info_from_yaml(file_path)

output_file_path = 'output.txt'  # Path to the output text file
write_to_file(output_file_path, names, dependencies)
