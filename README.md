# Escáner de Puertos de Red - Python

Aplicación básica desarrollada en Python que permite realizar un escaneo de puertos TCP sobre un equipo autorizado e identificar los puertos abiertos.

**Asignatura:** Seguridad Informática
**Carrera:** Tecnologías de la Información en Modalidad en Línea
**Práctica:** Desarrollo de un Escáner de Puertos de Red utilizando Python

## ⚠️ Uso responsable

Este programa debe ejecutarse **únicamente** sobre:
- Equipos propios
- Máquinas virtuales
- Redes autorizadas / laboratorio autorizado

Escanear equipos de terceros sin autorización expresa es ilegal.

## Herramientas utilizadas

- Python 3
- Visual Studio Code
- GitHub
- Biblioteca `socket` (estándar de Python)

## Contenido del repositorio

```
scanner-puertos-python/
├── scanner_puertos.py
├── README.md
└── MANUAL_USO.md
```

## Instalación rápida

1. Tener Python 3.8 o superior instalado.
2. Clonar este repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd scanner-puertos-python
   ```
3. Ejecutar el script:
   ```
   python3 scanner_puertos.py
   ```

Para más detalle sobre el funcionamiento, ver [MANUAL_USO.md](MANUAL_USO.md).

## Ejemplo de salida

```
ESCÁNER DE PUERTOS
IP: 192.168.1.10
Desde: 1
Hasta: 100
Escaneando...
Puerto 22 - ABIERTO
Puerto 80 - ABIERTO
Puertos analizados: 100
Puertos abiertos: 2
```

## Declaración de uso de Inteligencia Artificial (IA)

Yo, ____________________________, declaro que utilicé herramientas de Inteligencia Artificial como apoyo parcial en la elaboración del presente trabajo. La información generada fue verificada, analizada críticamente y utilizada de manera ética, conforme a los criterios establecidos en la actividad.
