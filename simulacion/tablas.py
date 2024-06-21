import random as r
class nueva_obra():
    #obras en espera al iniciar
    def obras_al_iniciar(self):
        a=r.random()
        if a>0 and a<=0.55:
            semanas=0
            return semanas
        elif a>0.55 and a<=0.85:
            semanas=1
            return semanas
        elif a>0.85 and a<=0.95:
            semanas=2
            return semanas
        elif a>0.95 and a<=1:
            semanas=3
            return semanas
    #temporada alta
    def tiempo_de_espera_alta(self):
        a = r.random()
        if a > 0 and a <= 0.05:
            semanas = 1
            return semanas
        elif a > 0.05 and a <= 0.2:
            semanas = 2
            return semanas
        elif a > 0.2 and a <= 0.65:
            semanas = 3
            return semanas
        elif a > 0.65 and a <= 0.83:
            semanas = 4
            return semanas
        elif a > 0.83 and a <= 0.93:
            semanas = 5
            return semanas
        elif a > 0.93 and a <= 1:
            semanas = 6
            return semanas
    #temporada baja
    def tiempo_de_espera_baja(self):
        a = r.random()
        if a > 0 and a <= 0.2:
            semanas = 4
            return semanas
        elif a > 0.2 and a <= 0.5:
            semanas = 5
            return semanas
        elif a > 0.5 and a <= 0.85:
            semanas = 6
            return semanas
        elif a > 0.85 and a <= 1:
            semanas = 7
            return semanas
    #magnitud de la obra
    def magnitud_de_obra(self):
        a = r.random()
        if a > 0 and a <= 0.35:
            m2 = 100
            return m2
        elif a > 0.35 and a <= 0.6:
            m2 = 200
            return m2
        elif a > 0.6 and a <= 0.7:
            m2 = 300
            return m2
        elif a > 0.7 and a <= 0.9:
            m2 = 400
            return m2
        elif a > 0.9 and a <= 1:
            m2 = 500
            return m2
    #si m2=100
    def duracion_100(self):
        a = r.random()
        if a > 0 and a <= 0.1:
            semanas = 10
            return semanas
        elif a > 0.1 and a <= 0.75:
            semanas = 12
            return semanas
        elif a > 0.75 and a <= 0.95:
            semanas = 16
            return semanas
        elif a > 0.95 and a <= 1:
            semanas = 20
            return semanas

    def personal_necesario_100(self):
        a = r.random()
        if a > 0 and a <= 0.8:
            cuadrillas = 1
            return cuadrillas
        elif a > 0.8 and a <= 0.95:
            cuadrillas = 2
            return cuadrillas
        elif a > 0.95 and a <= 0.99:
            cuadrillas = 3
            return cuadrillas
        elif a > 0.99 and a <= 1:
            cuadrillas = 4
            return cuadrillas
    # si m2=200
    def duracion_200(self):
        a = r.random()
        if a > 0 and a <= 0.15:
            semanas = 18
            return semanas
        elif a > 0.15 and a <= 0.6:
            semanas = 20
            return semanas
        elif a > 0.6 and a <= 0.9:
            semanas = 24
            return semanas
        elif a > 0.9 and a <= 1:
            semanas = 28
            return semanas

    def personal_necesario_200(self):
        a = r.random()
        if a > 0 and a <= 0.8:
            cuadrillas = 1
            return cuadrillas
        elif a > 0.8 and a <= 0.95:
            cuadrillas = 2
            return cuadrillas
        elif a > 0.95 and a <= 0.99:
            cuadrillas = 3
            return cuadrillas
        elif a > 0.99 and a <= 1:
            cuadrillas = 4
            return cuadrillas
    #si m2=300
    def duracion_300(self):
        a = r.random()
        if a > 0 and a <= 0.1:
            semanas = 24
            return semanas
        elif a > 0.1 and a <= 0.75:
            semanas = 26
            return semanas
        elif a > 0.75 and a <= 0.91:
            semanas = 30
            return semanas
        elif a > 0.91 and a <= 1:
            semanas = 36
            return semanas

    def personal_necesario_300(self):
        a = r.random()
        if a > 0 and a <= 0.7:
            cuadrillas = 1
            return cuadrillas
        elif a > 0.7 and a <= 0.95:
            cuadrillas = 2
            return cuadrillas
        elif a > 0.95 and a <= 0.99:
            cuadrillas = 3
            return cuadrillas
        elif a > 0.99 and a <= 1:
            cuadrillas = 4
            return cuadrillas
    # si m2=400
    def duracion_400(self):
        a = r.random()
        if a > 0 and a <= 0.1:
            semanas = 10
            return semanas
        elif a > 0.1 and a <= 0.75:
            semanas = 12
            return semanas
        elif a > 0.75 and a <= 0.91:
            semanas = 16
            return semanas
        elif a > 0.91 and a <= 1:
            semanas = 25
            return semanas

    def personal_necesario_400(self):
        a = r.random()
        if a > 0 and a <= 0.55:
            cuadrillas = 1
            return cuadrillas
        elif a > 0.55 and a <= 0.9:
            cuadrillas = 2
            return cuadrillas
        elif a > 0.9 and a <= 0.94:
            cuadrillas = 3
            return cuadrillas
        elif a > 0.94 and a <= 1:
            cuadrillas = 4
            return cuadrillas
    # si m2=500
    def duracion_500(self):
        a = r.random()
        if a > 0 and a <= 0.1:
            semanas = 10
            return semanas
        elif a > 0.1 and a <= 0.75:
            semanas = 12
            return semanas
        elif a > 0.75 and a <= 0.91:
            semanas = 16
            return semanas
        elif a > 0.91 and a <= 1:
            semanas = 25
            return semanas

    def personal_necesario_500(self):
        a = r.random()
        if a > 0 and a <= 0.6:
            cuadrillas = 3
            return cuadrillas
        elif a > 0.6 and a <= 0.85:
            cuadrillas = 4
            return cuadrillas
        elif a > 0.85 and a <= 0.99:
            cuadrillas = 5
            return cuadrillas
        elif a > 0.99 and a <= 1:
            cuadrillas = 6
            return cuadrillas
    #cada mes
    def licitacion_obra(self):
        a = r.random()
        if a > 0 and a <= 0.15:
            semanas = 1 #si
            return semanas
        elif a > 0.15 and a <= 1:
            semanas = 0 #no
            return semanas
    def magnitud_obra_gobierno(self):
        a = r.random()
        if a > 0 and a <= 0.15:
            trabajo = 1  # carretera
            return trabajo
        elif a > 0.15 and a <= 0.25:
            trabajo = 1  # edificio
            return trabajo
        elif a > 0.25 and a <= 0.75:
            trabajo = 1  # servicio
            return trabajo
        elif a > 0.75 and a <= 1:
            trabajo = 1  # proyecto
            return trabajo

    def magnitud_obra_gobierno_tiempo(self):
        a = r.random()
        if a > 0 and a <= 0.15:
            meses = 3
            return meses
        elif a > 0.15 and a <= 0.25:
            meses = 6
            return meses
        elif a > 0.25 and a <= 0.75:
            meses = 12
            return meses
        elif a > 0.75 and a <= 1:
            meses = 36
            return meses
    def personal_necesario(self):
        a = r.random()
        if a > 0 and a <= 0.2:
            cuadrillas = 5
            return cuadrillas
        elif a > 0.2 and a <= 0.55:
            cuadrillas = 6
            return cuadrillas
        elif a > 0.55 and a <= 0.95:
            cuadrillas = 7
            return cuadrillas
        elif a > 0.95 and a <= 1:
            cuadrillas = 8
            return cuadrillas
    def precio_licitacion(self):
        a = r.random()
        if a > 0 and a <= 0.1:
            precio = 15000
            return precio
        elif a > 0.1 and a <= 0.75:
            precio = 24000
            return precio
        elif a > 0.75 and a <= 0.91:
            precio = 30000
            return precio
        elif a > 0.91 and a <= 1:
            precio = 40000
            return precio
