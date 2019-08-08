import os
def rename_files():
    file_list = os.listdir('/Users/cidmedeiros1/Pictures/Piri_Trip')
    print(file_list)
    saved_path = os.getcwd()
    print("Working dir is " + saved_path)
    os.chdir('/Users/cidmedeiros1/Pictures/Piri_Trip')
    var0 = '.JPG'
    var1 = 1
    var2 = 'Piri_Trip'
    for file_name in file_list:
        print('Old Name was '+file_name)
        var1 = str(var1)
        new_file_name = var2+var1+var0
        os.rename(file_name,new_file_name)
        print('New Name is '+new_file_name)
        var1 = int(var1)
        var1 = var1+1
        
rename_files()
