from conexion import Conexion


class Tipo_cabanya:
    def __init__(self, nombre):
        self.nombre = ""

    def insertar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "INSERT INTO `tipo_cabanya` (`nombre`) VALUES (%s)"
            cursor.execute(sql, (self.nombre))
        
        c.commit()
        c.close()
    
    def eliminar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "DELETE FROM `tipo_cabanya` WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))
        
        c.commit()
        c.close()

    def actualizar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "UPDATE `tipo_cabanya` SET `nombre` = %s WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))

        c.commit()
        c.close()

    def consultar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM `tipo_cabanya` WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))
            return cursor.fetchone()

        c.close()

    def listar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM `tipo_cabanya`"
            cursor.execute(sql)
            c.close()
            return cursor.fetchall()