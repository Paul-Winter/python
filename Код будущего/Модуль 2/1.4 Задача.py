# фильтрация логов по уровню
# - прочитать лог log.txt
# - сохранить только строки с уровнями ERROR и WARNING в errors.txt
import os
os.chdir("C:\\test")    #???
with open("log.txt", "r") as file:
    with open("errors.txt","w") as copyFile:
        for line in file:
            #if line.find("ERROR ") == 0 or line.find("WARNING ") == 0:
            if 'ERROR' in line or 'WARNING' in line:    
                copyFile.write(line)
        print("Логи отфильтрованы. Результат в errors.txt")
