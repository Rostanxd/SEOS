from __future__ import unicode_literals

from django.db import models

ACTIVO = 'A'
INACTIVO = 'I'

ESTADOS = [
    (ACTIVO, 'Activo'),
    (INACTIVO, 'Inactivo'),
]


class Provincia(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True, db_column='proCodigo')
    nombre = models.CharField(max_length=25, db_column='proNombre')
    area = models.CharField(max_length=2, db_column='proArea')

    class Meta:
        db_table = 'pos_provincias'

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True, db_column='ciuCodigo')
    nombre = models.CharField(max_length=25, db_column='ciuNombre')
    provincia = models.ForeignKey(Provincia,
                                  models.SET_NULL,
                                  blank=True,
                                  null=True,
                                  db_column='proCodigo')

    class Meta:
        db_table = 'pos_ciudades'

    def estado_nombre(self):
        if self.estado == 'A':
            return 'Activo'
        else:
            return 'Inactivo'

    def __str__(self):
        return self.nombre
