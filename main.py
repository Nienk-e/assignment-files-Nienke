__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

def clean_cache():
    import os
    import shutil
    current_folder = os.getcwd()
    cache_path = current_folder + "/cache"
    if 'cache' in os.listdir(os.getcwd()):
        (shutil.rmtree(cache_path))
        return os.mkdir('cache')
    if 'cache' not in os.listdir(os.getcwd()):
        return os.mkdir('cache')
    return 

print(clean_cache())
        

def cache_zip(zip_file_path, cache_dir_path):
    from zipfile import ZipFile
    file_name = zip_file_path
    with ZipFile(file_name, 'r') as zip:
        zip.extractall(cache_dir_path)
    return

import os
cwd = os.getcwd()
zip_file_path = os.path.join(cwd,"data.zip") 
cache_dir_path = os.path.join(cwd,"cache")

print (cache_zip(zip_file_path, cache_dir_path))

def cached_files():
    import os
    cached_files_list = list(os.walk(cache_dir_path))    
    return cached_files_list

cached_files = cached_files()

def find_passwords(cached_files):
    for file_name in (cached_files[0][2]):
        file = open(file_name, "r")
        for line in file:
            if 'password' in file.read():
                password_file = file.read()
                start_password_line = password_file.find('password:')
                end_password_line = password_file.find('password:'[' ']) 
                password_line = password_file[start_password_line, end_password_line]
                print(password_line)
    else: print("password not found")
    return

print(find_passwords(cached_files))

    
    