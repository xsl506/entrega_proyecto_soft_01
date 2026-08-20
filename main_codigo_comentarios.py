# ============================================================================
# Curso: SOFT-01 Principios de Programación 1
# Proyecto Final
# PROGRAMA:  Sistema de tiquetería
# Descripción: Permite al usuario consultar eventos registrados en la plataforma, así como la compra de tiquetes.
# ============================================================================

# Funciones

# Utilidades dentro de Compra de entradas
def validar_correo(correo_electronico): # Función Basada en ejercicio Fase 1 - Ejercicio 3
    es_valido = True # declaramos variable, la cual valida si el correo es válido o no
    mensaje_error = None 
    errores = []

    if len(correo_electronico) == 0:    # Verificamos que se ingresó algún dato en la variable correo_electronico // calculamos la cantidad de elementos utilizando len()
        es_valido = False
        mensaje_error = "CORREO INVÁLIDO: No se ingresó ningún valor"  
        return es_valido, mensaje_error  # Retornamos el valor de la variable es_valido y el mensaje de error
    
    # Las variables detalladas a continuación son contadores para detectar caracteres no permitidos en el correo electrónico.
    tiene_espacio = correo_electronico.count(" ") > 0
    tiene_exclamacion = correo_electronico.count("!") > 0
    tiene_numeral = correo_electronico.count("#") > 0
    tiene_una_arroba = correo_electronico.count("@") == 1 # Contador para validar que el correo tiene exactamente una única @ (arroba)
    
    if not (tiene_espacio or tiene_exclamacion or tiene_numeral or not tiene_una_arroba):  # Verificamos que el valor ingresado comocorreo_electronico cumpla con las condiciones de validación, si no cumple, se le indica al usuario que el correo ingresado es inválido 
        # VALIDACIÓN de la estructura del usuario y dominio
        # ========================================================================
        partes = correo_electronico.split("@")     # Vamos a dividir antes/después del @ para obtener usuario y dominio
        usuario = partes[0]     # Usuario (antes del @)
        dominio = partes[1]     # Dominio (después del @)
        
        if len(usuario) == 0:   # Validamos que el Usuario no esta vacío
            es_valido = False
            errores.append("Error: No hay caracteres antes del @")
        elif len(dominio) == 0:   # Validamos que si hay valores después del @, que Dominio no este vacío
            es_valido = False
            errores.append("Error: No hay caracteres después del @")

        if es_valido and len(dominio) > 0: # condicional para validar la estructura del dominio
            if "." not in dominio: # Validamos que hay punto como parte del dominio
                es_valido = False
                errores.append("Error: El dominio debe contener un punto (.)")

            elif ".." in dominio: # Validar que NO hay puntos consecutivos luego del dominio
                es_valido = False
                errores.append("Error: El dominio contiene puntos consecutivos (..)")
            
            elif dominio.count(".") != 1: # Validamos que solamente hay 1 punto en dominio
                es_valido = False
                errores.append( f"Error: El dominio contiene {dominio.count('.')} puntos!")

        if es_valido and "." in dominio and dominio.count(".") == 1:  # Validamos nombre y extensión del dominio
            partes_dominio = dominio.split(".")     # split(".") divide el dominio por puntos
            nombre_dominio = partes_dominio[0]      # Antes del punto
            extension_dominio = partes_dominio[1]   # Después del punto

            if len(nombre_dominio) == 0:   # Validamos que el nombre del dominio no está vacío
                es_valido = False
                errores.append("Error: El nombre del dominio está vacío")

            elif len(extension_dominio) == 0:   # Validamos que la extensión no está vacía
                es_valido = False
                errores.append("Error: La extensión del dominio está vacía")
        
            else: # Validamos si el dominio es válido, según la lista de dominios permitidos (com, net, org)
                dominios_validos = ["com", "net", "org"] # Validamos que el dominio es uno de los valores permitidos de la lista creada
                            
                if extension_dominio in dominios_validos: # RESULTADO si el dominio del CORREO ES VÁLIDO
                    es_valido = True
                    errores.append( ""             )
                else: # RESULTADOS detallados si el CORREO NO ES VÁLIDO
                    es_valido = False
                    errores.append( f"Error: El dominio '.{extension_dominio}' no es válido")
    else:
        es_valido = False
        if tiene_espacio:           # No cumple la condición de no contener espacios, mostrar error al usuario
            errores.append("Error: El correo ingresado contiene espacios")
        if tiene_exclamacion:       # No cumple la condición de no contener signos exclamación, mostrar error al usuario
            errores.append("Error: El correo contiene el carácter (!)")
        if tiene_numeral:           # No cumple la condición de no contener signos de numeral, mostrar mj de error al usuario
            errores.append("Error: El correo contiene el carácter (#)")
        if not tiene_una_arroba:    # No cumple la condición de solo un @, mostrar error al usuario
            errores.append("Error: El correo debe contener únicamente un símbolo de arroba (@)")
    return es_valido, errores  # Retornamos el valor de la variable es_valido y el mensaje de error

