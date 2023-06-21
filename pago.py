from conexion import Conexion

class Pago:
    def __init__(self, reserva_id, fecha_pago, monto, metodo_pago):
        self.reserva_id = reserva_id
        self.fecha_pago = fecha_pago
        self.monto = monto
        self.metodo_pago = metodo_pago

    def insertar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "INSERT INTO pagos (reserva_id, fecha_pago, monto, metodo_pago) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.reserva_id, self.fecha_pago, self.monto, self.metodo_pago))
            c.commit()
            c.close()
    
    def actualizar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "UPDATE pagos SET reserva_id = %s, fecha_pago = %s, monto = %s, metodo_pago = %s WHERE id = %s"
            cursor.execute(sql, (self.reserva_id, self.fecha_pago, self.monto, self.metodo_pago, id))
            c.commit()
            c.close()
    
    def eliminar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "DELETE FROM pagos WHERE id = %s"
            cursor.execute(sql, (id))
            c.commit()
            c.close()

    def consultar(self, id):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM pagos WHERE id = %s"
            cursor.execute(sql, (id))
            pago = cursor.fetchone()
            c.close()
            return pago

    def listar(self):
        c = Conexion()

        with c.cursor() as cursor:
            sql = "SELECT * FROM pagos"
            cursor.execute(sql)
            pagos = cursor.fetchall()
            c.close()
            return pagos

