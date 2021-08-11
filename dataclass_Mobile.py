"""
A dataclass is now created here to store information regarding mobiles
"""
import json
from dataclasses import dataclass


@dataclass
class Mobile:
    """
    This is a dataclass that stores information regarding mobiles.
    It also handles insertion, deletion, update and deletion in smartphone_data.json
    file.
    """
    name: str
    series: str
    camera_mp: int
    battery_ah: int
    cost: float
    manufacturer: str

    def __init__(self):
        self.name = ''
        self.manufacturer = ''
        self.camera_mp = 0
        self.battery_ah = 0
        self.cost = 0
        self.series = ''

    def writeData(self, name, manfac, camera_mp, battery_ah, series, cost):
        """
        Method to enter data into a Mobile object
        \nname: Name of mobile phone
        \nmanfac: Manufacturer
        \ncamera_mp: Value of Camera Resolution Megapixel
        \nbattery_ah: mAH Value of Phone Batterys
        \nseries: Phone series
        \ncost: Cost of the phone
        \nreturn: none
        """
        self.name = name
        self.manufacturer = manfac
        self.camera_mp = camera_mp
        self.battery_ah = battery_ah
        self.series = series
        self.cost = cost

    @classmethod
    def getUserInput(cls):
        """
        Takes user input for name, manufacturer, camera resolution (in MP) and Battery mAH Value
        \nreturn: name, manufacturer, camera resolution, battery mAH Value
        """
        nam = input("Enter phone name: ")
        manf = input("Enter manufacturer of phone: ")
        cam_mp = int(input("Enter megapixel value for camera: "))
        batt_ah = int(input("Enter mAH value of battery: "))
        return nam, manf, cam_mp, batt_ah

    def __str__(self):
        str1 = ''
        if self.name != '':
            str1 = "Name: " + self.name
        if self.manufacturer != '':
            str1 += "\nManufacturer: " + self.manufacturer
        if self.camera_mp != '' and self.camera_mp != 0:
            str1 += "\nCamera MP: " + str(self.camera_mp)
        if self.battery_ah != '' and self.battery_ah != 0:
            str1 += "\nBattery mAH: " + str(self.battery_ah)
        if self.series != '':
            str1 += "\nSeries: " + self.series
        if self.cost != '' and self.cost != 0:
            str1 += "\nCost: " + str(self.cost)
        return str1

    @classmethod
    def writeFile(cls, mobile_list):
        """
        Method that writes mobile_list data into the file smartphone_data.json
        \nmobile_list: List of Mobile objects
        \nreturn: none
        """
        # f1 = open("smartphone_data.csv", 'w', encoding='UTF-8', newline='')
        header = ["Name", "Manufacturer", "Camera_mp", "Battery_ah", "Series", "Cost"]
        # it1 = iter(header)
        m1 = []
        for ele in mobile_list:
            it1 = iter(header)
            it2 = iter([ele.name, ele.manufacturer, ele.camera_mp, ele.battery_ah, ele.series, ele.cost])
            dict1 = dict(zip(it1, it2))
            m1.append(dict1)
            # w1.writerow([item.name, item.manufacturer, item.camera_mp, item.battery_ah, item.series, item.cost])
        f1 = open("smartphone_data.json", 'w', encoding='UTF-8')
        jsonString = json.dumps(m1, indent=2)
        f1.write(jsonString)
        f1.close()
        # print("File Written\n")
        # f1.close()

    @classmethod
    def readFile(cls):
        """
        Reads the data present in file
        \nreturn: List of mobile objects
        """
        m1 = []
        f1 = open("smartphone_data.json", 'r', encoding='UTF-8')
        data = json.load(f1)
        series_column = 4
        cost_column = 5
        k1 = 'Name'
        k2 = 'Manufacturer'
        k3 = 'Camera_mp'
        k4 = 'Battery_ah'
        k5 = 'Series'
        k6 = 'Cost'
        for item in data:
            m2 = Mobile()
            if len(item.keys()) == series_column:
                m2.writeData(item[k1], item[k2], item[k3], item[k4], '', '')
            elif len(item.keys()) == cost_column:
                m2.writeData(item[k1], item[k2], item[k3], item[k4], item[k5], '')
            else:
                m2.writeData(item[k1], item[k2], item[k3], item[k4], item[k5], item[k6])
            m1.append(m2)
        f1.close()
        return m1

    def addRowInFile(self):
        m1 = Mobile.readFile()
        header = ["Name", "Manufacturer", "Camera_mp", "Battery_ah", "Series", "Cost"]
        it1 = iter(header)
        it2 = iter([self.name, self.manufacturer, self.camera_mp, self.battery_ah, self.series, self.cost])
        dict1 = dict(zip(it1, it2))
        index = [index for index in range(len(m1)) if m1[index].name == self.name]
        if len(index) > 0:
            print("Error! Cannot add the record. Phone with this name already exists")
            return
        with open("smartphone_data.json", "r+", encoding='UTF-8') as file:
            data = json.load(file)
            data.append(dict1)
            file.seek(0)
            jsonString = json.dumps(data, indent=2)
            file.write(jsonString)
            print("File updated")

    @classmethod
    def deleteRowInFile(cls):
        m1 = Mobile.readFile()
        name = input("Enter name of Phone which has to be deleted from file: ")
        index = [index for index in range(len(m1)) if m1[index].name == name]
        if len(index) == 0:
            print("No such phone name can be found")
            return
        del m1[index[0]]
        Mobile.writeFile(m1)

    @classmethod
    def updateFile(cls):
        m1 = Mobile.readFile()
        name = input("Enter name of the phone for which the change has to be made: ")
        index = [index for index in range(len(m1)) if m1[index].name == name]
        if len(index) == 0:
            print("No such phone name can be found")
            return
        print("Enter the value you wish to update:"
              "\n 1 - Name"
              "\n 2 - Manufacturer"
              "\n 3 - Camera MP"
              "\n 4 - Battery mAH"
              "\n 5 - Cost")
        ch = int(input("\n Enter your choice: "))
        if ch == 1:
            m1[index[0]].name = input("Enter new name for the phone: ")
        elif ch == 2:
            m1[index[0]].manufacturer = input("Enter name of Manufacturer ")
        elif ch == 3:
            m1[index[0]].camera_mp = int(input("Enter camera megapixel value: "))
        elif ch == 4:
            m1[index[0]].battery_ah = int(input("Enter battery mAH value: "))
        elif ch == 5:
            m1[index[0]].cost = float(input("Enter phone cost: "))
        Mobile.writeFile(m1)

    @classmethod
    def searchFile(cls):
        """
        Searches the file based on attributes
        """
        m1 = Mobile.readFile()
        print("Enter the attribute based on which the search should occur:"
              "\n 1 - Name"
              "\n 2 - Manufacturer"
              "\n 3 - Camera MP"
              "\n 4 - Battery mAH"
              "\n 5 - Series")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            name = input("Enter name of Phone: ")
            index = [index for index in range(len(m1)) if m1[index].name == name]
            if len(index) == 0:
                print("No such phone name can be found")
                return
            print(m1[index[0]])

        if ch == 2:
            manf = input("Enter manufacturer name: ")
            index = [index for index in range(len(m1)) if m1[index].manufacturer == manf]
            if len(index) == 0:
                print("Not found")
                return
            for i in index:
                print(m1[i])
                print("\n")

        if ch == 3:
            cam_mp = input("Enter Camera Megapixel value: ")
            index = [index for index in range(len(m1)) if m1[index].camera_mp == cam_mp]
            if len(index) == 0:
                print("Not found")
                return
            for i in index:
                print(m1[i])
                print("\n")

        if ch == 4:
            batt_ah = input("Enter Battery mAH Value: ")
            index = [index for index in range(len(m1)) if m1[index].battery_ah == batt_ah]
            if len(index) == 0:
                print("Not found")
                return
            for i in index:
                print(m1[i])
                print("\n")

        if ch == 5:
            series1 = input("Enter phone series: ")
            index = [index for index in range(len(m1)) if m1[index].series == series1]
            if len(index) == 0:
                print("Not found")
                return
            for i in index:
                print(m1[i])
                print("\n")