def validar_edad(edad): # Función Basada en ejercicio Fase 1 - Ejercicio 1
    if edad.isnumeric() == False:
        return False, "Edad inválida: Debe ser un número entero."
    elif int(edad) < 18:
        return False, "No se permite el acceso a menores de edad."
    else:
        return True, ""
    
# Funcion para Registrar Nuevos eventos, submenú Admin
def registrar_evento(): # basado en el Ejercicio 3, fase 2
    temp = []
    print("\n===== Registro de Evento =====")  #Mostramos el título para el registro de eventos
    titulo = input("Título del evento: ")
    fecha = input("Fecha del evento: ")

    print("¿El evento es solo para mayores de edad?")
    print("1. Sí")
    print("2. No")
    
    evento_mayores = int(input("Seleccione una opción: "))  #Solicitamos al usuario que seleccione una opción para determinar si el evento es solo para mayores de edad o no
    while evento_mayores != 1 and evento_mayores != 2:      #Iniciamos un ciclo condicional para validar la opción ingresada por el usuario y definir si el evento es solo para mayores de edad o no
        print("Opción inválida.")            #En caso de que el usuario ingrese una opción diferente a 1 ó 2, se le indica que la opción es inválida y se le solicita nuevamente que seleccione una opción
        evento_mayores = int(input("Seleccione una opción (1 o 2): "))  #Imprimimos el mensaje de error y solicitamos nuevamente que seleccione una opción válida

    espacios_totales = int(input("Cantidad total de espacios: "))
    while espacios_totales <= 0:                            #Iniciamos un ciclo condicional para validar que la cantidad total de espacios ingresada por el usuario sea mayor que 0
        print("La cantidad total de espacios debe ser mayor que 0.")
        espacios_totales = int(input("Cantidad total de espacios: "))
    espacios_disponibles = int(input("Cantidad de espacios disponibles: "))

    while espacios_disponibles < 0 or espacios_disponibles > espacios_totales:  #Iniciamos un ciclo condicional para validar que la cantidad de espacios disponibles ingresada por el usuario sea mayor o igual a 0 y menor o igual a la cantidad total de espacios disponibles
        print("Cantidad de espacios disponibles inválida.")
        espacios_disponibles = int(input("Cantidad de espacios disponibles: "))

    # Precios para todas las entradas
    precio_vip = float(input("Precio de boleto VIP: "))
    while precio_vip < 0:                                   #Iniciamos un ciclo condicional para validar que el precio del boleto VIP ingresado por el usuario sea mayor o igual a 0
        print("El precio del boleto VIP debe ser mayor o igual a 0.")
        precio_vip = float(input("Precio de boleto VIP: "))
    precio_preferencial = float(input("Precio de boleto Preferencial: "))
    while precio_preferencial < 0:                          #Iniciamos un ciclo condicional para validar que el precio del boleto Preferencial ingresado por el usuario sea mayor o igual a 0
        print("El precio del boleto Preferencial debe ser mayor o igual a 0.")
        precio_preferencial = float(input("Precio de boleto Preferencial: "))
    precio_general = float(input("Precio de boleto General: "))
    while precio_general < 0:                               #Iniciamos un ciclo condicional para validar que el precio del boleto General ingresado por el usuario sea mayor o igual a 0
        print("El precio del boleto General debe ser mayor o igual a 0.")
        precio_general = float(input("Precio de boleto General: "))

    print("\n¿Desea registrar otro evento?")
    print("1. Sí")
    print("2. No")

    eventos_disponibles.append([titulo, fecha, "true" if evento_mayores == 1 else "false", espacios_totales, espacios_disponibles, precio_vip, precio_preferencial, precio_general])  #Agregamos el evento registrado a la lista de eventos disponibles

    evento_adicional = int(input("Seleccione una opción: "))
    if evento_adicional == 1:
        registrar_evento()  #Si el usuario desea registrar otro evento, se llama a la función nuevamente

