import os
#import shutil

if not os.path.exists('Управление_файлами'):
  os.mkdir('Управление_файлами')

file1_path = os.path.join('Управление_файлами', 'file1.txt')
file2_path = os.path.join('Управление_файлами', 'file2.txt')

with open(file1_path, 'w', encoding='utf-8') as file1:
  file1.write('Файл 1.')

with open(file2_path, 'w', encoding='utf-8') as file2:
  file2.write('Файл 2.')

files_and_dirs = os.listdir('Управление_файлами')
print("Файлы и директории:", files_and_dirs)

os.remove(file1_path)

files_and_dirs = os.listdir('Управление_файлами')
print("Файлы и директории:", files_and_dirs)

if not os.path.exists('Управление_файлами/Поддиректория'):
  os.mkdir('Управление_файлами/Поддиректория')

file2_path_new = os.path.join('Управление_файлами/Поддиректория', 'file2.txt')

os.system('move Управление_файлами\\file2.txt Управление_файлами\\Поддиректория') #через cmd
#shutil.move('Управление_файлами/file2.txt', 'Управление_файлами/Поддиректория') 

files_and_dirs = os.listdir('Управление_файлами')
print("Файлы и директории:", files_and_dirs)

files_and_dirs = os.listdir('Управление_файлами/Поддиректория')
print("Файлы и директории:", files_and_dirs)


os.system('rmdir /s Управление_файлами') #через cmd
#shutil.rmtree('Управление_файлами')