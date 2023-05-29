import os


def replace_class_in_files(folder_path, current_class_index, new_class_index):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    for file in txt_files:
        lines = []
        with open(os.path.join(folder_path, file), 'r') as f:
            for line in f:
                data = line.split()
                if int(data[0]) == current_class_index:
                    data[0] = str(new_class_index)
                lines.append(' '.join(data) + '\n')

        with open(os.path.join(folder_path, file), 'w') as f:
            f.writelines(lines)


folder_path = 'seg/train/labels'
current_class_index = 1
new_class_index = 0
replace_class_in_files(folder_path, current_class_index, new_class_index)