def eliminar_evento(): # Funcion para eliminar eventos, submenú Admin
    print("\n===== Borrar Evento =====")  #Mostramos el título para borrar de la lista de eventos
    titulo = input("Ingrese el título del evento a borrar: ")  #Solicitamos al usuario que ingrese el título del evento que desea borrar
    for evento in eventos_disponibles:  #Iniciamos un ciclo para recorrer la lista de eventos disponibles
        if evento[0] == titulo:  #Si el título del evento ingresado por el usuario coincide con algún evento en la lista de eventos disponibles
            eventos_disponibles.remove(evento)  #Eliminamos el evento de la lista de eventos disponibles
            print(f"Evento '{titulo}' borrado exitosamente.")  #Mostramos un mensaje indicando que el evento fue borrado exitosamente
            return  #Salimos de la función
    print(f"No se encontró ningún evento con el título '{titulo}'.")  #Si no se encuentra ningún evento con el título ingresado por el usuario, mostramos un mensaje de error indicando que no se encontró ningún evento con ese título

def modificar_evento(): # Funcion para editar los eventos de la Lista, submenú Admin
    print("\n===== Modificar Evento =====")  #Mostramos el título para modificar eventos
    titulo = input("Ingrese el título del evento a modificar: ")  #Solicitamos al usuario que ingrese el título del evento que desea modificar
    for evento in eventos_disponibles:  #Iniciamos un ciclo para recorrer la lista de eventos disponibles
        if evento[0] == titulo:  #Si el título del evento ingresado por el usuario coincide con algún evento en la lista de eventos disponibles
            print(f"Evento encontrado: {evento}")  #Mostramos un mensaje indicando que se encontró el evento y mostramos los detalles del mismo
            nuevo_titulo = input("Ingrese el nuevo título del evento (deje en blanco para no cambiar): ")  #Solicitamos al usuario que ingrese el nuevo título del evento, si desea cambiarlo
            if nuevo_titulo:  #Si el usuario ingresó un nuevo título
                evento[0] = nuevo_titulo  #Actualizamos el título del evento en la lista de eventos disponibles
            nueva_fecha = input("Ingrese la nueva fecha del evento (deje en blanco para no cambiar): ")  #Solicitamos al usuario que ingrese la nueva fecha del evento, si desea cambiarla
            if nueva_fecha:  #Si el usuario ingresó una nueva fecha
                evento[1] = nueva_fecha  #Actualizamos la fecha del evento en la lista de eventos disponibles
            print("¿El evento es solo para mayores de edad? (deje en blanco para no cambiar)")  #Solicitamos al usuario que indique si el evento es solo para mayores de edad, si desea cambiarlo
            print("1. Sí")
            print("2. No")
            evento_mayores = input("Seleccione una opción: ")  #Solicitamos al usuario que seleccione una opción para determinar si el evento es solo para mayores de edad o no
            if evento_mayores == "1":  #Si el usuario seleccionó la opción 1, actualizamos el valor correspondiente en la lista de eventos disponibles
                evento[2] = "true"
            elif evento_mayores == "2":  #Si el usuario seleccionó la opción 2, actualizamos el valor correspondiente en la lista de eventos disponibles
                evento[2] = "false"
            nuevos_espacios_totales = input("Ingrese la nueva cantidad total de espacios (deje en blanco para no cambiar): ")  #Solicitamos al usuario que ingrese la nueva cantidad total de espacios, si desea cambiarla
            if nuevos_espacios_totales:  #Si el usuario ingresó una nueva cantidad total de espacios
                evento[3] = int(nuevos_espacios_totales)  #Actualizamos la cantidad total de espacios en la lista de eventos disponibles
            nuevos_espacios_disponibles = input("Ingrese la nueva cantidad de espacios disponibles (deje en blanco para no cambiar): ")  #Solicitamos al usuario que ingrese la nueva cantidad de espacios disponibles, si desea cambiarla
            if nuevos_espacios_disponibles:  #Si el usuario ingresó una nueva cantidad de espacios disponibles
                evento[4] = int(nuevos_espacios_disponibles)  #Actualizamos la cantidad de espacios disponibles en la lista de eventos disponibles
            nuevo_precio_vip = input("Ingrese el nuevo precio de boleto VIP (deje en blanco para no cambiar): ")  #Solicitamos al usuario que ingrese el nuevo precio del boleto VIP, si desea cambiarlo
            if nuevo_precio_vip:  #Si el usuario ingresó un nuevo precio del boleto VIP
                evento[5] = float(nuevo_precio_vip)  #Actualizamos el precio del boleto VIP en la lista de eventos disponibles
            nuevo_precio_preferencial = input("Ingrese el nuevo precio de boleto Preferencial (deje en blanco para no cambiar): ")  #Solicitamos al usuario que ingrese el nuevo precio del boleto Preferencial, si desea cambiarlo
            if nuevo_precio_preferencial:  #Si el usuario ingresó un nuevo precio del boleto Preferencial
                evento[6] = float(nuevo_precio_preferencial)  #Actualizamos el precio del boleto Preferencial en la lista de eventos disponibles
            nuevo_precio_general = input("Ingrese el nuevo precio de boleto General (deje en blanco para no cambiar): ")  #Solicitamos al usuario que ingrese el nuevo precio del boleto General, si desea cambiarlo
            if nuevo_precio_general:  #Si el usuario ingresó un nuevo precio del boleto General
                evento[7] = float(nuevo_precio_general)  #Actualizamos el precio del boleto General en la lista de eventos disponibles
            print(f"Evento '{titulo}' modificado exitosamente.")  #Mostramos un mensaje indicando que el evento fue modificado exitosamente
            return  #Salimos de la función
    print(f"No se encontró ningún evento con el título '{titulo}'.")  #Si no se encuentra ningún evento con el título ingresado por el usuario, mostramos un mensaje indicando que no se encontró ningún evento con ese título

