from conexion import Conexion


class Tipo_usuario:
    def __init__(self, nombre):
        self.nombre = ""

    def insertar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "INSERT INTO `tipo_usuario` (`nombre`) VALUES (%s)"
            cursor.execute(sql, (self.nombre))
        
        c.commit()
        c.close()
    
    def eliminar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "DELETE FROM `tipo_usuario` WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))
        
        c.commit()
        c.close()

    def actualizar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "UPDATE `tipo_usuario` SET `nombre` = %s WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))

        c.commit()
        c.close()

    def consultar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM `tipo_usuario` WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))
            return cursor.fetchone()

        c.close()

    def listar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM `tipo_usuario`"
            cursor.execute(sql)
            c.close()
            return cursor.fetchall()