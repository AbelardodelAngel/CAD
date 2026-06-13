import pandas as pd
import numpy as np

def construir_dataset_ip():
    """
    Genera el dataset sintético de narrativas policiales para la 
    especialización del modelo en el léxico del C5.
    """
    
    narrativas_sinteticas = [
        # --- ROBO O HURTO (Etiqueta 0) ---
        "El afectado señala que un masculino le arrebató su teléfono celular mientras caminaba por la banqueta.",
        "Se reporta robo a casa habitación; los dueños regresaron y notaron faltante de electrodomésticos y joyería.",
        "Sujeto es asegurado saliendo de una tienda de conveniencia con mercancía oculta entre sus ropas sin pagar.",
        "Unidad policial atiende reporte de robo de vehículo estacionado afuera del centro comercial.",
        "El operador del C5 reporta que un individuo despojó de su bolso a una mujer amenazándola verbalmente.",
        "Se recibe llamada de emergencia indicando que dos sujetos sustrajeron herramientas de una obra en construcción.",
        "El ciudadano reporta que al dejar su bicicleta encadenada en el poste, un sujeto cortó el candado y huyó con ella.",
        "Reportan que en el transporte público un masculino sacó una cartera de la mochila de un pasajero sin que se diera cuenta.",
        "Se recibe alerta de robo en proceso dentro de una joyería; los sospechosos rompieron vitrinas para llevarse los relojes.",
        "El encargado de una bodega reporta el faltante de tres cajas de mercancía tras revisar las cámaras de seguridad.",
        "Detención en flagrancia de un sujeto que sustraía cableado eléctrico de los registros públicos de la avenida.",
        "Una mujer reporta que mientras esperaba el camión, un motociclista pasó corriendo y le quitó sus pertenencias.",
        "Se reporta el robo de una motocicleta que se encontraba estacionada sobre la acera peatonal.",
        "El dueño de una veterinaria indica que un cliente aprovechó un descuido para llevarse productos de mostrador.",
        "Elementos operativos aseguran a un masculino que llevaba una batería de coche de la cual no pudo acreditar propiedad.",
        "Reportan robo con violencia en gasolinera; sujetos armados despojaron del efectivo de las ventas al despachador.",
        "Se recibe reporte de robo de ganado en un rancho local; faltan cinco cabezas de bovino del corral principal.",
        "El afectado manifiesta que le sustrajeron la computadora portátil del interior de su oficina mientras fue a comer.",
        "Se atiende llamada de auxilio por robo de mercancía a un camión repartidor mientras se encontraba estacionado.",
        "Un individuo fue sorprendido intentando abrir la cajuela de un vehículo con una herramienta hechiza.",
        "La víctima refiere que ingresaron a su domicilio forzando la puerta trasera y se llevaron dinero en efectivo.",
        "Reportan hurto de medidores de agua en varias casas de la colonia durante el transcurso de la madrugada.",
        "Se asegura a una femenina que intentaba salir de un supermercado con prendas de ropa escondidas en su bolsa.",
        "El afectado indica que un sujeto le pidió prestado el teléfono para una emergencia y huyó corriendo con el equipo.",
        "Reporte de robo de autopartes; al ciudadano le faltaban los dos espejos laterales de su camioneta al salir de su casa.",
        "Sujeto armado despojó a un repartidor de comida de su motocicleta de trabajo y del dinero recolectado.",
        "Se recibe queja de locatario del mercado señalando que un cliente constante le robó mercancía de la bodega.",
        "La patrulla realiza la detención de un hombre que llevaba consigo una pantalla de televisión robada de una escuela.",
        "Reportan el robo de una bomba de agua del patio frontal de una vivienda deshabitada.",
        "Sujetos a bordo de un auto blanco interceptaron a un transeúnte y le quitaron su cartera y reloj.",
        "Se atiende reporte de farderas dentro de una tienda de ropa; escondían mercancía en bolsas forradas con aluminio.",
        "El encargado de un restaurante reporta que una mesa se retiró del lugar sin pagar la cuenta del consumo.",
        "Un ciudadano denuncia que un limpiaparabrisas le sacó el teléfono de la consola central de su auto en el semáforo.",
        "Reporte de robo a plantel educativo; faltan proyectores y computadoras del área de cómputo.",

        # --- LESIONES POR AGRESIÓN (Etiqueta 1) ---
        "Se recibió reporte de una riña en la vía pública donde un individuo agredió físicamente a otro provocándole heridas.",
        "Reportan violencia familiar en proceso; masculino golpea fuertemente a su cónyuge dentro del domicilio.",
        "Se solicita ambulancia para atender a un joven que presenta contusiones severas en el rostro tras una pelea callejera.",
        "Unidad médica traslada a un herido con arma blanca en el abdomen tras oponerse a un asalto.",
        "Se reporta riña campal afuera de un bar; hay varios lesionados por golpes con botellas de vidrio.",
        "Una mujer solicita auxilio debido a que su vecino la atacó físicamente tras discutir por un cajón de estacionamiento.",
        "El oficial reporta el hallazgo de un masculino ensangrentado tirado en la banqueta con huellas de violencia.",
        "Se atiende llamada por agresión física en un partido de fútbol; un jugador golpeó al árbitro causándole fractura.",
        "Reportan riña entre estudiantes a las afueras de la secundaria; uno de ellos requiere traslado por golpes en la cabeza.",
        "Un ciudadano resultó con quemaduras y lesiones tras ser agredido con líquido caliente durante una discusión familiar.",
        "Se asegura a un masculino que arrojó piedras a peatones logrando herir a una señora en el brazo.",
        "Reportan que un sujeto bajo los efectos del alcohol atacó a golpes a un repartidor sin motivo aparente.",
        "Se atiende a un masculino con heridas cortantes en las manos tras sostener una pelea con vidrios rotos.",
        "Una persona reporta que su hermano fue golpeado por varios sujetos al salir de una tienda de abarrotes.",
        "Se solicita apoyo policial por una riña entre operadores de transporte público; uno presenta herida en la ceja.",
        "El afectado manifiesta haber sido agredido con un bate de béisbol por un conocido tras un altercado verbal.",
        "Reporte de violencia escolar; un menor fue empujado por las escaleras resultando con fractura de extremidad.",
        "Unidad policial detiene a sujeto que propinó patadas y puñetazos a un guardia de seguridad privada.",
        "Se estabiliza a una femenina que presenta heridas punzocortantes leves tras un altercado con una vecina.",
        "Reportan herido por proyectil de arma de fuego en la pierna tras una discusión de tránsito en la avenida.",
        "Se atiende llamada de auxilio de un hombre que fue golpeado por su hijo dentro de su propiedad.",
        "Un comerciante fue agredido físicamente por un cliente inconforme, causándole lesiones en el tabique nasal.",
        "Reportan riña en el interior de un centro nocturno; paramédicos atienden a un masculino inconsciente por golpes.",
        "Se solicita la presencia policial debido a que un grupo de sujetos agrede a pedradas a los miembros de una familia.",
        "El lesionado refiere que fue interceptado por un conocido quien comenzó a golpearlo en repetidas ocasiones.",
        "Se atiende reporte de mujer lesionada tras ser empujada deliberadamente contra el suelo durante una discusión.",
        "Un masculino resulta con contusiones múltiples tras ser atacado por la espalda al salir de su lugar de trabajo.",
        "Reporte de agresión física mutua entre dos automovilistas que colisionaron sus unidades en el crucero.",
        "Se traslada a urgencias a un hombre que fue herido con una varilla durante una disputa por terrenos.",
        "Vecinos reportan que un sujeto golpea a un adulto mayor en el patio frontal de su vivienda.",
        "Se asegura a un individuo que atacó a su compañero de cuarto con un objeto contundente provocándole heridas.",
        "Reportan riña con heridos en una fiesta patronal; se despliegan unidades de emergencia para control de la situación.",
        "La víctima presenta hematomas visibles en los brazos tras haber sido sujetada con fuerza y golpeada.",

        # --- DAÑO EN PROPIEDAD AJENA (Etiqueta 2) ---
        "El ciudadano reporta que al llegar a su negocio local notó que las cerraduras estaban forzadas y la puerta rota.",
        "Sujeto desconocido arrojó una piedra contra el parabrisas de un automóvil estacionado, destrozando el cristal.",
        "Se reporta que un grupo de jóvenes se encuentra realizando pintas de grafiti en la fachada de una escuela pública.",
        "Un conductor perdió el control de su unidad e impactó la barda perimetral de un domicilio particular causándole daños.",
        "El propietario de un restaurante denuncia que un cliente ebrio rompió mesas y sillas antes de salir del lugar.",
        "Reportan que un individuo pateó intencionalmente el retrovisor de una camioneta provocando que se desprendiera.",
        "Se solicita el apoyo policial debido a que un vecino cortó deliberadamente la tubería de gas del quejoso.",
        "Unidad de patrulla asegura a un masculino que quebraba las luminarias públicas del parque con una resortera.",
        "Se reporta el incendio intencional de un contenedor de basura que afectó la pintura del negocio aledaño.",
        "Una mujer denuncia que su expareja acudió a su casa y destrozó las macetas y las ventanas de la fachada.",
        "El encargado de una plaza comercial reporta que vandalizaron el cajero automático doblando la bandeja de efectivo.",
        "Se reporta que un camión de carga pesada derribó el cableado y la mufa eléctrica de tres casas al pasar sin precaución.",
        "Un locatario señala que sujetos desconocidos arrojaron pintura negra sobre las cortinas de acero de su establecimiento.",
        "Se atiende llamada por daños a un vehículo; le poncharon las cuatro llantas con un objeto punzocortante.",
        "El reporte indica que un masculino pateó la puerta de acceso de un edificio de departamentos hasta romper el marco.",
        "Vecinos denuncian a un sujeto que derribó un árbol público provocando daños en las líneas telefónicas de la cuadra.",
        "Un ciudadano reporta que le rompieron el tragaluz de su vivienda al arrojar piedras desde el techo vecino.",
        "Se atiende reporte de vandalismo en un paradero de autobús; rompieron los paneles de vidrio templado de la estructura.",
        "El dueño de un taller mecánico refiere que un cliente inconforme rayó con una llave la pintura de tres autos terminados.",
        "Reportan que un individuo quebró el medidor de luz de una casa tras sostener una discusión con el residente.",
        "Se asegura a sujeto que causaba destrozos en el interior de una oficina de gobierno rompiendo monitores.",
        "Una llamada al C5 alerta sobre una persona dañando los neumáticos de los autos estacionados en la calle.",
        "El quejoso denuncia que los repartidores golpearon su portón de herrería al grado de doblar la estructura principal.",
        "Reporte de daños por grafiti en los monumentos históricos de la plaza principal; presuntos responsables huyen a pie.",
        "Se solicita unidad debido a que un conductor colisionó contra un poste de luz del municipio y pretende darse a la fuga.",
        "El propietario de un lote baldío reporta que destruyeron la malla ciclónica que delimitaba su propiedad.",
        "Sujeto arrojó una botella de vidrio contra el escaparate de una tienda de ropa provocando que se estrellara por completo.",
        "Reportan que unos niños jugando béisbol rompieron el ventanal de una casa; los padres se niegan a pagar los daños.",
        "Se atiende llamada de auxilio de un taxista cuyo vehículo fue apedreado por manifestantes en la avenida principal.",
        "El encargado de un hotel denuncia que huéspedes destrozaron las instalaciones de la habitación antes de hacer el check-out.",
        "Un masculino es detenido tras ser sorprendido rompiendo las cámaras de seguridad exteriores de un negocio comercial.",
        "Reportan que un camión recolector de basura golpeó el toldo de un local comercial provocando desprendimiento de láminas.",
        "Se reciben quejas de daños en propiedad; un sujeto quebró los candados de un portón vecinal para abrir el paso a la fuerza."
    ]

    # Etiquetas (34 de 0, 33 de 1, 33 de 2)
    labels = [0] * 34 + [1] * 33 + [2] * 33
    
    # Crear DataFrame
    df = pd.DataFrame({
        "narrativa": narrativas_sinteticas,
        "label_id": labels,
        "clase_delito": ["Robo o Hurto"]*34 + ["Lesiones por Agresión"]*33 + ["Daño en Propiedad Ajena"]*33
    })
    
    return df

# Ejecución
df_c5 = construir_dataset_ip()
df_c5.to_csv("dataset_c5_ip.csv", index=False)

print(f"✅ Dataset construido con {len(df_c5)} muestras.")
print(df_c5.head())