# Funcion para mostrar la lista de eventos, submenú Admin
def mostrar_resumen_todos_los_eventos(eventos_disponibles, entradas_compradas):
    print("\n" + "="*50)
    print("          RESUMEN GLOBAL DE TODOS LOS EVENTOS")
    print("="*50)

    for evento in eventos_disponibles:
        nombre = evento[0]
        cantidad_inicial = evento[3]  # Espacios totales iniciales
        cantidad_disponible = evento[4]  # Espacios disponibles actualmente
        
        # Precios de las entradas según la estructura de la lista
        precio_vip = evento[5]
        precio_preferencial = evento[6]
        precio_general = evento[7]

        total_vendidas = 0
        vendidas_general = 0
        vendidas_preferencial = 0
        vendidas_vip = 0

        # Contador de las entradas vendidas para este evento específico
        for entrada in entradas_compradas:
            if entrada[0].lower() == nombre.lower():
                total_vendidas += 1
                tipo_entrada = entrada[2].lower()
                
                if tipo_entrada == "general":
                    vendidas_general += 1
                elif tipo_entrada == "preferencial":
                    vendidas_preferencial += 1
                elif tipo_entrada == "vip":
                    vendidas_vip += 1

        # Calculamos los espacios disponibles y recaudación de dinero
        monto_recaudado = (vendidas_vip * precio_vip) + \
                          (vendidas_preferencial * precio_preferencial) + \
                          (vendidas_general * precio_general)

        # Mostramos las estadísticas de cada evento, luego de hacer compras
        print(f"\n* Nombre del evento: {nombre}")
        print(f"  - Cantidad inicial de espacios: {cantidad_inicial}")
        print(f"  - Cantidad de espacios disponibles: {cantidad_disponible}")
        print(f"  - Cantidad total de entradas vendidas: {total_vendidas}")
        print(f"  - Cantidad de entradas General vendidas: {vendidas_general}")
        print(f"  - Cantidad de entradas Preferencial vendidas: {vendidas_preferencial}")
        print(f"  - Cantidad de entradas VIP vendidas: {vendidas_vip}")
        print(f"  - Monto total recaudado: ${monto_recaudado}")
        print("-" * 50)

