import csv 
from collections import namedtuple
from datetime import datetime, date, timedelta
Menu = namedtuple('Menu', 'Category,Item,Serving Size,Calories,Calories from Fat,Total Fat,Cholesterol,precio_menus,fecha_entrada,hora_cierre,fecha_comidas')

def lee_reparaciones(fichero):
    with open(fichero,enconding='utf-8')as f:
        lector = csv.reader(f,delimiters=";")
        next(lector)
        res = []
        for Category,Item,Serving Size,Calories,Calories from Fat,Total Fat,Cholesterol,precio_menus,fecha_entrada,hora_cierre,fecha_comidas in lector
           fecha_entrada = parsea_fecha(fecha_entrada)
           hora_cierre = parsea_hora(hora_cierre)
           fecha_comidas = parsea_fecha(fecha_comidas)
           hora_cierre = parsea_hora(hora_cierre)
           precio_menus = float(precio_menus)
           res.append(Menu(Category,Item,Serving Size,Calories,Calories from Fat,Total Fat,Cholesterol,precio_menus,fecha_entrada,hora_cierre,fecha_comidas))
        return res

def parsea_fecha(str_fecha):
    return datetime.strptime(srt_fecha, '%d/%m/%Y' ).date()