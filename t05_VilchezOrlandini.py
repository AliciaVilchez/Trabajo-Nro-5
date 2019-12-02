#Ejercicio 01
empleado,nrodias,costo,horas_extra,monto="",0,0.0,0,0.0
empleado=str(input("Ingrese el nombre del empleado:"))
nrodias=int(input("Ingrese numero de dias:"))
costo=float(input("Ingrese costo por dia:"))
horas_extra=int(input("Ingrese nro de horas extra:"))

# PROCESSING
mostrar_salario=(nrodias*costo)+(horas_extra*10)
if(mostrar_salario > 1500):
    print("Mostrar salario")
#fin_if

#Ejercicio 02
cliente,producto,costo_del_producto,descuento,total="","",0.0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese el producto:"))
costo_del_producto=float(input("Ingrese costo del producto:"))
descuento=float(input("Ingrese descuento:"))

#PROCESSING
oferta=costo_del_producto-descuento
if(oferta < 200 ):
    print("Oferta")
#fin_if


#Ejercicio 03
cliente,producto,costo_del_producto,docena,total="","",0.0,0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese el producto:"))
costo_del_producto=float(input("Ingrese costo del producto:"))
docena=float(input("Ingrese la docena:"))

#PROCESSING
precio_al_por_mayor=costo_del_producto*docena
if(precio_al_por_mayor < 500):
    print("Precio al por mayor")
#fin_if

#Ejercicio 04
cliente,cant,costo_euro,total="",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
cant=int(input("Ingrese cantidad:"))
costo_euro=float(input("Ingrese costo del euro:"))

# PROCESSING
total_soles=cant*costo_euro
if(total_soles):
    print("Total soles")
#fin_if


#Ejericio 05
cliente,cant,costo_de_alquiler,total="",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
cant=int(input("Ingrese cantidad:"))
costo_de_alquiler=float(input("Ingrese costo de alquiler:"))

#PROCESSING
costo_de_alquiler=cant*costo_de_alquiler
minimo_costo_de_alquier=(costo_de_alquiler < 750)
if(minimo_costo_de_alquier):
    print("Minimo costo de alquiler")
#fin_if


#Ejercicio 06
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario
buena_calidad_de_tela=(total > 100)
if(buena_calidad_de_tela):
    print("Buena calidad de tela")
#fin_if


#Ejercicio 07
cliente,producto,cant,costo_unit,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese el producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unit=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unit
marcas_originales=(total > 300)
if(marcas_originales):
    print("es marca original")
#fin_if

#Ejercicio 08
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario
consumo_de_gasolina=(total > 150)
if(consumo_de_gasolina):
    print("consumo en exceso de gasolina")
#fin_if

#Ejercicio 09
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario
comprador_compulsivo=(total > 160)
if(comprador_compulsivo):
    print("comprador compulsivo")
#fin_if

#Ejercicio 10
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario
calidad_de_electrodomesticos=(total > 200)
if(calidad_de_electrodomesticos):
    print("calidad de electrodomesticos")
#fin_if


#Ejercicio 11
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario
calidad_de_tortas=(total > 70)
if(calidad_de_tortas):
    print("calidad de toras")
#fin_if


#Ejercicio 12
cliente,productos,cant,precios,total="","",0,0.0,0.0
cliente=input("Ingrese el cliente:")
productos=input("Ingrese productos:")
cant=int(input("Ingrese cantidades:"))
precios=float(input("Ingrese precios:"))

#PROCESSING
total=cant*precios
calidad_de_alimentos=(total > 300)
if(calidad_de_alimentos):
    print("calidad de alimentos")
#fin_if


#Ejercicio 13
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario
consumo_de_gaseosas=(total > 15)
if(consumo_de_gaseosas):
    print("consumidor de gaseosas")
#fin_if


#Ejercicio 14
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario
consumo_de_comida_chatarra=(total > 30)
if(consumo_de_comida_chatarra):
    print("Consumidor de comida chatarra")
#fin_if

