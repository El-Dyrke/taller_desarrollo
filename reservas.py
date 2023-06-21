from conexion import Conexion

class Reserva:
    def __init__(self, cabanya_id, usuario_id, fecha_entrada, fecha_salida):
        self.cabanya_id = cabanya_id
        self.usuario_id = usuario_id
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def insertar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "INSERT INTO reservas (cabanya_id, usuario_id, fecha_entrada, fecha_salida) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.cabanya_id, self.usuario_id, self.fecha_entrada, self.fecha_salida))
            c.commit()
            c.close()

    def eliminar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "DELETE FROM reservas WHERE cabanya_id = %s AND usuario_id = %s"
            cursor.execute(sql, (self.cabanya_id, self.usuario_id))
            c.commit()
            c.close()
    
    def actualizar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "UPDATE reservas SET fecha_entrada = %s, fecha_salida = %s WHERE id = %s"
            cursor.execute(sql, (self.fecha_entrada, self.fecha_salida, id))
            c.commit()
            c.close()

    def consultar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM reservas WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            c.close()
            return resultado

    def listar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM reservas"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            c.close()
            return resultado