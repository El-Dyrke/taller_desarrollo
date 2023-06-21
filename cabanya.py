from conexion import Conexion

class Cabanya:
    def __init__(self, tipo_id, precio):
        self.tipo_id = tipo_id
        self.precio = precio

    def insertar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "INSERT INTO cabaña (tipo_id, precio) VALUES (%s, %s)"
            cursor.execute(sql, (self.tipo_id, self.precio))
            c.commit()
            c.close()
    
    def eliminar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "DELETE FROM cabaña WHERE id = %s"
            cursor.execute(sql, (id))
            c.commit()
            c.close()

    def actualizar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "UPDATE cabaña SET tipo_id = %s, precio = %s WHERE id = %s"
            cursor.execute(sql, (self.tipo_id, self.precio, id))
            c.commit()
            c.close()

    def listar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM cabaña"
            cursor.execute(sql)
            return cursor.fetchall()
            c.close()

    def consultar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM cabaña WHERE id = %s"
            cursor.execute(sql, (id))
            return cursor.fetchone()
            c.close()