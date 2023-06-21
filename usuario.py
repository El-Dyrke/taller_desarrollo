from conexion import Conexion

class Usuario:
    def __init__(self, tipo_id, rut, nombre, apellido, email, telefono):
        self.tipo_id = tipo_id
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
    
    def insertar(self):
        c = Conexion()

        with c.cursor() as cursor:
            cursor.execute("INSERT INTO usuario (tipo_id, rut, nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)", 
                (self.tipo_id, self.rut, self.nombre, self.apellido, self.email, self.telefono))
            c.commit()

    def actualizar(self):
        c = Conexion()

        with c.cursor() as cursor:
            cursor.execute("UPDATE usuario SET tipo_id = %s, rut = %s, nombre = %s, apellido = %s, email = %s, telefono = %s WHERE id = %s", 
                (self.tipo_id, self.rut, self.nombre, self.apellido, self.email, self.telefono, self.id))
            c.commit()
            c.close()
    
    def eliminar(self):
        c = Conexion()

        with c.cursor() as cursor:
            cursor.execute("DELETE FROM usuario WHERE rut = %s", (self.rut))
            c.commit()
            c.close()

    def consultar(self):
        c = Conexion()

        with c.cursor() as cursor:
            cursor.execute("SELECT id, tipo_id, rut, nombre, apellido, email, telefono FROM usuario WHERE rut = %s", (self.rut))
            resultado = cursor.fetchone()
            c.close()
            return resultado

    def listar(self):
        c = Conexion()

        with c.cursor() as cursor:
            cursor.execute("SELECT id, tipo_id, rut, nombre, apellido, email, telefono FROM usuario")
            resultado = cursor.fetchall()
            c.close()
            return resultado