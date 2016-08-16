import os
def rename_files():
    file_list = os.listdir(r"V:\abc")
    print(file_list)
    path=os.getcwd()
    print("current working directory is:"+path)
    os.chdir(r"V:\abc")

    for file_name in file_list:
        os.rename(file_name,file_name.translate("0123456789"))
    os.chdir(path)
rename_files()    
