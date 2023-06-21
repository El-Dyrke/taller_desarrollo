CREATE TABLE tipo_cabanya ( 

    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,  

nombre VARCHAR(60) NOT NULL 

); 

 

 

CREATE TABLE cabanyas (  

  

    id INT(11) NOT NULL AUTO_INCREMENT,  

  

    tipo_id INT(11) NOT NULL,  

  

    precio DECIMAL(10,2) NOT NULL,  

  

    PRIMARY KEY (id),  

  

    CONSTRAINT Fk_tipoc FOREIGN KEY (tipo_id) REFERENCES tipo_cabanya(id) 

  

); 

  

 

CREATE TABLE tipo_usuario ( 

    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,  

nombre VARCHAR(60) NOT NULL 

); 

 

  

CREATE TABLE usuarios (  

  

   id INT(11) NOT NULL AUTO_INCREMENT, 

     

   tipo_id INT(11) NOT NULL, 

  

   rut INT(12) NOT NULL,  

  

   nombre VARCHAR(60) NOT NULL,  

  

   apellido VARCHAR(60) NOT NULL,  

  

   email VARCHAR(60) NOT NULL,  

  

   telefono VARCHAR(20) NOT NULL,  

  

   PRIMARY KEY (id), 

    

   CONSTRAINT Fk_tipou FOREIGN KEY (tipo_id) REFERENCES tipo_usuario(id) 

  

);  

  

  

CREATE TABLE reservas (  

  

   id INT(11) NOT NULL AUTO_INCREMENT,  

  

   cabanya_id INT(11) NOT NULL,  

  

   usuario_id INT(11) NOT NULL,  

  

   fecha_entrada DATE NOT NULL,  

  

   fecha_salida DATE NOT NULL,  

  

   PRIMARY KEY (id),  

  

   FOREIGN KEY (cabanya_id) REFERENCES cabanyas(id),  

  

   CONSTRAINT Fk_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)  

  

);  

  

CREATE TABLE metodo_pago ( 

    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,  

nombre VARCHAR(60) NOT NULL 

); 

 

  

CREATE TABLE pagos (  

  

   id INT(11) NOT NULL AUTO_INCREMENT,  

  

   reserva_id INT(11) NOT NULL,  

  

   fecha_pago DATE NOT NULL,  

  

   monto DECIMAL(10,2) NOT NULL,  

  

   metodo_pago INT(11) NOT NULL,  

  

   PRIMARY KEY (id),  

  

   CONSTRAINT Fk_res FOREIGN KEY (reserva_id) REFERENCES reservas(id), 

   CONSTRAINT Fk_tipop FOREIGN KEY (metodo_pago) REFERENCES metodo_pago(id)  

  

);  