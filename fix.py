import os


def fix_coordinates_in_files(folder_path):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    for file in txt_files:
        lines = []
        with open(os.path.join(folder_path, file), 'r') as f:
            for line in f:
                data = line.split()
                corrected_data = [str(max(min(float(coord), 1), 0)) for coord in data]
                lines.append(' '.join(corrected_data) + '\n')

        with open(os.path.join(folder_path, file), 'w') as f:
            f.writelines(lines)


folder_path = 'seg/train/labels'
fix_coordinates_in_files(folder_path)
