import cv2
import os
from moviepy.editor import *
import moviepy
import os
import shutil
ACCELERATOR=1.25
def compare_and_copy(folder_A, folder_B, folder_outputs):
    # Get the list of files in each folder
    files_A = set(os.listdir(folder_A))
    files_B = set(os.listdir(folder_B))

    # Find files that exist in B but not in A
    missing_files = files_B - files_A

    # Copy missing files to the Outputs folder
    for file in missing_files:
        path_to_file_B = os.path.join(folder_B, file)
        path_to_file_outputs = os.path.join(folder_outputs, file)
        shutil.copy2(path_to_file_B, path_to_file_outputs)
        print(f"Copied file: {file}")
if __name__ == '__main__':

    folder_path = "inputs2/"  # Укажите путь к папке, из которой вы хотите извлечь имена файлов
    out_folder='accelerated_3/'
    # Получаем список всех файлов в папке
    file_list = os.listdir(folder_path)

    # Вы можете также использовать list comprehension, чтобы получить только имена файлов без подпапок
    file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_path, f))]

    # Теперь в переменной `file_names` у вас будет список имен файлов из указанной папки
    print(file_names)
    for i in range (0,len(file_names)):
        print(str(i)+'   '+file_names[i])
        clip = VideoFileClip(folder_path+file_names[i])
        slowed_clip = clip.fx(vfx.speedx, ACCELERATOR)
        slowed_clip.write_videofile(out_folder+file_names[i])
    '''folder_A = "Small-dir"
    folder_B = "Big-dir"
    folder_outputs = "difference-dir"

    compare_and_copy(folder_A, folder_B, folder_outputs)'''