# bibiloteca necesita aplicacion que perimita gestionar el prestamo de libros y calcular el total de libro prestado por cada usuario.
registro_libros :{}
prestamos :{}
def registrar_libro ():
    titulo= input("Ingrese titulo del libro: ")
    autor= input("ingrese el autor: ")
    año= input(int("ingrese el año : ") )
    sku = titulo [:6].upper() + '-' + autor [:3]. upper () + '-' + año 
    if sku in self.libros:
        print("el libro ya esta registrado")
    else :
     self.libros[sku] = {'titulo': titulo,'autor': autor, 'año' : año ,'sku': sku }

    print(f"libro {titulo} registrado exitosamenre con sku {sku}.")
    def prestar_libro (self):
            usuario=input("ingrese el nombre del usuario:")
            sku = input("ingrese el sku del libro:")
            if sku in self.libros and sku not in  self.prestamos:
                self.prestamos[sku] = usuario
                print(f"libro {sku} prestado a  {usuario}.")
            elif sku not in self.libros:
                print("el libro no se encuentra registrado.")
            else:
                print("el libro ya esta prestado.")
                def listar_libros():
                    if not libros:
                        print("no hay libros registrados.")
                    else:
                        for sku, detalles en libros.items ():
                        print (f"titulo : {detalles['titulo]}, autor : {detalles['autor'']}, año: {detalles['año']}, {sku}")
                        def imprimir_reporte_prestamo():
                            if not prestamos():
                                if not prestamos:
                                    print("no hay libros prestados.")
                                else:
                                    for sku, usuario prestamos.items ():
                                    libro= libros [sku]
                                    print(f"usuario : {usuario}, libro: {libro['titulo']}, autor : {libro['autor']}, año: {libro['año']}, sku:{sku}")
                                    def salir_programa():
                                        print("saliendo del programa.")
                                    def menu_principal():
                                      while True: 
                                            print("Biblioteca ")
                                            print("1.registrar un libro")
                                            print("prestar un libro")
                                            print("lista de libro")
                                            print("prestamos")
                                            print("salir")
                                            opcion = input("ingrese su opcion:")
                                            if opcion == '1':
                                                registrar_libro()
                                            elif opcion == '2':
                                                prestar_libro()
                                            elif opcion == '3':
                                                listar_libros()
                                            elif opcion == '4':
                                                imprimir_reporte_prestamo()
                                            elif opcion == '5':
                                                salir_programa()
                                            else: 
                                                print("opcion invalida , intente nuevamente.")
                                                if __name__ == "__main__":
                                                    menu_principal()


                                    
































print("**biblioteca , ingrese opcion**")



funcionalidades: [1.Registar , 2.prestar libro 3. listar todos los libro 4. imprimir reporte de prestamo5. salir programa ]


"registrar_libro": registrar libro,
"prestar_libro": prestar libro,
"listar_todos_los_libros": listar todos los libros,
"imp_report_prestamos": iprimir resportes de prestamos
"salir_programa": salir del programa 



 



