#!/usr/bin/env python3
import math
import corrige_filters
# Pas utilisées, mais utiles pour faire écrire des tests
import random
import time

# fonctions annexes


def moyenne(valeurs: tuple or list) -> int:
    """
    Renvoie la moyenne d'un tuple ou d'une liste
    :param valeurs: un tuple ou une liste de nombres (entiers ou flottants)
    :return: la moyenne entière des valeurs du tuple ou de la liste
    """
    assert type(valeurs) == tuple or type(valeurs) == list
    return sum(valeurs) // len(valeurs)


def test_moyenne_1() -> bool:
    """
    Vérifie le bon fonctionnement de la fonction moyenne
    :return: True si tout va bien, False sinon
    """
    if moyenne([5, 6, 7, 8]) != 6:
        return False  # cas d'un nombre de valeurs pair
    return moyenne([5, 6, 7, 8, 9]) == 7  # cas d'un nombre de valeurs impair


def test_moyenne_2() -> None:
    """
    Vérifie le bon fonctionnement des asserts de la fonction moyenne
    :return: None
    """
    # moyenne(5)
    # moyenne(True)
    # moyenne("Cela ne marche pas")


# Section 4.2
# Manipulation d'images


def read_pixel(img: tuple, x: int, y: int) -> tuple:
    """
    Renvoie le code RGB du pixel (x, y) de l'image img
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param x: un entier strictement inférieur à la largeur de l'image
    :param y: un entier strictement inférieur à la hauteur de l'image
    :return: un triplet d'entiers formant le code RGB du pixel (x, y)
    """
    assert -1 < x < img[0] and -1 < y < img[1]
    ligne = img[0] * 3 * y
    colonne = x * 3
    pixel_1 = ligne + colonne  # permet de calculer l'indice de la valeur R du pixel (x, y)
    return img[2][pixel_1], img[2][pixel_1 + 1], img[2][pixel_1 + 2]