class trabajos():
    def tiempo_espera_ts(self):
        a = r.random()
        if a > 0 and a <= 0.2:
            dias = 7
            return dias
        elif a > 0.2 and a <= 0.9:
            dias = 15
            return dias
        elif a > 0.9 and a <= 1:
            dias = 20
            return dias
    def actividad_ts(self):
        a = r.random()
        if a > 0 and a <= 0.25:
            actividad = 0 #nada
            return actividad
        elif a > 0.25 and a <= 0.5:
            actividad = 1  # capacitacion
            return actividad
        elif a > 0.5 and a <= 0.75:
            actividad = 2  # remodelacion
            return actividad
        elif a > 0.75 and a <= 1:
            actividad = 3  # presupuesto
            return actividad
    def remodelacion(self):
        a = r.random()
        if a > 0 and a <= 0.45:
            duracion = 3  # dias
            return duracion
        elif a > 0.45 and a <= 0.95:
            duracion = 7  # dias
            return duracion
        elif a > 0.95 and a <= 1:
            duracion = 14  # dias
            return duracion
    def actividades_capacitacion(self):
        a = r.random()
        if a > 0 and a <= 0.2:
            semana = 1
            return semana
        elif a > 0.2 and a <= 0.3:
            semana = 3
            return semana
        elif a > 0.3 and a <= 1:
            semana = 4
            return semana
    def trabajos_simples(self):
        a = r.random()
        if a > 0 and a <= 0.3:
            dias = 3
            return dias
        elif a > 0.3 and a <= 0.5:
            dias = 5
            return dias
        elif a > 0.5 and a <= 1:
            dias = 7
            return dias
    def presupuesto(self):
        a = r.random()
        if a > 0 and a <= 0.3:
            dias = 2
            presupuesto=500
            return dias,presupuesto
        elif a > 0.3 and a <= 0.5:
            dias = 4
            presupuesto = 800
            return dias, presupuesto
        elif a > 0.5 and a <= 1:
            dias = 6
            presupuesto = 1000
            return dias, presupuesto
    def capacidad_cuadrillas(self):
        a = r.random()
        if a > 0 and a <= 0.2:
            cuadrillas = 2
            return cuadrillas
        elif a > 0.2 and a <= 0.3:
            cuadrillas = 3
            return cuadrillas
        elif a > 0.3 and a <= 1:
            cuadrillas = 4
            return cuadrillas
    def m2_presupuesto(self):
        a = r.random()
        if a > 0 and a <= 0.35:
            m2 = 100
            return m2
        elif a > 0.35 and a <= 0.6:
            m2 = 200
            return m2
        elif a > 0.6 and a <= 0.7:
            m2 = 300
            return m2
        elif a > 0.7 and a <= 0.9:
            m2 = 400
            return m2
        elif a > 0.9 and a <= 1:
            m2 = 500
            return m2
    def m2_remodelacion(self):
        a = r.random()
        if a > 0 and a <= 0.4:
            tamano= 10
            return tamano
        elif a > 0.4 and a <= 0.8:
            tamano = 25
            return tamano
        elif a > 0.8 and a <= 0.9:
            tamano = 35
            return tamano
        elif a > 0.9 and a <= 1:
            tamano = 50
            return tamano
