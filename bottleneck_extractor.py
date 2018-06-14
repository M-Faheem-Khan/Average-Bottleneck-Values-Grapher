# modules
import os
from statistics import mean

def bottleneck_values(folder):
        # getting list of files
        path = os.getcwd()+"/"+folder+"/"
        list_of_files = os.listdir(path) 
        # printing list_of_files
        print(list_of_files)
        list_of_average = []
        for file in list_of_files:
                content = []
                temp = []
                with open(path+file, "r+") as f:
                        content = f.read().strip().split(",")
                        for value in range(len(content)):
                                content[value] = float(content[value])
                                temp.append(content[value])

                list_of_average.append(mean(temp))

        file_name = folder+".txt"
        print("Writing list of averages to file")
        with open(file_name, "w") as f:
                for i in list_of_average:
                        f.write(str(i) + ",")




folders = ["Warbler1", "Warbler2", "Warbler3", "Warbler4"]
for folder in folders:
        bottleneck_values(folder)