def test_read_pixel_1(img: tuple, image_test: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction read_pixel
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si tout va bien, False sinon
    """
    if read_pixel(image_test, 0, 0) != (0, 0, 0):
        return False  # cas du premier pixel de l'image
    if read_pixel(image_test, 1, 0) != (1, 1, 1):
        return False  # cas d'un pixel quelconque dans l'image
    if read_pixel(image_test, 2, 1) != (5, 5, 5):
        return False  # cas du dernier pixel de l'image

    # tests plus approfondis avec des valeurs aléatoires, utilisant la correction comme référentiel
    for _ in range(10):
        x = random.randint(0, img[0] - 1)
        y = random.randint(0, img[1] - 1)
        if corrige_filters.read_pixel(img, x, y) != read_pixel(img, x, y):
            return False
    return True


def test_read_pixel_2(img: tuple) -> None:
    """
    Vérifie le bon fonctionnement des asserts de la fonction read_pixel
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :return: None
    """
    x, y = img[0], img[1]
    # read_pixel(img, x, 0)
    # read_pixel(img, 0, y)
    # read_pixel(img, -1, 0)
    # read_pixel(img, 0, -1)


def write_pixel(img: tuple, x: int, y: int, color: tuple) -> None:
    """
    Remplace le pixel (x, y) par la couleur donnée par color
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param x: un entier strictement inférieur à la largeur de l'image
    :param y: un entier strictement inférieur à la hauteur de l'image
    :param color: une couleur RGB sous la forme d'un triplet d'entiers
    :return: None (a redessiné un pixel de img)
    """
    assert -1 < x < img[0] and -1 < y < img[1]
    ligne = img[0] * 3 * y
    colonne = x * 3
    pixel_1 = ligne + colonne  # permet de calculer l'indice de la composante R du pixel (x, y)
    img[2][pixel_1] = color[0]
    img[2][pixel_1 + 1] = color[1]
    img[2][pixel_1 + 2] = color[2]


def test_write_pixel_1(img: tuple, image_test: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction write_pixel
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si tout va bien, False sinon
    """
    write_pixel(image_test, 0, 0, (12, 12, 14))
    write_pixel(image_test, 1, 0, (3, 2, 4))
    write_pixel(image_test, 2, 1, (0, 0, 0))
    if read_pixel(image_test, 0, 0) != (12, 12, 14):
        return False  # cas du premier pixel dans l'image
    if read_pixel(image_test, 1, 0) != (3, 2, 4):
        return False  # cas d'un pixel quelconque dans l'image
    if read_pixel(image_test, 2, 1) != (0, 0, 0):
        return False  # cas du dernier pixel dans l'image
    if read_pixel(image_test, 0, 1) != (3, 3, 3):
        return False  # cas d'un pixel resté inchangé

    # tests plus approfondis avec des valeurs aléatoires, utilisant la correction comme référentiel
    for _ in range(10):
        x = random.randint(0, img[0] - 1)
        y = random.randint(0, img[1] - 1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if corrige_filters.write_pixel(img, x, y, color) != write_pixel(img, x, y, color):
            return False
    return True


def test_write_pixel_2(img: tuple) -> None:
    """
    Vérifie le bon fonctionnement des asserts de la fonction write_pixel
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :return: None
    """
    x, y = img[0], img[1]
    # write_pixel(img, x, 0)
    # write_pixel(img, 0, y)
    # write_pixel(img, -1, 0)
    # write_pixel(img, 0, -1)


def copy_image(img: tuple) -> tuple:
    """
    Renvoie une copie de l'image donnée en entrée
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :return: la copie indépendante de l'image
    """
    return img[0], img[1], list(img[2])  # permet de délier la liste de la nouvelle image et de l'image de base


def test_copy_image_1(img: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction copy_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée reste inchangée, False sinon
    """
    nouvelle_image = copy_image(img)
    write_pixel(img, 0, 0, (0, 0, 0))
    if img == nouvelle_image:  # l'image copiée et l'image de base modifiée doivent être différentes
        return False
    write_pixel(img, 0, 0, (255, 255, 255))
    return not(img == nouvelle_image)  # on teste deux couleurs pour être certain d'avoir modifié l'image


# Section 4.3
# Filtres simples


def inv_image(src: tuple) -> tuple:
    """
    Renvoie une copie de l'image src dont les couleurs sont inversées
    :param src: une image sous la forme d'un triplet (int, int, list[int])
    :return: la copie indépendante de l'image dont les couleurs ont été inversées
    """
    copie = copy_image(src)
    # parcours chaque composante de tous les pixels pour les inverser
    for i in range(len(copie[2])):
        copie[2][i] = 255 - copie[2][i]
    return copie


def test_inv_image_1(img: tuple, image_test: tuple, image_test_2: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction inv_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test_2: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée est bien inversée, False sinon
    """
    if inv_image(image_test) != (3, 2, [243, 243, 241, 252, 253, 251, 253, 253, 253, 252, 252, 252, 251, 251, 251,
                                        255, 255, 255]):
        return False  # cas de composants petits
    if inv_image(image_test_2) != (3, 2, [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]):
        return False  # cas de composants grands

    # test plus poussé avec la correction comme référentiel
    return corrige_filters.inv_image(img) == inv_image(img)


def gray_image(src: tuple) -> tuple:
    """
    Renvoie une copie de l'image src dont les couleurs sont des nuances de gris
    :param src: une image sous la forme d'un triplet (int, int, list[int])
    :return: la copie indépendante de l'image dont les couleurs sont des nuances de gris
    """
    copie = copy_image(src)
    x = 0
    # se déplace de gauche à droite sur l'image
    while x < src[0]:
        # change colonne par colonne chaque pixel de l'image
        for ligne in range(src[1]):
            nouvelle_composante = moyenne(read_pixel(copie, x, ligne))
            write_pixel(copie, x, ligne, (nouvelle_composante, nouvelle_composante, nouvelle_composante))
        x += 1
    return copie


def test_gray_image_1(img: tuple, image_test: tuple, image_test_2: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction gray_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test_2: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée est bien nuancée de gris, False sinon
    """
    if gray_image(image_test) != (3, 2, [2, 2, 2, 5, 5, 5, 8, 8, 8, 11, 11, 11, 14, 14, 14, 17, 17, 17]):
        return False  # cas quelconque
    if gray_image(image_test_2) != (3, 2, [6, 6, 6, 3, 3, 3, 6, 6, 6, 10, 10, 10, 10, 10, 10, 15, 15, 15]):
        return False  # cas où les composantes d'un pixel sont parfois toutes les mêmes

    # test plus poussé avec la correction comme référentiel
    return corrige_filters.gray_image(img) == gray_image(img)


def jail_image(src: tuple, bar_color: tuple, bar_width: int, bar_spacing: int) -> tuple:
    """
    Dessine des barres verticales de paramètres donnés ci-dessus sur l'image
    :param src: une image sous la forme d'un triplet (int, int, list[int])
    :param bar_color: une couleur sous la forme d'un triplet d'entiers
    :param bar_width: un entier strictement supérieur à 0 et inférieur ou égal à la largeur de src
    :param bar_spacing: un entier supérieur ou égal à 0
    :return: la copie indépendante de l'image avec les barres par dessus
    """
    assert 0 < bar_width <= src[0] and bar_spacing >= 0 and len(bar_color) == 3
    for i in bar_color:
        assert 0 <= i <= 255
    copie = copy_image(src)
    x = 0
    # en se déplaçant de gauche à droite, vérifie que la prochaine barre peut être entièrement dessinée
    while x + bar_width < src[0]:
        # dessine colonne par colonne chaque pixel de la barre
        for i in range(bar_width):
            for ligne in range(src[1]):
                write_pixel(copie, x, ligne, bar_color)
            x += 1
        x += bar_spacing
    # fais les dernières colonnes formant une barre incomplète, si cela est possible
    while x < src[0]:
        for ligne in range(src[1]):
            write_pixel(copie, x, ligne, bar_color)
        x += 1
    return copie


def test_jail_image_1(img: tuple, image_test: tuple, image_test_2: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction jail_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test_2: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée a bien les barres dessinées, False sinon
    """
    if jail_image(image_test, (255, 0, 0), 1, 1) != (3, 2, [255, 0, 0, 3, 2, 4, 255, 0, 0, 255, 0, 0, 4, 4, 4, 255,
                                                            0, 0]):
        return False  # cas quelconque
    if jail_image(image_test_2, (255, 255, 0), 1, 4) != (3, 2, [255, 255, 0, 2, 4, 5, 6, 7, 7, 255, 255, 0, 1, 10, 10,
                                                                8, 8, 9]):
        return False  # cas d'un espacement de barres supérieur à la taille de l'image
    if jail_image(image_test_2, (255, 255, 0), 1, 0) != (3, 2, [255, 255, 0, 255, 255, 0, 255, 255, 0, 255, 255, 0,
                                                                255, 255, 0, 255, 255, 0]):
        return False  # cas d'un espacement de barres nul

    # tests plus poussés avec la correction comme référentiel
    for _ in range(10):
        bar_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        bar_width = random.randint(1, img[0])
        bar_spacing = random.randint(1, img[0])
        """
        Impossible d'exécuter ces tests car sur certaines valeurs, le corrigé a une erreur d'assert:
        la fonction de la correction tombe occasionnelement sur un pixel qui n'existe pas
        """
        # if corrige_filters.jail_image(img, bar_color, bar_width, bar_spacing) != \
                # jail_image(img, bar_color, bar_width, bar_spacing):
            # return False
    return True


def test_jail_image_2(img: tuple) -> None:
    """
    Vérifie le bon fonctionnement des asserts de la fonction jail_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :return: None
    """
    # jail_image(img, (0, 0, 0), 0, 1)
    # jail_image(img, (0, 0, 0), img[0] + 1, 1)
    # jail_image(img, (0, 0, 0), 1, -1)
    # jail_image(img, (-1, 0, 0), 1, 1)
    # jail_image(img, (0, 0, 256), 1, 1)


def overlay_image(src: tuple, x0: int, y0: int, overlay: tuple, key: tuple) -> tuple:
    """
    Renvoie une copie de src avec l'overlay par-dessus, dont le coin gauche est en (x0, y0)
    :param src: une image sous la forme d'un triplet (int, int, list[int]), celle sur laquelle on superpose
    :param x0: la coordonnée x où commencer à superposer overlay
    :param y0: la coordonnée y où commencer à superposer overlay
    :param overlay: une image sous la forme d'un triplet (int, int, list[int]), celle à superposer
    :param key: la couleur à ne pas superposer
    :return: une copie de l'image de base avec l'overlay
    """
    assert -1 < x0 < src[0] and -1 < y0 < src[1] and len(key) == 3
    for i in key:
        assert 0 <= i <= 255
    copie = copy_image(src)
    x, y = x0, y0  # itère sur l'image originale
    x1 = 0  # itère sur l'overlay
    # se déplace de gauche à droite sur l'overlay
    while x1 < overlay[0]:
        # dessine colonne par colonne les bons pixels de l'overlay sur l'image originale
        for ligne in range(overlay[1]):
            if x < src[0] and y + ligne < src[1] and read_pixel(overlay, x1, ligne) != key:
                # le if ci-dessous traite uniquement le cas du dm où certains pixels verts n'ont pas le même
                # vert que key, avec pour conséquence l'apparition de pixels verts sur la copie de l'image
                # enlever le # devant le if et indenter la ligne suivante pour traiter le cas du dm
                # if read_pixel(overlay, x1, y1 + ligne) == (0, 0, 0):
                write_pixel(copie, x, y + ligne, read_pixel(overlay, x1, ligne))
        x += 1
        x1 += 1
    return copie


def test_overlay_image_1(img: tuple, other: tuple, image_test: tuple, image_test_2: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction overlay_image
    :param img: une image sous la forme d'un triplet (int, int, list[int]), celle sur laquelle on superpose
    :param other: une image sous la forme d'un triplet (int, int, list[int]), celle à superposer
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test_2: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée a bien l'overlay dessus, False sinon
    """
    overlay_test = (2, 2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4])
    resultat = (3, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0])
    overlay_test2 = (4, 4, [2, 3, 4, 1, 2, 5, 6, 6, 6, 6, 6, 6, 5, 3, 9, 6, 6, 6, 5, 2, 9, 8, 8, 8, 6, 7, 2, 6, 6, 6,
                            6, 6, 6, 1, 2, 3, 7, 6, 6, 6, 6, 6, 6, 6, 7, 6, 7, 6])
    resultat_2 = (3, 2, [2, 3, 4, 1, 2, 5, 6, 7, 7, 5, 3, 9, 1, 10, 10, 5, 2, 9])
    if overlay_image(image_test, 1, 1, overlay_test, (4, 4, 4)) != resultat:
        return False  # cas où l'overlay est plus petit que l'image de base et rentre entièrement dedans
    if overlay_image(image_test_2, 0, 0, overlay_test2, (6, 6, 6)) != resultat_2:
        return False  # cas où l'overlay est plus grand que l'image de base

    # test plus poussé avec la correction comme référentiel
    return corrige_filters.overlay_image(img, 160, 10, other, (0, 255, 0)) == overlay_image(img, 160, 10, other,
                                                                                            (0, 255, 0))


def test_overlay_image_2(img: tuple, other: tuple) -> None:
    """
    Vérifie le bon fonctionnement des asserts de la fonction overlay_image
    :param img: une image sous la forme d'un triplet (int, int, list[int]), celle sur laquelle on superpose
    :param other: une image sous la forme d'un triplet (int, int, list[int]), celle à superposer
    :return: None
    """
    # overlay_image(img, 512, 10, other, (0, 255, 0))
    # overlay_image(img, -1, 10, other, (0, 255, 0))
    # overlay_image(img, 160, 512, other, (0, 255, 0))
    # overlay_image(img, 160, -1, other, (0, 255, 0))
    # overlay_image(img, 160, 10, other, (0, 256, 0))
    # overlay_image(img, 160, 10, other, (-1, 255, 0))


def scale_image(src: tuple, fw: float, fh: float) -> tuple:
    """
    Redimensionne une image verticalement et horizontalement selon les coefficients fw et fh
    :param src: une image sous la forme d'un triplet (int, int, list[int])
    :param fw: un flottant strictement positif
    :param fh: un flottant strictement positif
    :return: une copie redimensionnée de l'image
    """
    assert fw > 0 and fh > 0
    # crée une image totalement blanche de taille (x * fw, y * fh), l'image de destination
    copie = (int(src[0] * fw), int(src[1] * fh), [0 for _ in range(int(src[0] * fw) * int(src[1] * fh) * 3)])
    x = 0
    # on se déplace de gauche à droite sur l'image de destination
    while x < copie[0]:
        # dessine colonne par colonne chaque pixel de l'image de destination
        for ligne in range(copie[1]):
            # pixel par pixel, on utilise la méthode des plus proches voisins pour déterminer à quel
            # pixel de l'image originale le pixel de celle de destination appartient
            write_pixel(copie, x, ligne, read_pixel(src, int(x / fw), int(ligne / fh)))
        x += 1
    return copie


def test_scale_image_1(img: tuple, image_test: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction scale_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée a été correctement redimensionnée, False sinon
    """
    if scale_image(image_test, 1.2, 0.8) != (4, 4, [0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2,
                                                    4, 5, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 0, 5, 7, 2, 5,
                                                    3, 2, 4, 5]):
        return False  # cas où fw grandit et fh rétrécit
    if scale_image(image_test, 0.8, 1.2) != (3, 6, [0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 2,
                                                    5, 3, 2, 4, 5, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 2, 5, 3, 2, 4,
                                                    5, 0, 5, 7, 2, 5, 3, 2, 4, 5]):
        return False  # cas où fw rétrécit et fh grandit
    if scale_image(image_test, 1.2, 1.2) != (4, 6, [0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2,
                                                    4, 5, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 0, 5, 7, 2, 5,
                                                    3, 2, 4, 5, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 0, 5, 7,
                                                    2, 5, 3, 2, 4, 5]):
        return False  # cas où fw et fh grandissent
    if scale_image(image_test, 0.8, 0.8) != (3, 4, [0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 2,
                                                    5, 3, 2, 4, 5, 0, 5, 7, 2, 5, 3, 2, 4, 5]):
        return False  # cas où fw et fh rétrécissent

    # tests plus poussés avec la correction comme référentiel
    for _ in range(10):
        fw = random.uniform(0.5, 2.5)
        fh = random.uniform(0.5, 2.5)
        if corrige_filters.scale_image(img, fw, fh) != scale_image(img, fw, fh):
            return False
    return True


def test_scale_image_2(img: tuple) -> None:
    """
    Vérifie le bon fonctionnement des asserts de la fonction scale_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :return: None
    """
    # scale_image(img, 0, 1)
    # scale_image(img, 1, 0)


# Section 4.4
# Filtres avancés


def mosaic_image(src: tuple, block_size: int) -> tuple:
    """
    Pixélise l'image src avec des blocs d'une taille donnée
    :param src: une image sous la forme d'un triplet (int, int, list[int])
    :param block_size: un entier strictement supérieur à 0
    :return: une copie pixélisée de l'image
    """
    assert block_size > 0
    copie = copy_image(src)
    x, y = 0, 0
    # se déplace de gauche à droite puis de haut en bas, bloc par bloc (comme si on lisait un livre)
    while x < copie[0] and y < copie[1]:
        composante_1, composante_2, composante_3, pixels = 0, 0, 0, 0
        colonne = 0
        # récupère la couleur de chaque pixel d'un bloc sur l'image source pour faire la moyenne des composantes
        while colonne < block_size and x + colonne < src[0]:
            ligne = 0
            while ligne < block_size and y + ligne < src[1]:
                couleur = read_pixel(src, x + colonne, y + ligne)
                pixels += 1
                composante_1 += couleur[0]
                composante_2 += couleur[1]
                composante_3 += couleur[2]
                ligne += 1
            colonne += 1
        couleur_pixel = (composante_1 // pixels, composante_2 // pixels, composante_3 // pixels)
        # dessine chaque pixel d'un bloc sur l'image de destination, selon la couleur du bloc
        colonne = 0
        while colonne < block_size and x + colonne < src[0]:
            ligne = 0
            while ligne < block_size and y + ligne < src[1]:
                write_pixel(copie, x + colonne, y + ligne, couleur_pixel)
                ligne += 1
            colonne += 1
        x += block_size
        # revient à la ligne d'en dessous tout à gauche
        if x >= copie[0]:
            x = 0
            y += block_size
    return copie


def test_mosaic_image_1(img: tuple, image_test: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction mosaic_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée est bien pixélisée, False sinon
    """
    if mosaic_image(image_test, 1) != (4, 5, [0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2, 0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2,
                                              0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2, 0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2,
                                              0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2]):
        return False  # cas où la mosaïque fait 1 pixel
    if mosaic_image(image_test, 2) != (4, 5, [1, 5, 5, 1, 5, 5, 4, 5, 3, 4, 5, 3, 1, 5, 5, 1, 5, 5, 4, 5, 3, 4, 5, 3,
                                              1, 5, 5, 1, 5, 5, 4, 5, 3, 4, 5, 3, 1, 5, 5, 1, 5, 5, 4, 5, 3, 4, 5, 3,
                                              1, 5, 5, 1, 5, 5, 4, 5, 3, 4, 5, 3]):
        return False  # cas où la mosaïque est un diviseur de la largeur ou la hauteur
    if mosaic_image(image_test, 3) != (4, 5, [1, 4, 5, 1, 4, 5, 1, 4, 5, 6, 7, 2, 1, 4, 5, 1, 4, 5, 1, 4, 5, 6, 7, 2,
                                              1, 4, 5, 1, 4, 5, 1, 4, 5, 6, 7, 2, 1, 4, 5, 1, 4, 5, 1, 4, 5, 6, 7, 2,
                                              1, 4, 5, 1, 4, 5, 1, 4, 5, 6, 7, 2]):
        return False  # cas quelconque
    if mosaic_image(image_test, 4) != (4, 5, [2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4,
                                              2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4,
                                              2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4]):
        return False  # cas où la mosaïque est égale à la largeur ou la haute
    if mosaic_image(image_test, 5) != (4, 5, [2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4,
                                              2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4,
                                              2, 5, 4, 2, 5, 4, 2, 5, 4, 2, 5, 4]):
        return False  # cas où la mosaïque est supérieur à la largeur ou la haute

    # tests plus poussés avec la correction comme référentiel
    tab = []
    for _ in range(10):
        bloc = random.randint(1, 512)
        if mosaic_image(img, bloc) != corrige_filters.mosaic_image(img, bloc):
            return False
    return True


def test_mosaic_image_2(img: tuple) -> None:
    """
    Vérifie le bon fonctionnement des asserts de la fonction mosaic_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :return: None
    """
    # mosaic_image(img, 0)


def rotate_image(src: tuple, a: float) -> tuple:
    """
    Renvoie une copie de src tournée de a radians
    :param src: une image sous la forme d'un triplet (int, int, list[int])
    :param a: un nombre de degrés de rotation exprimé en radian
    :return:
    """
    centre = (int(src[0] / 2), int(src[1] / 2))
    point_max_x, point_max_y, point_min_x, point_min_y = 0, 0, src[0] * 2, src[1] * 2
    # cherche la coordonnée la plus grande et la plus petite pour créer l'image de destination aux bonnes dimensions
    image_x = int((0 - centre[0]) * math.cos(a) - (0 - centre[1]) * math.sin(a) + centre[0])
    image_y = int((0 - centre[0]) * math.sin(a) + (0 - centre[1]) * math.cos(a) + centre[0])
    if image_x > point_max_x:
        point_max_x = image_x
    elif image_x < point_min_x:
        point_min_x = image_x
    if image_y > point_max_y:
        point_max_y = image_y
    elif image_y < point_min_y:
        point_min_y = image_y
    image_x = int((src[0] - centre[0]) * math.cos(a) - (0 - centre[1]) * math.sin(a) + centre[0])
    image_y = int((src[0] - centre[0]) * math.sin(a) + (0 - centre[1]) * math.cos(a) + centre[0])
    if image_x > point_max_x:
        point_max_x = image_x
    elif image_x < point_min_x:
        point_min_x = image_x
    if image_y > point_max_y:
        point_max_y = image_y
    elif image_y < point_min_y:
        point_min_y = image_y
    image_x = int((0 - centre[0]) * math.cos(a) - (src[1] - centre[1]) * math.sin(a) + centre[0])
    image_y = int((0 - centre[0]) * math.sin(a) + (src[1] - centre[1]) * math.cos(a) + centre[0])
    if image_x > point_max_x:
        point_max_x = image_x
    elif image_x < point_min_x:
        point_min_x = image_x
    if image_y > point_max_y:
        point_max_y = image_y
    elif image_y < point_min_y:
        point_min_y = image_y
    image_x = int((src[0] - centre[0]) * math.cos(a) - (src[1] - centre[1]) * math.sin(a) + centre[0])
    image_y = int((src[0] - centre[0]) * math.sin(a) + (src[1] - centre[1]) * math.cos(a) + centre[0])
    if image_x > point_max_x:
        point_max_x = image_x
    elif image_x < point_min_x:
        point_min_x = image_x
    if image_y > point_max_y:
        point_max_y = image_y
    elif image_y < point_min_y:
        point_min_y = image_y
    taille_x, taille_y = point_max_x - point_min_x, point_max_y - point_min_y
    copie = (taille_x, taille_y, [0 for _ in range(taille_x * taille_y * 3)])
    # on se déplace de gauche à droite sur l'image originale
    x = 0
    new_centre = (copie[0] / 2, copie[1] / 2)
    while x < copie[0]:
        # dessine colonne par colonne chaque pixel de l'image originale sur celle de destination
        for ligne in range(copie[1]):
            x_pixel_base = int((x - new_centre[0]) * math.cos(-a) - (ligne - new_centre[1]) * math.sin(-a) + centre[0])
            y_pixel_base = int((x - new_centre[0]) * math.sin(-a) + (ligne - new_centre[1]) * math.cos(-a) + centre[1])
            if 0 <= x_pixel_base < src[0] and 0 <= y_pixel_base < src[1]:
                write_pixel(copie, x, ligne, read_pixel(src, x_pixel_base, y_pixel_base))
        x += 1
    return copie


def test_rotate_image_1(img: tuple, image_test: tuple) -> bool:
    """
    Vérifie le bon fonctionnement de la fonction mosaic_image
    :param img: une image sous la forme d'un triplet (int, int, list[int])
    :param image_test: une image sous la forme d'un triplet (int, int, list[int])
    :return: True si l'image copiée est bien tournée, False sinon
    """
    if rotate_image(image_test, math.pi/2) != (5, 4, [0, 5, 7, 0, 5, 7, 0, 5, 7, 0, 5, 7, 0, 5, 7, 0, 5, 7, 2, 5, 3,
                                                      2, 5, 3, 2, 5, 3, 2, 5, 3, 2, 5, 3, 2, 4, 5, 2, 4, 5, 2, 4, 5,
                                                      2, 4, 5, 6, 7, 2, 6, 7, 2, 6, 7, 2, 6, 7, 2, 6, 7, 2]):
        return False
    if rotate_image(image_test, math.pi/3) != (5, 5, [0, 0, 0, 0, 5, 7, 0, 5, 7, 0, 5, 7, 0, 5, 7, 0, 5, 7, 0, 5, 7,
                                                      0, 5, 7, 0, 5, 7, 2, 5, 3, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 5, 3,
                                                      2, 4, 5, 2, 5, 3, 2, 5, 3, 2, 4, 5, 2, 4, 5, 6, 7, 2, 2, 4, 5,
                                                      2, 4, 5, 6, 7, 2, 6, 7, 2, 0, 0, 0]):
        return False
    if rotate_image(image_test, math.pi/6) != (5, 5, [0, 0, 0, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 0, 5, 7,
                                                      0, 5, 7, 2, 5, 3, 2, 4, 5, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5,
                                                      6, 7, 2, 0, 5, 7, 0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2, 0, 5, 7,
                                                      2, 5, 3, 2, 4, 5, 6, 7, 2, 0, 0, 0]):
        return False

    # tests plus poussés avec la correction comme référentiel
    """
    Impossible pour moi de vérifier ces tests avec la fonction du corrigé qui ne renvoie vraisemblablement
    pas une nouvelle image suffisamment grande (voir les cas ci-dessous ou le cas suivant):
    test = corrige_filters.rotate_image(image_test, math.pi/2)
    print(test[0], test[1])
    La taille de l'image ici devrait être 5x4, mais le corrigé renvoie un 4x3 sur ma machine
    (on tourne à 90° une image de taille 4x5, donc on inverse simplement hauteur et largeur)
    Les annotations ci-dessous donnent la taille renvoyée par le corrigé vs celle renvoyée par mon programme
    """
    # if corrige_filters.rotate_image(img, math.pi/2) != rotate_image(img, math.pi/2):  # 512x511 vs 512x512
        # return False
    # if corrige_filters.rotate_image(img, math.pi/3) != rotate_image(img, math.pi/3):  # 697x697 vs 698x698
        # return False
    # return corrige_filters.rotate_image(img, math.pi/4) == rotate_image(img, math.pi/4)  # 722x722 vs 724x724
    return True


# NE PAS MODIFIER LES FONCTIONS CI-DESSOUS,
# À PART LA FONCTION main() pour tester votre programme.
# Fonctions utilitaires et programme principal


def next_token(f) -> str:
    """Lit le fichier ligne à ligne, retire les blancs et les commentaires"""
    while True:
        line = f.readline().decode()
        line = line.split("#", 1)[0]
        line = line.strip()
        if line:
            return line


def read_ppm(path: str) -> tuple:
    """
    Renvoie une image ppm sous une forme interprétable (int, int, list[int])
    :param path: le chemin pour accéder à l'image
    :return: l'image interprétable par nos fonctions
    """
    with open(path, "rb") as f:
        l1 = next_token(f)
        if l1 != "P6":
            raise Exception("Fichier invalide ligne 1")
        l2 = next_token(f).split(" ")
        w = int(l2[0])
        h = int(l2[1])
        l3 = next_token(f)
        if l3 != "255":
            raise Exception("Fichier invalide ligne 3")
        blen = w * h * 3
        data = [0] * blen
        for i in range(blen):
            data[i] = ord(f.read(1))
        return w, h, data


def write_ppm(path: str, img: tuple) -> None:
    """
    Crée dans le répertoire courant une image ppm de nom path grâce au format interprétable de img (int, int, list[int])
    :param path: le nom de la nouvelle image
    :param img: l'image interprétable à traduire en ppm
    :return: None (a créé une nouvelle image dans le répertoire courant)
    """
    with open(path, "wb") as f:
        w, h, data = img
        f.write(b"P6\n")
        f.write((str(w) + " " + str(h) + "\n").encode())
        f.write("255\n".encode())
        for c in data:
            f.write(c.to_bytes(1, 'big'))


# VOUS POUVEZ MODIFIER LA FONCTION CI-DESSOUS.


def main() -> None:
    """
    Fonction main permettant d'écrire les images dans le répertoire courant et
    de tester les fonctions de test pour les asserts et le fonctionnement
    de toutes les fonctions codées.
    Doit renvoyer dans la console "Aucun problème détecté"
    :return: None
    """
    # ecriture des images dans le répertoire courant:
    src = read_ppm("puppy.ppm")
    write_ppm("puppy_copy.ppm", copy_image(src))
    write_ppm("puppy_inv.ppm", inv_image(src))
    write_ppm("puppy_gray.ppm", gray_image(src))
    write_ppm("puppy_jail.ppm", jail_image(src, (255, 0, 0,), 10, 40))
    write_ppm("puppy_overlay.ppm", overlay_image(src, 160, 10, read_ppm("disguise.ppm"), (0, 255, 0)))
    write_ppm("puppy_scale_1.3x0.8.ppm", scale_image(src, 1.3, 0.8))
    write_ppm("puppy_scale_0.8.1.3.ppm", scale_image(src, 0.8, 1.3))
    write_ppm("puppy_scale_0.5x0.5.ppm", scale_image(src, 0.5, 0.5))
    write_ppm("puppy_scale_2x2.ppm", scale_image(src, 2, 2))
    write_ppm("puppy_mosaic.ppm", mosaic_image(src, 20))
    write_ppm("puppy_rotate.ppm", rotate_image(src, math.pi/3))

    # images utilisées pour les tests des fonctions:
    img_1 = (3, 2, [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])
    img_2 = (3, 2, [255, 255, 255, 254, 254, 254, 253, 253, 253, 252, 252, 252, 251, 251, 251, 250, 250, 250])
    img_3 = (3, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    img_4 = (3, 2, [3, 7, 8, 2, 4, 5, 6, 7, 7, 10, 10, 10, 11, 10, 10, 18, 18, 9])
    img_5 = (3, 2, [3, 7, 8, 2, 4, 5, 6, 7, 7, 1, 0, 0, 1, 10, 10, 8, 8, 9])
    img_6 = (3, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    img_7 = (4, 5, [0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2, 0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2, 0, 5, 7, 2, 5, 3, 2,
                    4, 5, 6, 7, 2, 0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2, 0, 5, 7, 2, 5, 3, 2, 4, 5, 6, 7, 2])

    # tests des asserts des fonctions (penser à enlever les lignes sous commentaire dans les fonctions):
    test_moyenne_2()
    test_read_pixel_2(src)
    test_write_pixel_2(src)
    test_jail_image_2(src)
    test_overlay_image_2(src, read_ppm("disguise.ppm"))
    test_scale_image_2(src)
    test_mosaic_image_2(src)

    # tests du bon fonctionnement des fonctions:
    somme_true = 0
    if test_moyenne_1():
        somme_true += 1
    else:
        print("Problème dans la fonction moyenne")
    if test_read_pixel_1(src, img_1):
        somme_true += 1
    else:
        print("Problème dans la fonction read_pixel")
    if test_write_pixel_1(src, img_1):
        somme_true += 1
    else:
        print("Problème dans la fonction write_pixel")
    if test_copy_image_1(src):
        somme_true += 1
    else:
        print("Problème dans la fonction copy_image")
    if test_inv_image_1(src, img_1, img_2):
        somme_true += 1
    else:
        print("Problème dans la fonction inv_image")
    if test_gray_image_1(src, img_3, img_4):
        somme_true += 1
    else:
        print("Problème dans la fonction gray_image")
    if test_jail_image_1(src, img_1, img_5):
        somme_true += 1
    else:
        print("Problème dans la fonction jail_image")
    if test_overlay_image_1(src, read_ppm("disguise.ppm"), img_6, img_5):
        somme_true += 1
    else:
        print("Problème dans la fonction overlay_image")
    if test_scale_image_1(src, img_7):
        somme_true += 1
    else:
        print("Problème dans la fonction scale_image")
    if test_mosaic_image_1(src, img_7):
        somme_true += 1
    else:
        print("Problème dans la fonction mosaic_image")
    if test_rotate_image_1(src, img_7):
        somme_true += 1
    else:
        print("Problème dans la fonction rotate_image")
    if somme_true == 11:
        return print("Aucun problème détecté")
    elif somme_true == 10:
        return print(1, "problème détecté")
    else:
        return print(11 - somme_true, 'problèmes détectés')


# main()
test_image_2 = (20, 5, [2, 45, 226, 61, 249, 224, 158, 109, 101, 150, 231, 152, 82, 137, 222, 228, 73, 248, 107, 9,
                        200, 79, 169, 244, 74, 158, 90, 15, 126, 184, 79, 176, 140, 213, 155, 179, 11, 60, 1, 181, 41,
                        152, 83, 1, 235, 71, 77, 246, 224, 6, 20, 59, 190, 66, 179, 30, 210, 120, 28, 147, 210, 243,
                        140, 88, 117, 1, 44, 182, 210, 230, 150, 26, 174, 57, 240, 221, 96, 112, 13, 201, 112, 224, 168,
                        128, 125, 202, 93, 216, 197, 225, 42, 107, 140, 225, 154, 108, 15, 26, 215, 41, 12, 247, 240,
                        26, 31, 86, 11, 199, 68, 218, 25, 75, 189, 90, 234, 52, 75, 110, 193, 243, 241, 144, 104, 36,
                        56, 23, 219, 28, 211, 60, 189, 20, 237, 227, 41, 12, 34, 126, 200, 182, 137, 167, 154, 166, 160,
                        82, 126, 169, 147, 224, 90, 130, 177, 146, 39, 224, 101, 236, 215, 15, 63, 86, 90, 209, 128,
                        195, 102, 75, 155, 165, 19, 244, 42, 229, 218, 69, 142, 78, 120, 23, 119, 148, 189, 17, 96, 166,
                        16, 153, 221, 228, 54, 243, 107, 103, 2, 79, 95, 92, 94, 230, 230, 70, 12, 83, 235, 130, 61,
                        227, 152, 106, 54, 32, 47, 46, 156, 241, 67, 130, 168, 243, 91, 143, 153, 171, 66, 139, 135, 24,
                        17, 231, 204, 174, 233, 46, 13, 148, 199, 25, 126, 236, 14, 162, 137, 88, 7, 198, 202, 117, 88,
                        250, 174, 185, 234, 199, 53, 170, 30, 100, 40, 213, 166, 105, 100, 79, 9, 133, 81, 47, 166, 169,
                        127, 181, 6, 123, 175, 74, 208, 238, 109, 82, 202, 17, 151, 34, 33, 145, 204, 92, 41, 197, 141,
                        51, 244, 173, 154, 57, 118, 88, 20, 204])
write_ppm("puppy_rotate_test.ppm", rotate_image(test_image_2, math.pi/3))
