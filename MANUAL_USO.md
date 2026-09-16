# Manual de Uso - Escáner de Puertos TCP

## 1. Requisitos para ejecutar el programa

- Tener instalado **Python 3.8 o superior**.
- No se requieren librerías externas: el programa solo usa módulos estándar de Python (`socket`, `sys`, `datetime`).
- Acceso a una terminal o consola de comandos.
- Permiso para escanear el equipo/red de destino (solo equipos propios, VM o laboratorio autorizado).

## 2. Instalación

1. Descargar o clonar el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Ingresar a la carpeta del proyecto:
   ```
   cd scanner-puertos-python
   ```
3. Verificar que Python esté instalado:
   ```
   python3 --version
   ```

## 3. Cómo iniciar la aplicación

Desde la terminal, dentro de la carpeta del proyecto, ejecutar:

```
python3 scanner_puertos.py
```

## 4. Cómo ingresar la IP

Al iniciar, el programa solicitará la dirección IP del equipo a escanear:

```
Ingrese la dirección IP a escanear: 192.168.1.10
```

> Para probar en el propio equipo, se puede usar `127.0.0.1` (localhost).

Si el formato de la IP no es válido, el programa pedirá que se ingrese nuevamente.

## 5. Cómo seleccionar el rango de puertos

El programa solicitará el puerto inicial y el puerto final del rango a analizar:

```
Ingrese el puerto inicial (1-65535): 1
Ingrese el puerto final (1-65535): 100
```

Reglas de validación:
- Ambos valores deben estar entre 1 y 65535.
- El puerto inicial no puede ser mayor que el puerto final.

## 6. Cómo ejecutar el escaneo

Una vez ingresados la IP y el rango de puertos, el escaneo comienza automáticamente. El programa probará, uno por uno, si cada puerto del rango indicado responde a una conexión TCP.

Mientras se ejecuta, se mostrará en pantalla cada puerto que se encuentre **ABIERTO**.

## 7. Cómo interpretar los resultados

Al finalizar, el programa muestra un resumen:

```
Puertos analizados: 100
Puertos abiertos: 2
Tiempo de escaneo: 1.85 segundos

RESUMEN FINAL
------------------------------
Puertos abiertos encontrados: [22, 80]
```

- **Puertos analizados:** cantidad total de puertos revisados en el rango.
- **Puertos abiertos:** cantidad de puertos que respondieron a la conexión (servicio activo).
- **Puertos no listados:** se consideran cerrados o filtrados (no respondieron a la conexión TCP).

## Notas importantes

- El escaneo puede tardar más tiempo mientras más amplio sea el rango de puertos.
- Usar esta herramienta solo con fines educativos y sobre equipos/redes autorizados.
