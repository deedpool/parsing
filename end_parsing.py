import openpyxl
import vk_api
import csv
import re

# Имя;Фамилмя;id_user;Пол;Город;Год Рождения;id_group
# -------------------------------------------------
book_tess = openpyxl.open("12.xlsx") #Выбор файла с данными групп
sheets = book_tess.sheetnames
data_excel = book_tess[sheets[0]] #Тут можно выбрать лист
stolbik = 1 #выбор столбца
stroka = 0 # выбор с какой строки начнет


# WORK VK
session = vk_api.VkApi(token="")#Ввести токен вк
vk = session.get_api()

def pars_memb(group_id):
    offset = 0
    count = 1000
    has_more_mambers = True
    resoult = []
    while has_more_mambers == True:
        response = session.method("groups.getMembers", {
            "group_id" : group_id,
            "fields" : "sex , city , bdate , domain",
            "offset" : offset,
            "count" : count
            })
        print(offset,len(response["items"]))
        has_more_mambers = bool(len(response["items"]))
        offset += count
        resoult = resoult + response["items"]
    
    return resoult

def get_user_city(user):
    try:
        return user["city"]["title"]
    except:
        return None

def get_user_by(user):
    try:
        date = user["bdate"].split(".")
        if len(date) == 3:
            return date[-1]
    except:
        return None

# Сохранение файла
def save_group_members(users):
    with open('moskow.csv','a',encoding='utf8', newline='') as File:  #Задать название файла
        writers = csv.writer(File,delimiter=';')
        for user in users:
            writers.writerow([
                user.get("first_name",""),
                user.get("last_name",""),
                user.get("domain",""),
                user.get("sex",""),
                get_user_city(user),
                get_user_by(user),
                goko
            ])


for urlrs in range(stolbik,data_excel.max_row):
    goko = data_excel[urlrs][stroka].value
    znachenieForUrl = data_excel[stolbik][stroka].value
    print(znachenieForUrl)
    if "m/" in znachenieForUrl:
        goko = znachenieForUrl.split("m/")[1]
        print(goko)

    if re.findall(r"club\d+", goko):
        nums = re.findall(r'\d+', goko)
        nums = [int(i) for i in nums]
        non_club = " ".join(map(str,nums))
        print(non_club)
        members = pars_memb(non_club)
        save_group_members(members)
    elif re.findall(r"public\d+", goko):
        nums = re.findall(r'\d+', goko)
        nums = [int(i) for i in nums]
        non_club = " ".join(map(str,nums))
        print(non_club)
        members = pars_memb(non_club)
        save_group_members(members)
    else:
        try:
            members = pars_memb(goko)
            save_group_members(members)
        except:
            None