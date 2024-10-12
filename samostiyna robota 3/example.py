from main import Student, ActualPerformance, DesiredPerformance, StudentData, SaveToJSON, SaveToXML, SaveToCSV

# Створення студента та успішності
student = Student("Palagniy Stas", "ISD31", "2004-12-20", "Kiev, Ukraine")
actual_performance = ActualPerformance(["Python", "IOT", "English"], [100, 95, 97])
desired_performance = DesiredPerformance(["Design", "Redio technology"], [97, 92])

# Дані студента
student_data = StudentData(student, actual_performance, desired_performance)
data_dict = student_data.get_data_dict()

# Збереження в різні формати
json_saver = SaveToJSON()
json_saver.save(data_dict, "PalagniyStas_ISD31_PR5")

xml_saver = SaveToXML()
xml_saver.save(data_dict, "PalagniyStas_ISD31_PR5")

csv_saver = SaveToCSV()
csv_saver.save(data_dict, "PalagniyStas_ISD31_PR5")
