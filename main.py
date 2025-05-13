import sqlite3
conn=sqlite3.connect("ositogominola.db")
cursor=conn.cursor()
def agregar():    
    conn=sqlite3.connect ("ositogominola.db")
    nom=input('ingrese el nombre')
    edad=int(input('ingrese la edad'))
    pais=input('ingrese el pais')
    club=input('ingrese el club')
    goles=int(input('ingrese los goles'))
    conn.execute('''insert into jugadores(nombre,edad,pais,club,goles) values ('%s','%s')'''% (nom,edad,pais,club,goles))



