"""
Escáner de Puertos TCP
Asignatura: Seguridad Informática - UNEMI
Práctica: Desarrollo de un Escáner de Puertos de Red utilizando Python

Uso ético y responsable:
Este programa debe ejecutarse ÚNICAMENTE sobre equipos propios, máquinas
virtuales o redes autorizadas. Escanear equipos de terceros sin autorización
es ilegal y va en contra de los principios de uso responsable de esta práctica.
"""

import socket
import sys
from datetime import datetime


def validar_ip(direccion_ip):
    """Valida que la cadena ingresada sea una dirección IP válida."""
    try:
        socket.inet_aton(direccion_ip)
        return True
    except socket.error:
        return False


def escanear_puerto(ip, puerto, timeout=0.5):
    """
    Intenta conectarse a un puerto TCP específico.
    Retorna True si el puerto está abierto, False si está cerrado/filtrado.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    resultado = sock.connect_ex((ip, puerto))
    sock.close()
    return resultado == 0


def escanear_rango(ip, puerto_inicial, puerto_final):
    """
    Escanea un rango de puertos TCP sobre una IP dada.
    Retorna una lista con los puertos que se encontraron abiertos.
    """
    puertos_abiertos = []
    total_puertos = puerto_final - puerto_inicial + 1

    print("\nESCÁNER DE PUERTOS")
    print(f"IP: {ip}")
    print(f"Desde: {puerto_inicial}")
    print(f"Hasta: {puerto_final}")
    print("Escaneando...\n")

    inicio = datetime.now()

    for puerto in range(puerto_inicial, puerto_final + 1):
        if escanear_puerto(ip, puerto):
            print(f"Puerto {puerto} - ABIERTO")
            puertos_abiertos.append(puerto)

    fin = datetime.now()
    duracion = (fin - inicio).total_seconds()

    print(f"\nPuertos analizados: {total_puertos}")
    print(f"Puertos abiertos: {len(puertos_abiertos)}")
    print(f"Tiempo de escaneo: {duracion:.2f} segundos")

    return puertos_abiertos


def solicitar_datos():
    """Pide al usuario la IP y el rango de puertos, validando la entrada."""
    while True:
        ip = input("Ingrese la dirección IP a escanear: ").strip()
        if validar_ip(ip):
            break
        print("Dirección IP inválida. Intente nuevamente (ej. 192.168.1.10).")

    while True:
        try:
            puerto_inicial = int(input("Ingrese el puerto inicial (1-65535): "))
            puerto_final = int(input("Ingrese el puerto final (1-65535): "))

            if not (1 <= puerto_inicial <= 65535) or not (1 <= puerto_final <= 65535):
                print("Los puertos deben estar entre 1 y 65535.")
                continue
            if puerto_inicial > puerto_final:
                print("El puerto inicial no puede ser mayor que el puerto final.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")

    return ip, puerto_inicial, puerto_final


def main():
    print("=" * 40)
    print(" ESCÁNER DE PUERTOS TCP - Python")
    print(" Uso permitido solo en equipos/redes autorizadas")
    print("=" * 40)

    ip, puerto_inicial, puerto_final = solicitar_datos()

    try:
        puertos_abiertos = escanear_rango(ip, puerto_inicial, puerto_final)

        print("\nRESUMEN FINAL")
        print("-" * 30)
        if puertos_abiertos:
            print(f"Puertos abiertos encontrados: {puertos_abiertos}")
        else:
            print("No se encontraron puertos abiertos en el rango indicado.")

    except KeyboardInterrupt:
        print("\nEscaneo interrumpido por el usuario.")
        sys.exit(0)
    except socket.gaierror:
        print("Error: no se pudo resolver la dirección IP/host indicado.")
        sys.exit(1)


if __name__ == "__main__":
    main()