# Funciones para el Menú de Usuario
def mostrar_evento_especifico(): # Función creada para mostrar detalles de un evento específico 
    print("\n===== Mostrar Evento Específico =====")  #Mostramos el título para mostrar un evento específico
    titulo = input("Ingrese el título del evento a mostrar: ")  #Solicitamos al usuario que ingrese el título del evento que desea mostrar
    for evento in eventos_disponibles:  #Iniciamos un ciclo para recorrer la lista de eventos disponibles
        if evento[0] == titulo:  #Si el título del evento ingresado por el usuario coincide con algún evento en la lista de eventos disponibles
            print(f"Evento encontrado: {evento[0]}")  #Mostramos un mensaje indicando que se encontró el evento y mostramos los detalles del mismo
            print(f"Fecha: {evento[1]}")  #Mostramos la fecha del evento
            print(f"Evento solo para mayores de edad: {'Sí' if evento[2] == 'true' else 'No'}")  #Mostramos si el evento es solo para mayores de edad o no
            print(f"Cantidad total de espacios: {evento[3]}")  #Mostramos la cantidad total de espacios del evento
            print(f"Cantidad de espacios disponibles: {evento[4]}")  #Mostramos la cantidad de espacios disponibles del evento
            print(f"Precio de boleto VIP: {evento[5]}")  #Mostramos el precio del boleto VIP del evento
            print(f"Precio de boleto Preferencial: {evento[6]}")  #Mostramos el precio del boleto Preferencial del evento
            print(f"Precio de boleto General: {evento[7]}")  #Mostramos el precio del boleto General del evento
            return  #Salimos de la función
    print(f"No se encontró ningún evento con el título '{titulo}'.")  #Si no se encuentra ningún evento con el título ingresado por el usuario, mostramos un mensaje indicando que no se encontró ningún evento con ese título

def mostrar_espacios_evento(): # Función creada para mostrar los espacios disponibles de un evento específico 
    print("\n===== Mostrar Evento Específico =====")  #Mostramos el título de un evento específico
    titulo = input("Ingrese el título del evento a mostrar: ")  #Solicitamos al usuario que ingrese el título del evento que desea mostrar
    for evento in eventos_disponibles:  #Iniciamos un ciclo para recorrer la lista de eventos disponibles
        if evento[0] == titulo:  #Si el título del evento ingresado por el usuario coincide con algún evento en la lista de eventos disponibles
            print(f"Evento encontrado: {evento[0]}")  #Mostramos un mensaje indicando que se encontró el evento y mostramos los detalles del mismo
            print(f"Cantidad de espacios disponibles: {evento[4]}")  #Mostramos la cantidad de espacios disponibles del evento
            return  #Salimos de la función
    print(f"No se encontró ningún evento con el título '{titulo}'.")  #Si no se encuentra ningún evento con el título ingresado por el usuario, mostramos un mensaje indicando que no se encontró ningún evento con ese título

