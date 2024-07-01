# Descripción

Este proyecto tiene como objetivo desarrollar y simular un modelo basado en utilidad para la distribución y asignación óptima de recursos en entornos de computación en la nube. 
La idea principal es hacer uso de funciones de utilidad para representar la satisfacción del usuario o el valor derivado de diferentes configuraciones para los recursos disponibles en tal forma que se pueda maximizar la utilidad global. 
El proyecto implica diseñar un ambiente en la nube simulado donde usuarios con diferentes requisitos de recursos y funciones de utilidad interactúan con los recursos disponibles gestionados por los algoritmos de asignación.
## Componentes clave:
- **Gestión de recursos:** Incluye diferentes tipos de recursos (CPU, RAM, almacenamiento) con atributos como capacidad total y disponible.
- **Funciones de utilidad:** Representan la satisfacción que obtienen los usuarios al consumir cantidades específicas de recursos, modeladas mediante funciones polinómicas u otras funciones matemáticas.
- **Algoritmos de asignación:** Implementan varias estrategias para la asignación de recursos, entre las cuales se incluyen algoritmos codiciosos, basados en la optimización y heurísticos, para determinar el método más eficaz para maximizar la utilidad total.
- **Entorno de simulación:** Un entorno de nube virtual en el que los usuarios solicitan recursos y los algoritmos de asignación gestionan la distribución de estos recursos para maximizar la utilidad total.

---

# Justificación
La asignación eficiente de recursos es un problema general para empresas y usuarios que buscan migrar sus sistemas a ambientes en la nube, en los cuales delegar la maquinaria sostén para sus sistemas. 
Sin embargo, optimizar el rendimiento y la satisfacción de los usuarios sin incurrir en elevados costos es un ejercicio bastante complejo incluso hoy en día. 
Los métodos tradicionales de asignación de recursos no suelen ajustarse de forma dinámica con base en la demanda del usuario, aunque objetos como balanceadores de carga existen para estas labores, en la práctica, el análisis manual y el diagnóstico toman más parte que las labores automatizadas.
## Principales ventajas:
- **Mejora de la satisfacción del usuario:** Al modelar las preferencias y la satisfacción de los usuarios mediante funciones de utilidad, el proyecto pretende asignar los recursos de forma que satisfagan mejor las necesidades de los usuarios, lo que redundará en una mayor satisfacción.
- **Utilización optimizada de los recursos:** Los algoritmos de asignación eficientes pueden ayudar a maximizar la utilización de los recursos disponibles, reduciendo los residuos y mejorando el rendimiento general del sistema.
- **Adaptación dinámica:** El proyecto pretende desarrollar mecanismos que puedan adaptar la asignación de recursos en tiempo real en función de las cambiantes demandas de los usuarios y la disponibilidad de recursos, mejorando la resistencia y flexibilidad de los servicios en la nube.
- **Escalabilidad:** El entorno de simulación se diseñará para manejar un número variable de usuarios y recursos, garantizando que las soluciones propuestas puedan escalar eficazmente.
