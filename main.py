import os, glob, getpass, shutil

def delete_exefiles_from_downloads_dir():
    username = getpass.getuser()
    downloads_directory = glob.glob('c:\\Users\\' + username +'\\Downloads\\*.exe')
    exe_found = False
    
    for exe_file in downloads_directory:
        if os.path.exists(exe_file):
            os.remove(exe_file)
            print(f"{exe_file} successfully removed!")
            exe_found = True

    if not exe_found:
        print("No exe files found in the downloads folder.")
        
        
def delete_temp_files():
    temp_folder = 'C:\\Windows\\Temp'
    shutil.rmtree(temp_folder, ignore_errors=True)
    print('All files in the temp folder have been deleted.') 
    return

def delete_temp2_files():
    username = getpass.getuser()
    temp2_folder = 'C:\\Users\\' + username + '\\AppData\\Local\\Temp'
    shutil.rmtree(temp2_folder, ignore_errors=True)
    print('All files in the %temp% folder have been deleted.') 
    return

def delete_prefetch_files():
    prefetch_folder = 'C:\\Windows\\Prefetch'
    shutil.rmtree(prefetch_folder, ignore_errors=True)
    print('All files in the prefetch folder have been deleted.') 
    return


delete_exefiles_from_downloads_dir()
delete_temp_files()
delete_temp2_files()
delete_prefetch_files()