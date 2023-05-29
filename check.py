import os


def check_class_in_files(folder_path, class_index):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    files_with_class = []
    for file in txt_files:
        with open(os.path.join(folder_path, file), 'r') as f:
            for line in f:
                data = line.split()
                if int(data[0]) == class_index:
                    files_with_class.append(file)
                    break

    return files_with_class


folder_path = 'seg/train/labels'
class_index = 0
files_with_class = check_class_in_files(folder_path, class_index)
print(f"Files containing class {class_index}:")
for file in files_with_class:
    print(file)
