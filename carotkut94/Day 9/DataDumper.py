# I encountered a problem of data dumping faced by my colleagues
# I wrote this script for them for data entry


import time
import mysql.connector
import xlrd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sample"
)

cursor = db.cursor()

workbook = xlrd.open_workbook("car.xlsx")
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
for rowx in range(sheet.nrows):
    row = sheet.row_values(rowx)
    model_name = row[0]
    fuel_type = row[1]
    customer_service_rate = row[2]
    partner_service_rate = row[3]
    service_id = 44
    vehicle_type = 1
    modified_date = time.time()
    created_date = time.time()
    estimated_time = ""

    mysql = """insert into services_available_for_models(model_id, service_id, vehicle_type_id, fuel_type_id, estimated_time,company_service_rate,partner_service_rate,created,modified) value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    val = (model_name, service_id, vehicle_type, fuel_type, estimated_time, customer_service_rate, partner_service_rate,
           created_date, modified_date)
    cursor.execute(mysql, val)
    db.commit()
    print(mysql)