#Ejercicio 15
cliente,producto,cant,costo,total="","",0,0.0,0.0
cliente=str(input("Ingrese el cliente:"))
producto=str(input("Ingrese producto:"))
cant=int(input("Ingrese cantidad:"))
costo=float(input("Ingrese costo:"))

#PROCESSING
total=cant*costo
consumo_de_energia=(total > 100)
if(consumo_de_energia):
    print("consumidor de energia")
#fin_if


#Ejercicio 16
alumno,horas_dedicadas_al_estudio_por_dia="",0
alumno=str(input("alumno:"))
horas_dedicadas_al_estudio_por_dia=int(input("horas dedicadas al estudio por dia:"))

#PROCESSING
total_de_horas_por_semana=(horas_dedicadas_al_estudio_por_dia)*7
bajo_rendimiento_academico=(total_de_horas_por_semana < 30)
if(bajo_rendimiento_academico):
    print("Bajo rendimiento academico")
#Fin_if


#Ejercicio 17
alumno,nota1,nota2,nota3,nota4="",0,0,0,0
alumno=str(input("alumno"))
nota1=int(input("nota1"))
nota2=int(input("nota2"))
nota3=int(input("nota3"))
nota4=int(input("nota4"))

#PRECESSING
prom=(nota1+nota2+nota3+nota4)/4
if(prom > 15):
    print("aprobado")
#fin_if

#Ejercicio 18
profesor,numero_horas_que_enseña,costo_por_hora="",0,0
profesor=str(input("profesor"))
numero_horas_que_enseña=int(input("Ingrese nro de horas que enseña"))
costo_por_hora=float(input("Ingrese costo por hora"))

#PROCESSING
sueldo_mensual=numero_horas_que_enseña*costo_por_hora
if(sueldo_mensual > 1500):
    print("bien pagado")
#fin_if

#Ejercicicio 19
hospital,nro_areas,nro_personal_por_area="",0,0
hospital=str(input("Ingresar nombre del hopital"))
nro_areas=str(input("nro_areas"))
nro_personal_por_area=str(input("nro_personal_por_area"))

#PROCESSING
if(nro_areas=="personal capacitado") and (nro_personal_por_area=="postulantes"):
    print("contratado")
#fin_if

#Ejercicio 20
nombre,profesion,edad,tiempo_de_trabajo="","",0,""
nombre=str(input("Ingresar nombre"))
profesion=str(input("profesion"))
edad=int(input("Ingresar edad"))
tiempo_de_trabajo=str(input("tiempo_de_trabajo"))

#PROCESSING
if(profesion=="Doctor")and(tiempo_de_trabajo=="2años"):
    print("Nombrado")
#fin_if


#Ejercicio 21
nombre_equipo,nro_jugadores,nr_copas_ganadas="",0,0
nombre_equipo=str(input("Ingresar nombre del equipo"))
nro_campeonatos=int(input("Ingresar el nro de campeonatos"))
nr_de_campeonatos_ganados=int(input("Ingresar el nro de campeonatos ganados"))

#PROCESSING
Nro_de_copas_ganadas=nro_campeonatos/nr_de_campeonatos_ganados
if(Nro_de_copas_ganadas > 2):
    print("Campeones")
#fin_if

#Ejercicio 23
paciente,tipo_de_atencion,edad,pago_consulta="","",0,""
paciente=str(input("Ingrese el nombre del paciente"))
tipo_de_atencion=str(input("tipo_de_atencion"))
edad=int(input("Ingrese edad"))
pago_consulta=str(input("pago_consulta"))

#PROCESSING
if(tipo_de_atencion=="Particular")and(pago_consulta=="Si"):
    print("No tiene SIS")
#fin_if

#Ejercicio 24
alumno,documento,curso1,curso2,curso3,curso4="","",0,0,0,0
alumno=str(input("Ingrese nombre del alumno"))
documento=str(input("Ingrese nombre del documento"))
curso1=int(input("curso1"))
curso2=int(input("curso2"))
curso3=int(input("curso3"))
curso4=int(input("curso4"))

#PROCESSING
total_de_cursos_matriculados=curso1+curso2+curso3+curso4
if(total_de_cursos_matriculados > 21):
    print("Matriculado")
#fin_if


