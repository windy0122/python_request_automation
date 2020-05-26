import configparser


cf = configparser.ConfigParser()
cf.read('case.ini', encoding='utf-8')

# res_1 = cf.get('MODE', 'mode')
# print(res_1)
#
# res_2 = cf['MODE']['mode']
# print(res_2)

# print(cf.sections())    # ['MODE', 'PYTHON', 'LEMON']
# print(cf.items('PYTHON'))   # [('num', '66'), ('name', '吴迪')]