def comprar_entrada(): # Función creada para comprar entradas de un evento
    print("\n===== Comprar Entrada =====")  #Muestra el título del evento para comprar entradas
    titulo = input("Ingrese el título del evento para comprar entrada: ")  #Solicitamos al usuario que ingrese el título del evento para comprar entrada
    for evento in eventos_disponibles:  #Iniciamos un ciclo para recorrer la lista de eventos disponibles
        if evento[0] == titulo:  #Si el título del evento ingresado por el usuario coincide con algún evento en la lista de eventos disponibles
            print(f"Evento encontrado: {evento[0]}")  #Mostramos un mensaje indicando que se encontró el evento y mostramos los detalles del mismo
            print(f"Fecha: {evento[1]}")  #Mostramos la fecha del evento
            print(f"Evento solo para mayores de edad: {'Sí' if evento[2] == 'true' else 'No'}")  #Mostramos si el evento es solo para mayores de edad o no
            print(f"Cantidad total de espacios: {evento[3]}")  #Mostramos la cantidad total de espacios del evento
            print(f"Cantidad de espacios disponibles: {evento[4]}")  #Mostramos la cantidad de espacios disponibles del evento
            print(f"Precio de boleto VIP: {evento[5]}")  #Mostramos el precio del boleto VIP del evento
            print(f"Precio de boleto Preferencial: {evento[6]}")  #Mostramos el precio del boleto Preferencial del evento
            print(f"Precio de boleto General: {evento[7]}")  #Mostramos el precio del boleto General del evento

            if evento[4] <= 0:  #Validamos si hay espacios disponibles para el evento
                print("No hay espacios disponibles para este evento.")  #Si no hay espacios disponibles para el eventmostramos un mensaje indicando que no hay espacios disponibles
                return  #Salimos de la función

            #TODO REVISAR VALIDACION EN CICLO
            print("Digite su coreo electrónico para continuar con la compra: ")  #Solicitamos al usuario que ingrese su correo electrónico para continuar con la compra

            while True:
                correo_electronico = input("Correo electrónico: ")
                correo_es_valido, mensajes_error_correo = validar_correo(correo_electronico)
                if correo_es_valido == False:  #Validamos que el correo electrónico ingresado por el usuario sea válido
                    for mensaje in mensajes_error_correo:
                        print(mensaje)  #Si el correo electrónico ingresado por el usuario no es válido, mostramos un mensaje indicando que es inválido
                else:
                    break

            # basado en el Ejercicio 1 fase 1, validamos la mayoría de edad antes de comprar entradas
            print("Digite su edad para continuar con la compra: ")  #Solicitamos al usuario que ingrese su edad para continuar con la compra
            edad = input("Edad: ")
            while validar_edad(edad)[0] == False:  #Validamos que la edad ingresada por el usuario sea válida
                print(validar_edad(edad)[1])  #Si la edad ingresada por el usuario no es válida, mostramos un mensaje indicando que es inválida
                edad = input("Edad: ")  #Solicitamos al usuario que ingrese nuevamente su edad

            tipo_entrada = input("Ingrese el tipo de entrada (VIP, Preferencial, General): ")  #Solicitamos al usuario que ingrese el tipo de entrada que desea comprar
            while tipo_entrada not in ["VIP", "Preferencial", "General"]:  #Validamos que el tipo de entrada ingresado pusuario sea válido
                tipo_entrada = input("Tipo de entrada inválido. Ingrese el tipo de entrada (VIP, Preferencial, General): ")  #tipo de entrada ingresado por el usuario no es válido, mostramos un mensaje indicando que es inválido
                return  #Salimos de la función

            print("Cuantas entradas desea comprar?")  #Solicitamos al usuario que ingrese la cantidad de entradas que desea comprar
            cantidad_entradas = int(input("Cantidad de entradas: "))
            while cantidad_entradas <= 0 or cantidad_entradas > evento[4]:  #Validamos que la cantidad de entradas ingresada por el usuario sea mayor que 0 y menor o igual a la cantidad de espacios disponibles para el evento
                print(f"La cantidad de entradas debe ser mayor que 0 y menor o igual a {evento[4]}.")  #Si la cantidad de entradas ingresada por el usuario no es válida, mostramos un mensaje indicando que es inválida
                cantidad_entradas = int(input("Cantidad de entradas: "))  #Solicitamos al usuario que ingrese nuevamente la cantidad de entradas que desea comprar

            print("Con cuanto efectivo cuenta, compadre?")  #Solicitamos al usuario que ingrese la cantidad de efectivo con la que cuenta para comprar las entradas
            efectivo = float(input("Efectivo: "))
            precio_total = 0  #Inicializamos la variable precio_total en 0
            if tipo_entrada == "VIP":  #Si el tipo de entrada ingresado por el usuario es VIP, calculamos el precio total multiplicando la cantidad de entradas por el precio del boleto VIP
                precio_total = cantidad_entradas * evento[5]
            elif tipo_entrada == "Preferencial":  #Si el tipo de entrada ingresado por el usuario es Preferencial, calculamos el precio total multiplicando la cantidad de entradas por el precio del boleto Preferencial
                precio_total = cantidad_entradas * evento[6]
            elif tipo_entrada == "General":  #Si el tipo de entrada ingresado por el usuario es General, calculamos el precio total multiplicando la cantidad de entradas por el precio del boleto General
                precio_total = cantidad_entradas * evento[7]
            if efectivo < precio_total:  #Validamos que la cantidad de efectivo ingresada por el usuario sea mayor o igual al precio total de las entradas
                print(f"No tiene suficiente efectivo amix. El precio total es: {precio_total}")  #Si la cantidad de efectivo ingresada por el usuario no es suficiente, mostramos un mensaje indicando que no tiene suficiente efectivo y mostramos el precio total de las entradas
                return  #Salimos de la función
            else:  #Si la cantidad de efectivo ingresada por el usuario es suficiente, mostramos un mensaje indicando que la compra fue exitosa y mostramos el precio total de las entradas
                print(f"Compra exitosa! El precio total es: {precio_total}")  #Mostramos un mensaje indicando que la compra fue exitosa y mostramos el precio total de las entradas
                evento[4] -= cantidad_entradas  #Actualizamos la cantidad de espacios disponibles para el evento restando la cantidad de entradas compradas
                entradas_compradas.append([titulo, "true" if evento[2] == "true" else "false", tipo_entrada])  #Agregamos la compra a la lista de entradas compradas
                return  #Salimos de la función
    print(f"No se encontró ningún evento con el título '{titulo}'.")  #Si no se encuentra ningún evento con el título ingresado por el usuario, mostramos un mensaje indicando que no se