#Ejercicio 25
titulo,autor,genero_literario,año="","","",0
titulo=str(input("Ingrese el nombre del tituol"))
autor=str(input("autor"))
genero_literario=str(input("genero_literario"))
año=int(input("Ingrese el año"))

#PROCESSING
if(autor=="MarioVargasLllosa")and(genero_literario=="Hispanoamericana"):
    print("Premio Nobel")
#fin_if

#Ejercicio 26
año_actual,nombre,fecha_de_nacimiento=0,"",""
año_actual=int(input("Ingrese año actual"))
nombre=str(input("Ingre nombre"))
fecha_de_nacimiento=int(input("Ingrese fecha de nacimiento"))

#PROCESSING
Edad=año_actual-fecha_de_nacimiento
if(Edad > 18):
    print("Es mayor de edad")
#fin_if

#Ejercicio 27
redsocial,usuario,contraseña="","",0
redsocial=str(input("Ingrese redsocial"))
usuario=str(input("usuario"))
contraseña=int(input("contraseña"))

#PROCESSING
if(usuario=="codigo")and(contraseña=="12345"):
    print("Iniciar sesion")
#fin_if

#Ejercicio 28
cliente,nro_ollas,precio_unitario="",0,0.0
cliente=str(input("Ingrese nombre del cliente"))
nro_ollas=int(input("Ingrese nro de ollas"))
precio_unitario=float(input("Ingrese el precio unitario"))

#PROCESSING
Total_pagar=nro_ollas*precio_unitario
if(Total_pagar):
    print("Ollas de fierro")
#fin_if

#Ejercicio 29
jefe_de_unidad,cargo,sueldo_mensua,nro_faltas="","",0.0,0
jefe_de_unidad=str(input("Ingrese el jefe de unidad"))
cargo=str(input("Ingrese el cargo"))
sueldo_mensual=float(input("Ingrese el suelto mensual"))
nro_faltas=int(input("Ingrese nro de faltas"))

#PROCESSING
descuento=sueldo_mensual-nro_faltas
if(descuento > 500):
    print("Dejar el cargo")
#fin_if


#Ejercicio 30
cuenta,nro_visitas,costo_de_visitas="",0.0,0
cuenta=str(input("Ingrese cuenta"))
nro_visitas=float(input("Ingre el numero de visitas"))
costo_de_visitas=int(input("Ingrese el costo de visitas"))

#PROCESSING
total_ganancia=nro_visitas*costo_de_visitas
if(total_ganancia):
    print("Gracias por su visita")
#fin_if

#Ejercicio 31
cliente,nro_tarjetas,sueldo,costo_tarjeta="",0,0,0
cliente=str(input("Ingrese cliente"))
nro_tarjetas=int(input("Ingrese numero de tarjetas"))
sueldo=int(input("Ingrese sueldo"))
costo_tarjeta=int(input("Ingrese cossto de la tarjeta"))

#PROCESSING
total=sueldo-(nro_tarjetas*costo_tarjeta)
if(total):
    print("descuento con tarjeta")
#fin_if

#Ejercicio 32
youtuber,nro_presentaciones,costo_presentacion="",0,0
youtuber=str(input("Ingrese el nombre del youtuber"))
nro_presentaciones=int(input("Ingrese el nro de presentaciones"))
costo_presentacion=int(input("Ingrese elcosto de presentacion"))

#PROCESSING
total=nro_presentaciones*costo_presentacion
if(total):
    print("Buen monologo")
#fin_if


#Ejercicio 33
cliente,nro_electrodomesticos,costo_electrodomestico="",0,0
cliente=str(input("Ingrese normbre del cliente"))
nro_electrodomesticos=int(input("Ingresar nro de electrodomesticoas"))
costo_electrodomestico=int(input("Ingrese costo de los electrodomesticos"))

#PROCESSING
total_pagar=nro_electrodomesticos*costo_electrodomestico
if(total_pagar > 3000):
    print("Carsa")
#fin_if