class temporadas():
    def especulaciones(self):
        a = r.random()
        if a > 0 and a <= 0.4:
            tamano = 1 #si
            return tamano
        elif a > 0.4 and a <= 1:
            tamano = 0 #no
            return tamano
    def cancelacion_temporal_cliente(self):
        a = r.random()
        if a > 0 and a <= 0.08:
            semanas = 2
            return semanas
        elif a > 0.08 and a <= 0.1:
            semanas = 5
            return semanas
        elif a > 0.1 and a <= 1:
            semanas = 0
            return semanas
    def porcentaje_aumento(self):
        a = r.random()
        if a > 0 and a <= 0.2:
            porcentaje = 3
            return porcentaje
        elif a > 0.2 and a <= 0.5:
            porcentaje = 4
            return porcentaje
        elif a > 0.5 and a <= 0.8:
            porcentaje = 3
            return porcentaje
        elif a > 0.8 and a <= 1:
            porcentaje = 1
            return porcentaje
class problemas():
    def recision_contrato(self):
        a = r.random()
        if a > 0 and a <= 0.95:
            decision = 0 #no
            return decision
        elif a > 0.95 and a <= 1:
            decision = 1 #si
            return decision

    def actividades_atipicas(self):
        a = r.random()
        if a > 0 and a <= 0.15:
            decision = 1  # si
            return decision
        elif a > 0.15 and a <= 1:
            decision = 0  # no
            return decision
    def accidentes(self):
        a = r.random()
        if a > 0 and a <= 0.8:
            decision = 1  # si
            return decision
        elif a > 0.8 and a <= 1:
            decision = 0  # no
            return decision
    def clausuras(self):
        a = r.random()
        if a > 0 and a <= 0.8:
            decision = 0  # no
            return decision
        elif a > 0.8 and a <= 1:
            decision = 1  # si
            return decision
    def tramite_permisos(self):
        a = r.random()
        if a > 0 and a <= 0.3:
            dias = 1
            return dias
        elif a > 0.3 and a <= 0.5:
            dias = 3
            return dias
        elif a > 0.5 and a <= 1:
            dias = 7
            return dias
    def actividades_atipicas_2(self):
        a = r.random()
        if a > 0 and a <= 0.3:
            semanas = 4
            tamano=15
            return tamano,semanas
        elif a > 0.3 and a <= 0.5:
            semanas = 6
            tamano = 10
            return tamano, semanas
        elif a > 0.5 and a <= 1:
            semanas = 8
            tamano = 5
            return tamano, semanas
    def accidentes_2(self):
        a = r.random()
        if a > 0 and a <= 0.3:
            tiempo = 2
            accidente = 0
            return accidente, tiempo
        elif a > 0.3 and a <= 0.5:
            tiempo = 1
            accidente = 1
            return accidente, tiempo
        elif a > 0.5 and a <= 1:
            tiempo = 2
            accidente = 2
            return accidente, tiempo
    def clausuras_tiempo(self):
        a = r.random()
        if a > 0 and a <= 0.4:
            tiempo = 4
            return tiempo
        elif a > 0.4 and a <= 0.5:
            tiempo = 8
            return tiempo
        elif a > 0.5 and a <= 1:
            tiempo = 12
            return tiempo
