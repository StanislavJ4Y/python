from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
import csv

# Клас СТУДЕНТ
class Student:
    def __init__(self, full_name, group_number, birthdate, address=None):
        self.__full_name = full_name
        self.__group_number = group_number
        self.__birthdate = birthdate
        self.__address = address

    # Геттери та сеттери
    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_group_number(self):
        return self.__group_number

    def set_group_number(self, group_number):
        self.__group_number = group_number

    def get_birthdate(self):
        return self.__birthdate

    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

# Абстрактний клас УСПІШНІСТЬ
class AcademicPerformance(ABC):
    def __init__(self, subjects, grades):
        self.subjects = subjects
        self.grades = grades

    @abstractmethod
    def average_grade(self):
        pass

# Клас РЕАЛЬНА УСПІШНІСТЬ
class ActualPerformance(AcademicPerformance):
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# Клас БАЖАНА УСПІШНІСТЬ
class DesiredPerformance(AcademicPerformance):
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# Клас ДАНІ_СТУДЕНТА
class StudentData:
    def __init__(self, student, actual_performance, desired_performance):
        self.student = student
        self.actual_performance = actual_performance
        self.desired_performance = desired_performance

    def get_data_dict(self):
        return {
            "Student": {
                "Full Name": self.student.get_full_name(),
                "Group Number": self.student.get_group_number(),
                "Birthdate": self.student.get_birthdate(),
                "Address": self.student.get_address(),
            },
            "Actual Performance": {
                "Subjects": self.actual_performance.subjects,
                "Grades": self.actual_performance.grades,
                "Average Grade": self.actual_performance.average_grade()
            },
            "Desired Performance": {
                "Desired Grades": self.desired_performance.grades,
                "Desired Average Grade": self.desired_performance.average_grade()
            }
        }

# Абстрактний клас ЗБЕРЕЖЕННЯ_ДАНИХ
class DataSaver(ABC):
    @abstractmethod
    def save(self, data, filename):
        pass

# Клас ЗБЕРЕЖЕННЯ_У_JSON
class SaveToJSON(DataSaver):
    def save(self, data, filename):
        with open(f"{filename}.json", "w") as file:
            json.dump(data, file, indent=4)  # Записує дані у файл у форматі JSON

# Клас ЗБЕРЕЖЕННЯ_У_XML
class SaveToXML(DataSaver):
    def save(self, data, filename):
        root = ET.Element("StudentData")

        student_info = ET.SubElement(root, "Student")
        ET.SubElement(student_info, "FullName").text = data["Student"]["Full Name"]
        ET.SubElement(student_info, "GroupNumber").text = data["Student"]["Group Number"]
        ET.SubElement(student_info, "Birthdate").text = data["Student"]["Birthdate"]
        ET.SubElement(student_info, "Address").text = data["Student"]["Address"]

        actual_performance = ET.SubElement(root, "ActualPerformance")
        ET.SubElement(actual_performance, "Subjects").text = ', '.join(data["Actual Performance"]["Subjects"])
        ET.SubElement(actual_performance, "Grades").text = ', '.join(map(str, data["Actual Performance"]["Grades"]))
        ET.SubElement(actual_performance, "AverageGrade").text = str(data["Actual Performance"]["Average Grade"])

        desired_performance = ET.SubElement(root, "DesiredPerformance")
        ET.SubElement(desired_performance, "DesiredGrades").text = ', '.join(map(str, data["Desired Performance"]["Desired Grades"]))
        ET.SubElement(desired_performance, "DesiredAverageGrade").text = str(data["Desired Performance"]["Desired Average Grade"])

        tree = ET.ElementTree(root)
        tree.write(f"{filename}.xml")

# Клас ЗБЕРЕЖЕННЯ_У_CSV
class SaveToCSV(DataSaver):
    def save(self, data, filename):
        with open(f"{filename}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Data"])
            writer.writerow(["Full Name", data["Student"]["Full Name"]])
            writer.writerow(["Group Number", data["Student"]["Group Number"]])
            writer.writerow(["Birthdate", data["Student"]["Birthdate"]])
            writer.writerow(["Address", data["Student"]["Address"]])
            writer.writerow(["Subjects", ', '.join(data["Actual Performance"]["Subjects"])])
            writer.writerow(["Grades", ', '.join(map(str, data["Actual Performance"]["Grades"]))])
            writer.writerow(["Average Grade", data["Actual Performance"]["Average Grade"]])