#Ejercicio 34
trabajador,profesion,nro_declaraciones_sunat,costo_por_declaraciones="","",0,0
trabajador=str(input("Ingrese el nombre del trabajador"))
profesion=str(input("Ingrese profesion"))
nro_declaraciones_sunat=int(input("Ingrese el nuro de declaraciones a la sunat"))
costo_por_declaraciones=int(input("Ingrese el costo por declarar"))

#PROCESSING
cobrar=nro_declaraciones_sunat*costo_por_declaraciones
if(cobrar > 500):
    print("Buen contador")
#fin_if


#Ejercicio 35
trabajador,profesion,nro_casos,costo_juicio="","",0,0
trabajador=str(input("Ingrese el nombre el trabajador"))
profesion=str(input("Ingrese el nombre de la profesion"))
nro_casos=int(input("Ingrese el nro de casoso"))
costo_juicio=int(input("Ingrese el costo de cada juicio"))

#PROCESSING
total_cobrar=nro_casos*costo_juicio
if(total_cobrar > 700):
    print("Buen abogado")
#fin_if


#Ejercicio 36
clinica,paciente,edad,costo_consulta,="","",0,0
clinica=str(input("Ingrese el nombre de la clinita"))
paciente=str(input("Ingrese el nombre del paciente"))
edad=str(input("edad"))
costo_consulta=str(input("costo_consulta"))

#PROCESSING
if(edad=="50años")and(costo_consulta=="No paga"):
    print("oferta")
#fin_if


#Ejercicio 37
laboratorio,paciente,costo_analisis,consulta="","",0,0
laboratorio=str(input("Ingrese nombre del laboratorio"))
paciente=str(input("Ingrese nombre del paciente"))
costo_analisis=int(input("Ingrese el costo del analisis"))
consulta=int(input("Ingrese consulta"))

#PROCESSING
pagar=costo_analisis+consulta
if(pagar < 100):
    print("Barato")
#fin_if


#Ejercicio 38
vendedor,precio_al_vender,invertido="",0,0
venderdor=str(input("Ingrese nombre del vendedor"))
invertido=int(input("Ingresar lo invertido"))
precio_al_vender=int(input("Ingresar el precio"))

#PROCESSING
ganancia=precio_al_vender-invertido
if(ganancia > 30):
    print("Gano")
#fin_if


#Ejercicio 39
cliente,precio_celular,descuento="",0,0
cliente=str(input("Ingrese el nombre del cliente"))
precio_celular=int(input("Ingrese el precio"))
descuento=int(input("Ingrese el descuento"))

#PROCESSING
precio_con_descuento=precio_celular-descuento
if(precio_con_descuento):
    print("Aprovecha el descuento")
#fin_if


#Ejercicio 40
cliente,costo_envio,precio_producto="",0,0.0
cliente=str(input("Ingrese nombre del cliente"))
costo_envio=int(input("Ingrese el costo de envio"))
precio_producto=float(input("Ingrese precio del producto"))

#PROCESSING
pagar_producto=costo_envio+precio_producto
if(pagar_producto):
    print("Confiable")
#fin_if


#Ejercicio 41
negocio,precio_caja_cerveza,nro_cajas_fines_semana="",0,0
negocio=str(input("Ingrese el nombre del negocio"))
precio_caja_cerveza=int(input("Ingrese el precio de la caja de cerveza"))
nro_cajas_fines_semana=int(input("Ingrese el nro de cajas que consumen los fines de semana"))

#PROCESSING
consumo_soles=precio_caja_cerveza*nro_cajas_fines_semana
if(consumo_soles):
    print("Alcoholicos")
#fin_if


#Ejercicio 42
nombre,clinica_dental,precio_de_los_brackets,precio_curaciones="","",0,0
nombre=str(input("Ingrese el nombre del paciente"))
clinica_dental=str(input("Ingrese el nombre de la clinica dental"))
precio_de_los_brackets=int(input("Ingrese el precio de los brackets"))
precio_curaciones=int(input("Ingrese precio de curaciones de los dientes"))

#PROCESSING
precio_total=precio_de_los_brackets+precio_curaciones
if(precio_total):
    print("Por una sonrisa mejor")
#fin_if


