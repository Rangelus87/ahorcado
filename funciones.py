from tkinter import messagebox as ms
import sqlite3
import listas
import random


def guardar_usuario(user):
    conex = sqlite3.connect("Base1.db")
    conex.execute("insert into usuarios (usuario) values(?)", (user,))
    conex.commit()
    conex.close()


def select_pais():
    """
    funcion que selecciona una palabra random de una lista, crea una tabla en la bd y agrega la palabra en dicha tabla
    """
    pais = random.choice(listas.lista_paises)
    conex1 = sqlite3.connect("Base1.db")
    conex1.execute("drop table if exists pais")
    conex1.execute("create table pais (pais text)")
    conex1.execute("insert into pais(pais) values(?)", (pais,))
    conex1.commit()
    conex1.close()
    return cambio_letras()


def cambio_letras():
    """
    funcion que recibe un string y devuelve cada caracter del string como guiones,
    crea una tabla y agrega el string de guiones en dicha tabla
    """
    conex2 = sqlite3.connect("Base1.db")
    dato = conex2.cursor()
    dato.execute("select pais from pais")
    pais = dato.fetchall()[0]
    palabra = ""
    for a in pais:
        palabra = a
    print(palabra)
    guiones = "".join(["_" if letra != " " else " " for letra in palabra])
    print(guiones)
    return guiones


def comprobar_letras(letra):
    """
    funcion que recibe un caracter primero comprueba que sea una letra del alfabeto,
    segungo la agrega a una lista con los caracteres que se han ingresado anteriormente,
    crea una tabla en la BD y agrega dicha lista a la base de datos
    :param letra:
    :return:
    """

    if not letra.isalpha() or len(letra) > 1:
        ms.showerror("Error", "Ha ingresado mas de una letra o un caracter "
                              "invalido, \n Presione \"Esc\" para salir")

    conex_char = sqlite3.connect("Base1.db")
    cursor_char = conex_char.cursor()
    cursor_char.execute("SELECT * FROM caracteres WHERE letra= ?", (letra,))
    character = cursor_char.fetchall()
    conex_char.close()

    if character:
        ms.showerror("Error", f"Error ya incertaste el caracter {letra}")
    else:
        conex3 = sqlite3.connect("Base1.db")
        conex3.execute("insert into caracteres(letra) values(?)", (letra,))
        conex3.commit()
        conex3.close()
    return letra


def fun_contador(palabra, letra, contador):
    if letra not in palabra:
        contador -= 1
        conex_contador = sqlite3.connect("Base1.db")
        conex_contador.execute("update contador set num = ?", (contador,))
        conex_contador.commit()
        conex_contador.close()
        print("num = ", contador)

    if contador == 0:
        ms.showinfo("Perdio", "Lo siento se te acabaron las oportunidades")
    return contador


def recupero_datos():
    # recupero los caracteres de la base de datos
    conex4 = sqlite3.connect("Base1.db")
    cursor0 = conex4.cursor()
    cursor0.execute("select letra from caracteres")
    recupero_letra = cursor0.fetchall()

    letras = []
    for a in recupero_letra:
        letras.append(a[0])
    print(f"la letra es {letras}")

    # recupero el pais de la base de datos
    cursor1 = conex4.cursor()
    cursor1.execute("select pais from pais")
    recupero_pais = cursor1.fetchall()[0]

    palabra = ""
    for c in recupero_pais:
        palabra = c
    print(f"la palabra es {palabra}")

    cursor2 = conex4.cursor()
    cursor2.execute("select num from contador")
    contador = cursor2.fetchall()[0]
    print(contador[0])

    conex4.commit()
    conex4.close()

    count = fun_contador(palabra, letras[-1], contador[0])
    cambio = cambio_caracter(letras, palabra)

    # llamo a la funcion que hace el cambio de caracter en casao que exista en la palabra
    return count, cambio


def cambio_caracter(caracteres, palabra):
    # sustituimos el caracter en los guiones
    sustituto = ""

    for c in palabra:
        if c.lower() in [char.lower() for char in caracteres]:
            sustituto += c
        elif c == " ":
            sustituto += " "
        else:
            sustituto += "_"
    print("este es el sustituto ", sustituto)

    # mando el cambio a la base de datos y en caso que se adivine la palabra se borran las letras de la base de datos
    conex5 = sqlite3.connect("Base1.db")
    cursor3 = conex5.cursor()
    cursor3.execute("drop table if exists agregar")
    cursor3.execute("create table agregar(sustituto text)")
    cursor3.execute("insert into agregar(sustituto) values(?)", (sustituto,))
    conex5.commit()
    conex5.close()
    if sustituto == palabra:
        final()
        gano()
    return sustituto


def gano():
    ms.showinfo("Felicidades", "Felicidades, adivinaste la palabra")
    final()


def borrar_caracteres():
    conex6 = sqlite3.connect("Base1.db")
    conex6.execute("DELETE FROM caracteres")
    conex6.commit()
    conex6.close()


def contador_0():
    conex_contador = sqlite3.connect("Base1.db")
    conex_contador.execute("update contador set num = ?", (10,))
    conex_contador.commit()
    conex_contador.close()


def final():
    contador_0()
    borrar_caracteres()
