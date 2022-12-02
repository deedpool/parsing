# import openpyxl
# from openpyxl import Workbook

# book_tess = openpyxl.open("23.xlsx")
# sheets = book_tess.sheetnames
# ws2 = book_tess[sheets[1]]

# wb = Workbook()
# ws = wb.active
# n=2

# for i in ws2[n][0].value:
#     gg = ws2[n][0].value
#     ws.append([gg])
#     # print(gg)
#     n+=1
# wb.save("sample.xlsx")

# Имя;Фамилмя;user_id;Пол;Город;Год Рождения;group_id
a = "https://vk.com/ligioligio"

if 'vk.' in a:
    print(1)
else:
    print(2)

# import sys

# if __name__ == "__main__":
#     for group_URL in sys.argv:
#         print (group_URL)