#Ejercicio 43
empresa,destino,nro_pasajeros,costo_pasaje="","",0,0
empresa=str(input("Ingresar el nombre de la empresa"))
destino=str(input("Ingrese el nombre del destino"))
nro_pasajeros=int(input("Ingrese nro de pasajeros"))
costo_pasaje=int(input("Ingrese el costo de los pajes"))

#PROCESSING
total_dinero_obteniado_en_un_dia=nro_pasajeros*costo_pasaje
if(total_dinero_obteniado_en_un_dia):
    print("Buen viaje")
#fin_if


#Ejercicio 44
nombre_facultad,precio_fut,nro_futs_al_año="",0,0
nombre_facultad=str(input("Ingrese el nombre de la facultad"))
precio_fut=int(input("Ingrese el precio de los futs"))
nro_futs_al_año=int(input("Ingrese el numero de fusts al año"))

#PROCESSING
ingresos_de_futs=precio_fut*nro_futs_al_año
if(ingresos_de_futs):
    print("Ingresos")
#fin_if


#Ejercicio 45
cliente,nro_de_recargas_por_dia,costo_de_la_recarga="",0,0
cliente=str(input("Ingrese el nombre del cliente"))
nro_de_recargas_por_dia=int(input("Ingrese el nro de recargas diarias"))
costo_de_la_recarga=int(input("Ingrese el costo de la recarga"))

#PROCESSING
total_dinero_por_recargas=nro_de_recargas_por_dia*costo_de_la_recarga
if(total_dinero_por_recargas):
    print("Reacarga aqui")
#fin_if


#Ejercicio 46
cliente,nro_de_zapatos_vendidios_al_dia,costo_de_zapatos_de_colegio="",0,0
cliente=str(input("Ingrese el nombre del cliente"))
nro_de_zapatos_vendidios_al_dia=int(input("Ingrese el nro de zapatos vendidos al dia"))
costo_de_zapatos_de_colegio=int(input("Ingrese el costo de zapatos de colegio"))

#PROCESSING
Total=nro_de_zapatos_vendidios_al_dia*costo_de_zapatos_de_colegio
if(Total):
    print("Calzado")
#fin_if


#Ejercicio 47
cliente,nro_horas_trabajadas,costo_por_hora="",0,0
cliente=str(input("Ingrese el nombre del cliente"))
nro_horas_trabajadas=int(input("Ingrese el nro de horas trabajadas"))
costo_por_hora=int(input("Ingrese el costo por hora "))

#PROCESSING
Total_cobrar=nro_horas_trabajadas*costo_por_hora
if(Total_cobrar):
    print("Part Time")
#fin_if


#Ejercicio 48
cliente,precio_del_departamento,pagar_en_cuotas="",0,0
cliente=str(input("Ingrese el nombre del cliente"))
precio_del_departamento=str(input("precio_del_departamento"))
pagar_en_cuotas=str(input("pagar_en_cuotas"))

#PROCESSING
if(precio_del_departamento=="tarjeta")and(pagar_en_cuotas=="descuento"):
    print("Los Portales")
#fin_if


#Ejercicio 49
cliente,precio_de_pelicula,nro_boletos_vendidos="",0,0
cliente=str(input("Ingrese el nombre del cliente"))
precio_de_pelicula=int(input("Ingrese el precio de la pelicula"))
nro_boletos_vendidos=int(input("Ingrese el nro de boletos vendididos"))

#PROCESSING
total=precio_de_pelicula*nro_boletos_vendidos
if(total):
    print("Bienvenidos")
#fin_if


#Ejercicio 50
vendedor,precio_entrada_al_concierto_pre_venta,nro_entradas_vendidas="",0,0
cliente=str(input("Ingrese el nombre del cliente"))
precio_entrada_al_concierto_pre_venta=int(input("Ingrese el precio de la entra en pre venta"))
nro_entradas_vendidas=int(input("Ingrese el nro de entradas vendidas"))

#PROCESSING
total_recaudado_de_la_pre_venta=precio_entrada_al_concierto_pre_venta*nro_entradas_vendidas
if(total_recaudado_de_la_pre_venta):
    print("Vivo por el Rock")
#fin_if





