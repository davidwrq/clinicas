# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class ClinicasItem(Item):
    rubro =  Field()
    rut = Field()
    direccion = Field()
    comuna = Field()
    ciudad = Field()
    razon_social = Field()
    telefono = Field()
    contacto = Field()
    rol = Field()
    nombre_de_fantasia = Field()
    sitio_web = Field()
    mail = Field()
    facebook = Field()
