from openpyxl import Workbook

obj=Workbook()

obj_active=obj.active

obj_active["B2"]="salom"
obj_active["C5"]="24"
obj_active["A2"]="Hayr"

obj_active.append([1,2,3,4,5,6,7])

print(obj_active["A2"].value)

obj.save("hujjat.xlsx")