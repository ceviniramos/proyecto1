import sqlite3
conn=sqlite3.connect("ositogominola.db")
cursor=conn.cursor()
def agregar():    

    nom=input('ingrese el nombre')
    edad=int(input('ingrese la edad'))
    pais=input('ingrese el pais')
    club=input('ingrese el club')
    goles=int(input('ingrese los goles'))
    conn.execute('''insert into futbol(nom,edad,pais,club,goles) values ('%s','%s','%s','%s','%s')'''%(nom,edad,pais,club,goles))
    conn.commit()
    conn.close()

def modificar():
    nombre = input("Nombre del jugador a actualizar")
    nueva_edad = int(input("Nueva edad"))
    sql = "UPDATE futbol SET edad = ? WHERE nombre = ?"
    conn.execute(sql, (nueva_edad, nombre))
    conn.commit()
    print("✔ Edad actualizada.\n")

def mostrar_jugadores():
    sql = "SELECT * FROM futbol"
    cursor = conn.execute(sql)
    jugadores = cursor.fetchall()
    print("Lista de jugadores")
    for jugador in jugadores:
        print(jugador)
    print()

def eliminar_menores():
    edad_limite = int(input("Eliminar jugadores menores a: "))
    sql = "DELETE FROM futbol WHERE edad < ?"
    conn.execute(sql, (edad_limite,))
    conn.commit()
    print(f"✔ Jugadores menores de {edad_limite} eliminados.\n")

def buscar_por_nombre():
    nombre = input("Buscar jugador por nombre: ")
    sql = "SELECT * FROM futbol WHERE nombre LIKE ?"
    cursor = conn.execute(sql, (f"%{nombre}%",))
    resultados = cursor.fetchall()
    print("\n--- Resultados de búsqueda ---")
    for jugador in resultados:
        print(jugador)
    print()


while True:
    print("=== MENÚ FÚTBOL ===")
    print("1. Agregar jugador")
    print("2. Actualizar edad por nombre")
    print("3. Mostrar todos los jugadores")
    print("4. Eliminar jugadores menores de cierta edad")
    print("5. Buscar jugador por nombre")
    print("6. Estadísticas")
    print("7. Salir")

    opcion = input("Selecciona una opción: ")

    match opcion:
        case "1":
            agregar()
        case "2":
            modificar()
        case "3":
            mostrar_jugadores()
        case "4":
            eliminar_menores()
        case "5":
            buscar_por_nombre()

        case "7":
            print("Saliendo del programa.")
        case _:
            print("Opción inválida. Intenta otra vez.\n")