# Datos Iniciales para Lista de eventos
eventos_disponibles = [["Gorillaz", "2026-09-15", "true", 100, 20, 30, 13, 22], ["Coldplay", "2024-02-20", "false", 100, 20, 30, 16, 25], ["Imagine Dragons", "2027-11-05", "true", 100, 20, 30, 19, 28]]
entradas_compradas = [["Gorillaz", "true", "VIP"], ["Coldplay", "false", "General"], ["Imagine Dragons", "true", "Preferencial"], ["Gorillaz", "true", "VIP"]]

#registrar_evento()  # Llamada inicial a la función para registrar eventos

# Condicional / Loop Principal
current_module = None
while True:
    # Menu Principal Inicial del Programa
    if not current_module:
        print("\n====== Seleccione módulo ======")
        print("1. Menú del Usuario")
        print("2. Menú del Administrador")
        print("3. Salir")
        print("===========================")
        choice = input("\Seleccione una Opción: ")
        match choice:
            case "1":
                current_module = "usuario"
            case "2":
                current_module = "admin"
            case "3":
                print("Saliendo del Menú...")
                mostrar_resumen_todos_los_eventos(eventos_disponibles, entradas_compradas)  # Mostramos el resumen general de todos los eventos antes de salir
                input("Ingrese Enter para salir del Menú...")
                break
            case _:
                print("Opción Inválida. Intente nuevamente.")
    elif current_module == "usuario":
        print("\n===== MENÚ DEL USUARIO =====")   
        print("1. Consultar Evento")
        print("2. Comprar boletos")
        print("3. Consultar espacios disponibles")
        print("4. Volver al menú principal")
        print("===========================")  
        opcion = int(input("\nSeleccione una opción: "))    #Solicitamos al usuario que seleccione una opción del menú usuario
            # Inicio del ciclo condicional para determinar qué opción seleccionó el usuario

        if opcion == 1:     
            mostrar_evento_especifico()  # Mostramos la información de un evento específico
        elif opcion == 2:
            comprar_entrada()  # Permite al usuario comprar boletos para un evento
        elif opcion == 3:
            mostrar_espacios_evento()  # Mostramos la cantidad de espacios disponibles para un evento específico
        elif opcion == 4:
            current_module = None  # Volvemos al menú principal
        else:
            print("Opción inválida!")
    elif current_module == "admin":
        print("\n===== MENÚ DEL ADMINISTRADOR =====")
        print("1. Registrar evento")
        print("2. Modificar evento")
        print("3. Eliminar evento")
        print("4. Volver al menú principal")
        print("=====================================") 

        opcion_usuario = input("Selecciones una opción: ") #Solicitamos información al usuario

        match opcion_usuario:
            case "1":
                registrar_evento()  # Llamada a la función para registrar eventos
            case "2":
                modificar_evento()  # Llamada a la función para modificar eventos
            case "3":
                eliminar_evento()  # Llamada a la función para eliminar eventos
            case "4":
                current_module = None  # Vuelve al menú principal
            case _:
                print("Opción Invalida.")