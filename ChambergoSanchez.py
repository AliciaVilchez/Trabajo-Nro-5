#Ejercicio_01
usuario,red_social_1,red_social_2,cant_de_hora_diarias_1,cant_de_hora_diaria_2="","","",0,0
usuario=str(input("usuario:"))
red_social_1=str(input("red social 1:"))
red_social_2=str(input("red social 2: "))
cant_de_hora_diarias_1=int(input("cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("cantidad de horas diarias 2:"))

#Processing
total_de_horas_por_dia=(cant_de_hora_diarias_1+cant_de_hora_diarias_2)
adicto_a_las_redes_sociales=(total_de_horas_por_dia > 12)
if(adicto_a_las_redes_sociales):
    print("Adicto a las redes sociales")
#fin_if


#Ejercicio_02
alumno,horas_dedicadas_al_estudio_por_dia="",0
alumno=str(input("alumno:"))
horas_dedicadas_al_estudio_por_dia=int(input("horas dedicadas al estudio por dia:"))

# Processing
total_de_horas_por_semana=(horas_dedicadas_al_estudio_por_dia)*7
bajo_rendimiento_academico=(total_de_horas_por_semana < 31)
if(bajo_rendimiento_academico):
    print("Bajo rendimiento academico")
#fin_if


#Ejercicio_03
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2="","","",0,0,0.0,0.0
cliente=str(input("cliente:"))
producto1=str(input("producto 1:"))
producto2=str(input("producto 2:"))
cant_de_producto1=str(input("cantidad de producto 1"))
cant_de_producto2=str(input("cantidad de producto 2:"))
cost_uni1=float(input("cosot unitario 1:"))
cost_uni2=float(input("costo unitario 2:"))

# Processing
total=(cant_de_producto1*cost_uni1)+(cant_de_producto2*cost_uni2)
comprador_compulsivo=(total < 180)
if(comprador_compulsivo):
    print("Comprador compulsivo")
#fin_if


#Ejercicio_04
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia="","","",0,0
paciente=str(input("paciente:"))
medicamento_1=str(input("medicamento 1:"))
medicamento_2=str(input("medicamento 2:"))
cant_de_medicamento1_por_dia=str(input("cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=str(input("cantidad de medicamento 2 por dia:"))

# Processing
total_de_medicamentos_por_semana=(cant_de_medicamento1_por_dia*7)+(cant_de_medicamento2_por_dia*7)
automedicacion=(total_de_medicamentos_por_semana > 15 )
if(automedicacion):
    print("Automedicacion")
#fin_if


#Ejercicio_05
nombre,deporte1,deporte2,cant_de_hora_diarias_1,cant_de_hora_diarias_2="","","",0,0
nombre=str(input("nombre:"))
deporte1=str(input("deporte 1:"))
deporte2=str(input("deporte 2:"))
cant_de_hora_diarias_1=str(input("cantidad de hora diarias 1:"))
cant_de_hora_diarias_2=str(input("cantidad de hora diarias 2:"))

# Processing
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2
inclinacion_al_deporte=(total_de_horas_por_semana > 8)
if(inclinacion_al_deporte):
    print("Inclinacion al deporte")
#fin_if


#Ejercicio_06
cliente,producto_1,cantidad_producto_1,cost_uni_1="","",0,0.0
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
cantidad_producto_1=str(input("cantidad producto 1:"))
cost_uni1=float(input("costo unitario 1:"))

# Processing
total=cantidad_producto_1*cost_uni_1
comprador_pasivo=(total > 50)
if(comprador_pasivo):
    print("Comprador pasivo")
#fin_if


#Ejercicio_07
nombre_alumno,nota_1,nota_2,nota_3="",0,0,0
nombre_alumno=str(input("nombre alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))

# Processing
promedio=(nota_1+nota_2+nota_3)/3
nota_aprobatoria=(promedio > 14)
if(nota_aprobatoria):
    print("Nota aprobatoria")
#fin_if


#Ejercicio_08
trabajador,horas_de_jornada_laboral_por_dia,dias_de_jornada_laboral="",0,0
trabajador=str(input("trabajador:"))
horas_de_jornada_laboral_por_dia=str(input("horas de jornada laboral por dia:"))
dias_de_jornada_laboral=str(input("dias de jornada laboral:"))

# Processing
total=horas_de_jornada_laboral_por_dia*dias_de_jornada_laboral
cumplimiento_de_horas_de_trabajo=(total_de_horas_por_semana > 42 )
if(cumplimiento_de_horas_de_trabajo):
    print("Cumplimiento de horas de trabajo")
#fin_if


#Ejercicio_09
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_television_por_dia=str(input("horas dedicadas a la television por dia:"))
horas_dedicadas_a_la_television_por_semana=str(input("horas dedicadas a la television por semana:"))

# Processing
total=horas_dedicadas_a_la_television_por_dia*horas_dedicadas_a_la_television_por_semana
adiccion_a_la_television=(total_de_horas_por_semana > 60 )
if(adiccion_a_la_television):
    print("Adiccion a la television")
#fin_if


#Ejercicio_10
cliente,horas_dedicadas_al_gimnasio_por_dia,horas_dedicadas_al_gimnasio_por_semana="",0,0
cliente=str(input("cliente:"))
horas_dedicadas_al_gimnasio_por_dia=str(input("horas dedicadas al gimnasio por dia:"))
horas_dedicadas_al_gimnasio_por_semana=str(input("horas dedicadas al gimnasio por semana:"))

# Processing
total=horas_dedicadas_al_gimnasio_por_dia*horas_dedicadas_al_gimnasio_por_semana
adiccion_al_gimnasio=(total_de_horas_por_semana > 50 )
if(adiccion_al_gimnasio):
    print("Adiccion al gimnasio")
#fin_if


#Ejercicio_11
cliente,producto_1,producto_2,costo_uni_1,costo_uni_2,cant_de_producto_1,cant_de_producto_2="","","",0.0,0.0,0,0
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
producto_2=str(input("producto 2:"))
costo_uni_1=float(input("costo unitario 1:"))
costo_uni_2=float(input("costo unitario 2:"))
cant_de_producto_1=str(input("cantidad de producto 1:"))
cant_de_producto_2=str(input("cantidad de producto 2:"))

# Processing
total=(costo_uni_1*cant_de_producto_1)+(costo_uni_2*cant_de_producto_2)
comprador_compulsivo=(total > 150)
if(comprador_compulsivo):
    print("Comprador compulsivo")
#fin_if


#Ejercicio_12
alumno,nota_1,nota_2,nota_3,nota_4="",0,0,0,0
alumno=str(input("alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))
nota_4=str(input("nota4:"))

# Processing
promedio=(nota_1+nota_2+nota_3+nota_4)/4
materia_desaprobada=(promedio < 10)
if(materia_desaprobada):
    print("Materia desaprobada")
#fin_if


#Ejercicio_13
cliente,cajetilla_1,cantidad_de_cigarros_por_dia="",0,0
cliente=str(input("cliente:"))
cajetilla_1=str(input("cajetilla 1:"))
cantidad_de_cigarros_por_dia=str(input("cantidad de cigarros por dia:"))

# Processing
cantidad_de_cigarros_por_semana=(cantidad_de_cigarros_por_dia*cajetilla_1)
adiccion_al_cigarro=(cantidad_de_cigarros_por_dia > 4 )
if(adiccion_al_cigarro):
    print("Adiccion al cigarro")
#fin_if


#Ejercicio_14
alumno,nota_01,nota_02,nota_03="",0,0,0
alumno=str(input("alumno:"))
nota_01=str(input("nota 01:"))
nota_02=str(input("nota 02:"))
nota_03=str(input("nota 03:"))

# Processing
promedio=(nota_01+nota_02+nota_03)/3
nota_aprobatoria_ingles=(promedio > 80 )
if(nota_aprobatoria_ingles):
    print("Nota aprobatoria ingles")
#fin_if


#Ejercicio_15
cliente,horas_dedicadas_al_yoga_por_dia,horas_dedicadas_al_yoga_por_semana="",0,0
cliente=str(input("cliente:"))
horas_dedicadas_al_yoga_por_dia=str(input("horas dedicadas al yoga por dia:"))
horas_dedicadas_al_yoga_por_semana=str(input("horas dedicadas al yoga por semana:"))

# Processing
total=horas_dedicadas_al_yoga_por_dia*horas_dedicadas_al_yoga_por_semana
adiccion_al_yoga=(total_de_horas_por_semana > 30 )
if(adiccion_al_yoga):
    print("Adiccion al yoga")
#fin_if


#Ejercicio_16
empleado,horas_de_tardanza_al_trabajo_por_dia,horas_de_tardanza_al_trabajo_por_semana="",0,0
empleado=str(input("empleado:"))
horas_de_tardanza_al_trabajo_por_dia=str(input("horas de tardanza al trabajo por dia:"))
horas_de_tardanza_al_trabajo_por_semana=str(input("horas de tardanza al trabajo por semana:"))

# Processing
total=horas_de_tardanza_al_trabajo_por_dia*horas_de_tardanza_al_trabajo_por_semana
despedido=(total_de_horas_por_semana > 15 )
if(despedido):
    print("Despedido")
#fin_if


#Ejercicio_17
nombre,horas_dedicadas_a_la_musica_por_dia,horas_dedicadas_a_la_musica_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_musica_por_dia=str(input("horas dedicadas a la musica por dia:"))
horas_dedicadas_a_la_musica_por_semana=str(input("horas dedicadas a la musica por semana:"))

# Processing
total=horas_dedicadas_a_la_musica_por_dia*horas_dedicadas_a_la_musica_por_semana
gusto_por_la_musica=(total_de_horas_por_semana > 50 )
if(gusto_por_la_musica):
    print("Gusto por la musica")
#fin_if



#Ejercicio_18
alumna,horas_dedicadas_al_ballet_por_dia,horas_dedicadas_al_ballet_por_semana="",0,0
alumna=str(input("alumna:"))
horas_dedicadas_al_ballet_por_dia=str(input("horas dedicadas al ballet:"))
horas_dedicadas_al_ballet_por_semana=str(input("horas dedicadas al ballet por semana:"))

# Processing
total=horas_dedicadas_al_ballet_por_dia*horas_dedicadas_al_ballet_por_semana
inclinacion_al_ballet=(total_de_horas_por_semana > 40 )
if(inclinacion_al_ballet):
    print("Inclinacion al ballet")
#fin_if


#Ejercicio_19
nombre,horas_viendo_peliculas_por_dia,horas_viendo_peliculas_por_semana="",0,0
nombre=str(input("nombre:"))
horas_viendo_peliculas_por_dia=str(input("horas viendo peliculas por dia:"))
horas_viendo_peliculas_por_semana=str(input("horas viendo peliculas por semana:"))

# Processing
total=horas_viendo_peliculas_por_dia*horas_viendo_peliculas_por_semana
fanatico_de_las_peliculas=(total_de_horas_por_semana > 20 )
if(fanatico_de_las_peliculas):
    print("Fanatico de las peliculas")
#fin_if


#Ejercicio_20
paciente,horas_en_hospital_por_dia,horas_en_hospital_por_semana="",0,0
paciente=str(input("pacinete:"))
horas_en_hospital_por_dia=str(input("horas en hospital por dia:"))
horas_en_hospital_por_semana=str(input("horas en hospital por semana:"))

# Processing
total=horas_en_hospital_por_dia*horas_en_hospital_por_semana
dar_de_alta=(total_de_horas_por_semana > 60 )
if(dar_de_alta):
    print("Dar de alta")
#fin_if


#Ejercicio_21
nombre,horas_dedicadas_a_los_videojuegos_por_dia,horas_dedicadas_a_los_videojuegos_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_los_videojuegos_por_dia=str(input("horas dedicadas a los videojuegos por dia:"))
horas_dedicadas_a_los_videojuegos_por_semanaç=str(input("horas dedicadas a los videojuegos por semana:"))

# Processing
total=horas_dedicadas_a_los_videojuegos_por_dia*horas_dedicadas_a_los_videojuegos_por_semana
transtorno_mental=(total_de_horas_por_semana > 20 )
if(transtorno_mental):
    print("Transtorno mental")
#fin_if


#Ejercicio_22
paciente,horas_falta_de_sueño_por_dia,horas_falta_de_sueño_por_semana="",0,0
paciente=str(input("paciente:"))
horas_falta_de_sueño_por_dia=str(input("horas falta de sueño por dia:"))
horas_falta_de_sueño_por_semana=str(input("horas falta de sueño por semana:"))

# Processing
total=horas_falta_de_sueño_por_dia*horas_falta_de_sueño_por_semana
sufre_imsomnio=(total_de_horas_por_semana > 120 )
if(sufre_imsomnio):
    print("Sufre imsomnio")
#fin_if


#Ejercicio_23
cliente,producto_1,producto_2,costo_uni_1,costo_uni_2,cant_de_producto_1,cant_de_producto_2="","","",0.0,0.0,0,0
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
producto_2=str(input("producto 2:"))
costo_uni_1=float(input("costo unitario 1:"))
costo_uni_2=float(input("costo unitario 2:"))
cant_de_producto_1=str(input("cantidad de producto 1:"))
cant_de_producto_2=str(input("cantidad de producto 2:"))

# Processing
total=(costo_uni_1*cant_de_producto_1)+(costo_uni_2*cant_de_producto_2)
comprador_prudente=(total < 50)
if(comprador_prudente):
    print("Comprador prudente")
#fin_if


#Ejercicio_24
nombre_del_alumno,nota_1,nota_2,nota_3,nota_4="",0,0,0,0
nombre_del_alumno=str(input("nombre del alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))
nota_4=str(input("nota4:"))

# Processing
promedio=(nota_1+nota_2+nota_3+nota_4)/4
alumno_sobresaliente=(promedio > 18)
if(alumno_sobresaliente):
    print("Alumno sobresaliente")
#fin_if


#Ejercicio_25
nombre,numero_veces_al_dia_tomando_cafe,numero_veces_a_la_semana_tomando_cafe="",0,0
cliente=str(input("cliente:"))
numero_veces_al_dia_tomando_cafe=str(input("numero veces al dia tomando cafe:"))
numero_veces_a_la_semana_tomando_cafe=str(input("numero veces a la semana tomando cafe:"))

# Processing
total=numero_veces_al_dia_tomando_cafe*numero_veces_a_la_semana_tomando_cafe
adiccion_al_cafe=(numero_veces_a_la_semana_tomando_cafe > 7 )
if(adiccion_al_cafe):
    print("Adiccion al cafe")
#fin_if


#Ejercicio_26
nombre,numero_viajes_a_la_semana,numero_viajes_al_mes="",0,0
nombre=str(input("nombre:"))
numero_viajes_a_la_semana=str(input("numero viajes a la semana:"))
numero_viajes_al_mes=str(input("numero viajes al mes:"))

# Processing
total=numero_viajes_a_la_semana*numero_viajes_al_mes
gusto_por_viajar=(numero_viajes_al_mes > 20 )
if(gusto_por_viajar):
    print("Gusto por viajar")
#fin_if


#Ejercicio_27
cliente,numero_visitas_a_la_biblioteca_por_dia,numero_visitas_a_la_biblioteca_por_semana="",0,0
cliente=str(input("cliente:"))
numero_visitas_a_la_biblioteca_por_dia=str(input("numero visitas a la biblioteca por dia:"))
numero_visitas_a_la_biblioteca_por_semana=str(input("numero visitas a la biblioteca por semana:"))

# Processing
total=numero_visitas_a_la_biblioteca_por_dia*numero_visitas_a_la_biblioteca_por_semana
amante_de_la_lectura=(numero_visitas_a_la_biblioteca_por_semana > 14 )
if(amante_de_la_lectura):
    print("Amante de la lectura")
#fin_if


#Ejercicio_28
nombre,fruta_1,fruta_2,cant_de_fruta_1_por_dia,cant_de_fruta_2_por_dia="","","",0,0
nombre=str(input("nombre:"))
fruta_1=str(input("fruta 1:"))
fruta_2=str(input("fruta 2:"))
cant_de_fruta_1_por_dia=str(input("cantidad de fruta 1 por dia:"))
cant_de_fruta_2_por_dia=str(input("cantidad de fruta 2 por dia:"))

# Processing
total_de_fruta_por_semana=(cant_de_fruta_1_por_dia*7)+(cant_de_fruta_2_por_dia*7)
gusto_por_la_fruta=(total_de_fruta_por_semana > 36 )
if(gusto_por_la_fruta):
    print("Gusto por la fruta")
#fin_if


#Ejercicio_29
nombre,verdura1,verdura2,cant_de_verdura1_por_dia,cant_de_verdura2_por_dia="","","",0,0
nombre=str(input("nombre:"))
verdura1=str(input("verdura 1:"))
verdura2=str(input("verdura 2:"))
cant_de_verdura1_por_dia=str(input("cantidad de verdura 1 por dia:"))
cant_de_verdura2_por_dia=str(input("cantidad de verdura 2 por dia:"))

# Processing
total_de_verdura_por_semana=(cant_de_verdura1_por_dia*7)+(cant_de_verdura2_por_dia*7)
persona_vegetariana=(total_de_verdura_por_semana > 40 )
if(persona_vegetariana):
    print("Persona vegetariana")
#fin_if


#Ejercicio_30
nombre,pescados,mariscos,cant_de_pescado_por_dia,cant_de_marisco_por_dia="","","",0,0
nombre=str(input("nombre:"))
pescados=str(input("pescados:"))
mariscos=str(input("mariscos:"))
cant_de_pescado_por_dia=str(input("cantidad de pescado por dia:"))
cant_de_marisco_por_dia=str(input("cantidad de marisco por dia:"))

# Processing
total_de_mariscos_por_semana=(cant_de_pescado_por_dia*7)+(cant_de_marisco_por_dia*7)
pescetariano=(total_de_mariscos_por_semana > 30 )
if(pescetariano):
    print("Pescetariano")
#fin_if


#Ejercicio_31
usuario,red_social_1,red_social_2,cant_de_hora_diarias_1,cant_de_hora_diaria_2="","","",0,0
usuario=str(input("usuario:"))
red_social_1=str(input("red social 1:"))
red_social_2=str(input("red social 2: "))
cant_de_hora_diarias_1=int(input("cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("cantidad de horas diarias 2:"))

#Processing
total_de_horas_por_dia=(cant_de_hora_diarias_1+cant_de_hora_diarias_2)
uso_moderado_de_redes_sociales=(total_de_horas_por_dia < 8 )
if(uso_moderado_de_redes_sociales):
    print("Uso moderado de redes sociales")
#fin_if


#Ejercicio_32
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia="","","",0,0
paciente=str(input("paciente:"))
medicamento_1=str(input("medicamento 1:"))
medicamento_2=str(input("medicamento 2:"))
cant_de_medicamento1_por_dia=str(input("cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=str(input("cantidad de medicamento 2 por dia:"))

# Processing
total_de_medicamentos_por_semana=(cant_de_medicamento1_por_dia*7)+(cant_de_medicamento2_por_dia*7)
medicacion_moderada=(total_de_medicamentos_por_semana < 5 )
if(medicacion_moderada):
    print("Medicacion moderada")
#fin_if


#Ejercicio_33
nombre,deporte1,deporte2,cant_de_hora_diarias_1,cant_de_hora_diarias_2="","","",0,0
nombre=str(input("nombre:"))
deporte1=str(input("deporte 1:"))
deporte2=str(input("deporte 2:"))
cant_de_hora_diarias_1=str(input("cantidad de hora diarias 1:"))
cant_de_hora_diarias_2=str(input("cantidad de hora diarias 2:"))

# Processing
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2
disgusto_por_el_deporte=(total_de_horas_por_semana < 2 )
if(disgusto_por_el_deporte):
    print("Disgusto por el deporte")
#fin_if


#Ejercicio_34
trabajador,horas_de_jornada_laboral_por_dia,dias_de_jornada_laboral="",0,0
trabajador=str(input("trabajador:"))
horas_de_jornada_laboral_por_dia=str(input("horas de jornada laboral por dia:"))
dias_de_jornada_laboral=str(input("dias de jornada laboral:"))

# Processing
total=horas_de_jornada_laboral_por_dia*dias_de_jornada_laboral
incumplimiento_de_horas_de_trabajo=(total_de_horas_por_semana < 30 )
if(incumplimiento_de_horas_de_trabajo):
    print("Incumplimiento de horas de trabajo")
#fin_if


#Ejercicio_35
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_television_por_dia=str(input("horas dedicadas a la television por dia:"))
horas_dedicadas_a_la_television_por_semana=str(input("horas dedicadas a la television por semana:"))

# Processing
total=horas_dedicadas_a_la_television_por_dia*horas_dedicadas_a_la_television_por_semana
disgusto_a_la_television=(total_de_horas_por_semana < 5 )
if(disgusto_a_la_television):
    print("Disgusto a la television")
#fin_if


#Ejercicio_36
alumno,nota_1,nota_2,nota_3,nota_4="",0,0,0,0
alumno=str(input("alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))
nota_4=str(input("nota4:"))

# Processing
promedio=(nota_1+nota_2+nota_3+nota_4)/4
materia_aprobada=(promedio > 14)
if(materia_aprobada):
    print("Materia aprobada")
#fin_if


#Ejercicio_37
cliente,cajetilla_1,cantidad_de_cigarros_por_dia="",0,0
cliente=str(input("cliente:"))
cajetilla_1=str(input("cajetilla 1:"))
cantidad_de_cigarros_por_dia=str(input("cantidad de cigarros por dia:"))

# Processing
cantidad_de_cigarros_por_semana=(cantidad_de_cigarros_por_dia*cajetilla_1)
fumador_pasivo=(cantidad_de_cigarros_por_dia < 1 )
if(fumador_pasivo):
    print("Fumador pasivo")
#fin_if


#Ejercicio_38
alumno,nota_01,nota_02,nota_03="",0,0,0
alumno=str(input("alumno:"))
nota_01=str(input("nota 01:"))
nota_02=str(input("nota 02:"))
nota_03=str(input("nota 03:"))

# Processing
promedio=(nota_01+nota_02+nota_03)/3
nota_desaprobatoria_ingles=(promedio < 50 )
if(nota_desaprobatoria_ingles):
    print("Nota desaprobatoria ingles")
#fin_if


#Ejercicio_39
paciente,horas_en_hospital_por_dia,horas_en_hospital_por_semana="",0,0
paciente=str(input("pacinete:"))
horas_en_hospital_por_dia=str(input("horas en hospital por dia:"))
horas_en_hospital_por_semana=str(input("horas en hospital por semana:"))

# Processing
total=horas_en_hospital_por_dia*horas_en_hospital_por_semana
dada_de_alta_denegada=(total_de_horas_por_semana < 6 )
if(dada_de_alta_denegada):
    print("Dada de alta denegada")
#fin_if


#Ejercicio_40
paciente,horas_de_sueño_por_dia,horas_de_sueño_por_semana="",0,0
paciente=str(input("paciente:"))
horas_de_sueño_por_dia=str(input("horas de sueño por dia:"))
horas_de_sueño_por_semana=str(input("horas de sueño por semana:"))

# Processing
total=horas_de_sueño_por_dia*horas_de_sueño_por_semana
no_sufre_imsomnio=(total_de_horas_por_semana > 56 )
if(no_sufre_imsomnio):
    print("No sufre imsomnio")
#fin_if


#Ejercicio_41
nombre,numero_veces_al_dia_tomando_cafe,numero_veces_a_la_semana_tomando_cafe="",0,0
cliente=str(input("cliente:"))
numero_veces_al_dia_tomando_cafe=str(input("numero veces al dia tomando cafe:"))
numero_veces_a_la_semana_tomando_cafe=str(input("numero veces a la semana tomando cafe:"))

# Processing
total=numero_veces_al_dia_tomando_cafe*numero_veces_a_la_semana_tomando_cafe
gusto_moderado_por_el_cafe=(numero_veces_a_la_semana_tomando_cafe < 4 )
if(gusto_moderado_por_el_cafe):
    print("Gusto moderado por el cafe")
#fin_if


#Ejercicio_42
nombre,numero_viajes_a_la_semana,numero_viajes_al_mes="",0,0
nombre=str(input("nombre:"))
numero_viajes_a_la_semana=str(input("numero viajes a la semana:"))
numero_viajes_al_mes=str(input("numero viajes al mes:"))

# Processing
total=numero_viajes_a_la_semana*numero_viajes_al_mes
hodofobia=(numero_viajes_al_mes < 2 )
if(hodofobia):
    print("Hodofobia")
#fin_if


#Ejercicio_43
cliente,numero_visitas_a_la_biblioteca_por_dia,numero_visitas_a_la_biblioteca_por_semana="",0,0
cliente=str(input("cliente:"))
numero_visitas_a_la_biblioteca_por_dia=str(input("numero visitas a la biblioteca por dia:"))
numero_visitas_a_la_biblioteca_por_semana=str(input("numero visitas a la biblioteca por semana:"))

# Processing
total=numero_visitas_a_la_biblioteca_por_dia*numero_visitas_a_la_biblioteca_por_semana
disgusto_por_la_lectura=(numero_visitas_a_la_biblioteca_por_semana < 3 )
if(disgusto_por_la_lectura):
    print("Disgusto por la lectura")
#fin_if


#Ejercicio_44
nombre,fruta_1,fruta_2,cant_de_fruta_1_por_dia,cant_de_fruta_2_por_dia="","","",0,0
nombre=str(input("nombre:"))
fruta_1=str(input("fruta 1:"))
fruta_2=str(input("fruta 2:"))
cant_de_fruta_1_por_dia=str(input("cantidad de fruta 1 por dia:"))
cant_de_fruta_2_por_dia=str(input("cantidad de fruta 2 por dia:"))

# Processing
total_de_fruta_por_semana=(cant_de_fruta_1_por_dia*7)+(cant_de_fruta_2_por_dia*7)
no_come_saludable=(total_de_fruta_por_semana < 4 )
if(no_come_saludable):
    print("No come saludable")
#fin_if


#Ejercicio_45
nombre,verdura1,verdura2,cant_de_verdura1_por_dia,cant_de_verdura2_por_dia="","","",0,0
nombre=str(input("nombre:"))
verdura1=str(input("verdura 1:"))
verdura2=str(input("verdura 2:"))
cant_de_verdura1_por_dia=str(input("cantidad de verdura 1 por dia:"))
cant_de_verdura2_por_dia=str(input("cantidad de verdura 2 por dia:"))

# Processing
total_de_verdura_por_semana=(cant_de_verdura1_por_dia*7)+(cant_de_verdura2_por_dia*7)
no_es_vegetariana=(total_de_verdura_por_semana < 6 )
if(no_es_vegetariana):
    print("No es  vegetariana")
#fin_if


#Ejercicio_46
nombre,horas_dedicadas_a_la_cocina_por_dia,horas_dedicadas_a_la_cocina_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_cocina_por_dia=str(input("horas dedicadas a la cocina por dia:"))
horas_dedicadas_a_la_cocina_por_semana=str(input("horas dedicadas a la cocina por semana:"))

# Processing
total=horas_dedicadas_a_la_cocina_por_dia*horas_dedicadas_a_la_cocina_por_semana
disgusto_a_la_gastronomia=(total_de_horas_por_semana < 20 )
if(disgusto_a_la_gastronomia):
    print("Disgusto a la gastronomia")
#fin_if


#Ejercicio_47
nombre,horas_dedicadas_a_la_cocina_por_dia,horas_dedicadas_a_la_cocina_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_cocina_por_dia=str(input("horas dedicadas a la cocina por dia:"))
horas_dedicadas_a_la_cocina_por_semana=str(input("horas dedicadas a la cocina por semana:"))

# Processing
total=horas_dedicadas_a_la_cocina_por_dia*horas_dedicadas_a_la_cocina_por_semana
aficion_a_la_gastronomia=(total_de_horas_por_semana > 50 )
if(aficion_a_la_gastronomia):
    print("Aficion a la gastronomia")
#fin_if


#Ejercicio_48
alumno,nota_01,nota_02,nota_03="",0,0,0
alumno=str(input("alumno:"))
nota_01=str(input("nota 01:"))
nota_02=str(input("nota 02:"))
nota_03=str(input("nota 03:"))

# Processing
promedio=(nota_01+nota_02+nota_03)/3
nota_aprobatoria_algebra=(promedio > 15 )
if(nota_aprobatoria_algebra):
    print("Nota aprobatoria algebra")
#fin_if


#Ejercicio_49
candidato,numero_votos_costa,numero_votos_sierra,numero_votos_selva="",0,0,0
candidato=str(input("candidato:"))
numero_votos_costa=str(input("numero votos costa:"))
numero_votos_sierra=str(input("numero votos sierra:"))
numero_votos_selva=str(input("numero votos selva:"))

# Processing
total=numero_votos_costa+numero_votos_sierra+numero_votos_selva
presidente_de_ecuador=(total > 54000)
if(presidente_de_ecuador):
    print("Presidente de ecuador")
#fin_if


#Ejercicio_50
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2="","","",0,0,0.0,0.0
cliente=str(input("cliente:"))
producto1=str(input("producto 1:"))
producto2=str(input("producto 2:"))
cant_de_producto1=str(input("cantidad de producto 1"))
cant_de_producto2=str(input("cantidad de producto 2:"))
cost_uni1=str(input("cosot unitario 1:"))
cost_uni2=str(input("costo unitario 2:"))

# Processing
total=(cant_de_producto1*cost_uni1)+(cant_de_producto2*cost_uni2)
obsecion_por_el_maquillaje=(total > 200 )
if(obsecion_por_el_maquillaje):
    print("Obsecion por el maquillaje")
#fin_if

