from datetime import time, datetime


def main():
    ahora = datetime.now().time()
    horaSalida = time(19, 0, 0)

    print("la hora de salida es", horaSalida)
    print("la hora actual es", ahora.isoformat())

    if ahora >= horaSalida:
        print("Son las 7, es hora de salir")
    else:
        faltaHora = horaSalida.hour - ahora.hour
        faltaMinuto = horaSalida.minute - ahora.minute + 59
        faltaSegundo = horaSalida.second - ahora.second + 59
        print("faltan", faltaHora, "horas con", faltaMinuto, "minutos y", faltaSegundo,
              "segundos para terminar de trabajar por hoy")


if __name__ == "__main__":
    main()
