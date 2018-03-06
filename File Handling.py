import csv
class Data:
    def __init__(self, Name="", Gender="", Age=0, Class="",):
        self.Name = Name
        self.Gender=Gender
        self.Age = Age
        self.Class = Class
    def __str__(self):
        OutString = "{0},{1}, {2},{3}".format(self.Name,self.Gender,self.Age,self.Class)
        return OutString
    def SaveData(Filename = "", DataList = []):
        with open(Filename,"w", newline='\n') as csvfile:
            DataWriter = csv.writer(csvfile,delimiter='\n',quotechar=" ",quoting=csv.QUOTE_NONNUMERIC)
            DataWriter.writerow(DataList)
            csvfile.close()
    def ReadData(Filename = ""):
        with open(Filename,"r", newline='\n') as csvfile:
            DataReader = csv.reader(csvfile,delimiter="\n",quotechar=" ",quoting=csv.QUOTE_NONNUMERIC)
            Output = []
            for Item in DataReader:
                Output.append(Item[0])
            csvfile.close()
            return Output

DataContent = [Data("Ansh", "Male",17, "XI-C"),Data("Aditya", "Male",18, "XII-C"),Data("Sally", "Female",16, "X-C")]
Data.SaveData("DataFile.csv", DataContent)

DataContent = Data.ReadData("DataFile.csv")
for Entry in DataContent:
    print(Entry)

print("\r\nAdding a Record for Harry.")
Record = "'Harry', 'Male', 17, 'XI-C'"
DataContent.append(Record)
for Entry in DataContent:
    print(Entry)
DataContent = Data.ReadData("DataFile.csv")

print("\r\nRemoving Aditya's record.")
print(DataContent)
Location = DataContent.index("Aditya,Male, 18,XII-C")
Record = DataContent[Location]
DataContent.remove(Record)
for Entry in DataContent:
    print(Entry)

print("\r\nModifying Sally's record.")
Location = DataContent.index("Sally,Female, 16,X-C")
Record = DataContent[Location]
Split = Record.split(",")
NewRecord = Data(Split[0].replace("'", ""),Split[1].replace("",""),int(Split[2]),Split[3].replace("",""))
NewRecord.Class = "XI-C"
NewRecord.Age = 17
DataContent.append(NewRecord.__str__())
DataContent.remove(Record)
for Entry in DataContent:
    print(Entry)
Data.SaveData("DataFile.csv", DataContent)