class rendimientos():
    def enfermedad(self):
        a = r.random()
        if a > 0 and a <= 0.1:
            decision = 1  # si
            return decision
        elif a > 0.1 and a <= 1:
            decision = 0  # no
            return decision
    def enfermedad_1(self):
        a = r.random()
        if a > 0 and a <= 0.05:
            decision = 1  # si
            return decision
        elif a > 0.05 and a <= 1:
            decision = 0  # no
            return decision
    def necesidad_laboratorio(self):
        a = r.random()
        if a > 0 and a <= 0.4:
            decision = 1  # si
            return decision
        elif a > 0.4 and a <= 1:
            decision = 0  # no
            return decision
    def cuadrilla_eficiente(self):
        a = r.random()
        if a > 0 and a <= 0.75:
            aumento = 0
            return aumento
        elif a > 0.75 and a <= 0.9:
            aumento = 5
            return aumento
        elif a > 0.9 and a <= 0.95:
            aumento = 1
            return aumento
        elif a > 0.95 and a <= 1:
            aumento = 10
            return aumento
    def ocasiones_laboratorio(self):
        a = r.random()
        if a > 0 and a <= 0.5:
            aumento = 0
            return aumento
        elif a > 0.5 and a <= 0.8:
            aumento = 1
            return aumento
        elif a > 0.8 and a <= 0.95:
            aumento = 2
            return aumento
        elif a > 0.95 and a <= 1:
            aumento = 3
            return aumento
