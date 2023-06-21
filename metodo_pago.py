from conexion import Conexion


class Metodo_pago:
    def __init__(self, nombre):
        self.nombre = ""

    def insertar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "INSERT INTO `metodo_pago` (`nombre`) VALUES (%s)"
            cursor.execute(sql, (self.nombre))
        
        c.commit()
        c.close()
    
    def eliminar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "DELETE FROM `metodo_pago` WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))
        
        c.commit()
        c.close()

    def actualizar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "UPDATE `metodo_pago` SET `nombre` = %s WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))

        c.commit()
        c.close()

    def consultar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM `metodo_pago` WHERE `nombre` = %s"
            cursor.execute(sql, (self.nombre))
            return cursor.fetchone()

        c.close()

    def listar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM `metodo_pago`"
            cursor.execute(sql)
            c.close()
            return cursor.fetchall()