class personal():
    def personal(self):
        a = r.random()
        if a > 0 and a <= 0.5:
            aumento = 0 #no se necesita
            return aumento
        elif a > 0.5 and a <= 0.8:
            aumento = 1 #foranea
            return aumento
        elif a > 0.8 and a <= 0.95:
            aumento = 2 #certificado
            return aumento
        elif a > 0.95 and a <= 1:
            aumento = 3 #especialista
            return aumento
    def contratacion_maquinaria(self):
        a = r.random()
        if a > 0 and a <= 0.35:
            cuadrilla = 5 #no se necesita
            reduccion=0
            return cuadrilla,reduccion
        elif a > 0.35 and a <= 0.6:
            cuadrilla= 10 #foranea
            reduccion = 2
            return cuadrilla, reduccion
        elif a > 0.6 and a <= 0.9:
            cuadrilla = 15 #certificado
            reduccion = 3
            return cuadrilla, reduccion
        elif a > 0.9 and a <= 1:
            cuadrilla = 17 #especialista
            reduccion = 4
            return cuadrilla, reduccion
    def tiempo_cuadrilla_foranea(self):
        a = r.random()
        if a > 0 and a <= 0.75:
            ocasiones= 1
            return ocasiones
        elif a > 0.75 and a <= 0.9:
            ocasiones = 2
            return ocasiones
        elif a > 0.9 and a <= 1:
            ocasiones = 3
            return ocasiones
    def tiempo_certificada(self):
        a = r.random()
        if a > 0 and a <= 0.75:
            ocasiones= 1
            return ocasiones
        elif a > 0.75 and a <= 0.9:
            ocasiones = 2
            return ocasiones
        elif a > 0.9 and a <= 1:
            ocasiones = 3
            return ocasiones
    def tiempo_especialista(self):
        a = r.random()
        if a > 0 and a <= 0.75:
            ocasiones= 1
            return ocasiones
        elif a > 0.75 and a <= 0.9:
            ocasiones = 2
            return ocasiones
        elif a > 0.9 and a <= 1:
            ocasiones = 3
            return ocasiones
    def concentracion_cuadrillas(self):
        a = r.random()
        if a > 0 and a <= 0.2:
            tamano= 5
            return tamano
        elif a > 0.2 and a <= 0.7:
            tamano = 10
            return tamano
        elif a > 0.7 and a <= 1:
            tamano = 15
            return tamano
    def concentraccion_personal_calificado(self):
        a = r.random()
        if a > 0 and a <= 0.3:
            tamano = 5
            return tamano
        elif a > 0.3 and a <= 0.7:
            tamano = 10
            return tamano
        elif a > 0.7 and a <= 1:
            tamano = 15
            return tamano
    def personal_calificado(self):
        a = r.random()
        if a > 0 and a <= 0.25:
            tipo = 0 #minoritario
            return tipo
        elif a > 0.25 and a <= 0.65:
            tipo = 1 #parcial
            return tipo
        elif a > 0.65 and a <= 1:
            tipo = 2 #total
            return tipo
    def maquinaria_requerida(self):
        a = r.random()
        if a > 0 and a <= 0.6:
            decision = 1  # si
            return decision
        elif a > 0.6 and a <= 1:
            decision = 0  # no
            return decision
    def contratacion_especialista(self):
        a = r.random()
        if a > 0 and a <= 0.55:
            decision = 1  # si
            return decision
        elif a > 0.55 and a <= 1:
            decision = 0  # no
            return decision
    def personal_analista(self):
        a = r.random()
        if a > 0 and a <= 0.6:
            decision = 1  # si
            return decision
        elif a > 0.6 and a <= 1:
            decision = 0  # no
            return decision
    def tiempo_extra_costo(self):
        a = r.random()
        if a > 0 and a <= 0.15:
            costo = 100
            tiempo = 2
            return costo, tiempo
        elif a > 0.15 and a <= 0.4:
            costo = 200
            tiempo = 3
            return costo, tiempo
        elif a > 0.4 and a <= 0.9:
            costo = 400
            tiempo = 5
            return costo, tiempo
        elif a > 0.9 and a <= 1:
            costo = 500
            tiempo = 6
            return costo, tiempo
