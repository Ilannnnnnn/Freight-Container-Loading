"""
Autheurs :
Baptiste Musellec <baptiste.musellec@isen-ouest.yncrea.fr>
Ilan Jaffeux-Cheniout <ilan.jaffeux--cheniout@isen-ouest.yncrea.fr>

Tous les commentaires sont rédigés par IA 
"""

import time


def create_cuboid(width, height, depth):
    """
    Crée un cuboïde.

    Args:
        width: La largeur du cuboïde.
        height: La hauteur du cuboïde.
        depth: La profondeur du cuboïde.

    Returns:
        Un dictionnaire représentant le cuboïde avec ses dimensions et son volume.
    """
    return {'width': width, 'height': height, 'depth': depth, 'volume': width * height * depth}


def create_bin(width, height, depth):
    """
    Crée un conteneur.

    Args:
        width: La largeur du conteneur.
        height: La hauteur du conteneur.
        depth: La profondeur du conteneur.

    Returns:
        Un dictionnaire représentant le conteneur avec ses dimensions, une liste des cuboïdes placés (`items`) et une liste des espaces libres restants (`free_spaces`).
    """
    return {'width': width, 'height': height, 'depth': depth, 'items': [], 'free_spaces': [(0, 0, 0, width, height, depth)]}


def can_fit(free_space, cuboid):
    """
    Vérifie si un cuboïde peut tenir dans un espace libre.

    Args:
        free_space: Un tuple représentant l'espace libre (x, y, z, largeur, hauteur, profondeur).
        cuboid: Un dictionnaire représentant le cuboïde avec ses dimensions.

    Returns:
        True si le cuboïde peut tenir dans l'espace libre, False sinon.
    """
    return (cuboid['width'] <= free_space[3] and
            cuboid['height'] <= free_space[4] and
            cuboid['depth'] <= free_space[5])


def subtract_space(free_space, cuboid, position):
    """
    Calcule les nouveaux espaces libres après avoir placé un cuboïde.

    Args:
        free_space: Un tuple représentant l'espace libre initial (x, y, z, largeur, hauteur, profondeur).
        cuboid: Un dictionnaire représentant le cuboïde placé.
        position: Un tuple représentant la position (x, y, z) du cuboïde dans l'espace libre.

    Returns:
        Une liste de tuples représentant les nouveaux espaces libres créés.
    """
    new_spaces = []
    (fx, fy, fz, fw, fh, fd) = free_space
    (px, py, pz) = position
    cw, ch, cd = cuboid['width'], cuboid['height'], cuboid['depth']

    # Generate new free spaces by cutting the free space along the dimensions of the placed cuboid
    if px + cw < fx + fw:  # Right
        new_spaces.append((px + cw, fy, fz, fx + fw - (px + cw), fh, fd))
    if py + ch < fy + fh:  # Above
        new_spaces.append((fx, py + ch, fz, fw, fy + fh - (py + ch), fd))
    if pz + cd < fz + fd:  # In front
        new_spaces.append((fx, fy, pz + cd, fw, fh, fz + fd - (pz + cd)))

    return new_spaces


def add_to_bin(bin, cuboid):
    """
    Essaie d'ajouter un cuboïde à un conteneur.

    Args:
        bin: Un dictionnaire représentant le conteneur.
        cuboid: Un dictionnaire représentant le cuboïde à ajouter.

    Returns:
        True si le cuboïde a été ajouté avec succès, False sinon.
    """
    for i, free_space in enumerate(bin['free_spaces']):
        if can_fit(free_space, cuboid):
            position = (free_space[0], free_space[1], free_space[2])
            bin['items'].append((cuboid, position))
            new_free_spaces = subtract_space(free_space, cuboid, position)
            bin['free_spaces'].pop(i)
            bin['free_spaces'].extend(new_free_spaces)
            return True
    return False


def rotate_cuboid(cuboid):
    """
    Génère toutes les rotations possibles d'un cuboïde.

    Args:
        cuboid: Un dictionnaire représentant le cuboïde à tourner.

    Returns:
        Une liste de dictionnaires représentant toutes les rotations possibles du cuboïde.
    """
    return [
        create_cuboid(cuboid['width'], cuboid['height'], cuboid['depth']),
        create_cuboid(cuboid['width'], cuboid['depth'], cuboid['height']),
        create_cuboid(cuboid['height'], cuboid['width'], cuboid['depth']),
        create_cuboid(cuboid['height'], cuboid['depth'], cuboid['width']),
        create_cuboid(cuboid['depth'], cuboid['width'], cuboid['height']),
        create_cuboid(cuboid['depth'], cuboid['height'], cuboid['width'])
    ]


def bin_packing_3d(bin_width, bin_height, bin_depth, cuboids):
    """
    Effectue l'emballage 3D de cuboïdes dans des conteneurs.

    Args:
        bin_width: La largeur des conteneurs.
        bin_height: La hauteur des conteneurs.
        bin_depth: La profondeur des conteneurs.
        cuboids: Une liste de dictionnaires représentant les cuboïdes à placer.

    Returns:
        Une liste de conteneurs avec les cuboïdes placés.
    """
    # Sort cuboids by volume (largest to smallest)
    #cuboids = sorted(cuboids, key=lambda c: c['volume'], reverse=True)

    bins = []
    for cuboid in cuboids:
        placed = False
        for bin in bins:
            for rotated_cuboid in rotate_cuboid(cuboid):
                if add_to_bin(bin, rotated_cuboid):
                    placed = True
                    break
            if placed:
                break
        if not placed:
            new_bin = create_bin(bin_width, bin_height, bin_depth)
            for rotated_cuboid in rotate_cuboid(cuboid):
                if add_to_bin(new_bin, rotated_cuboid):
                    bins.append(new_bin)
                    placed = True
                    break
            if not placed:
                raise ValueError("Cuboid too large to fit in a new bin.")
    return bins




def print_bins(bins):
    for i, bin in enumerate(bins):
        print(f"Bin {i+1}:")
        for item, position in bin['items']:
            print(f"  Cuboid({item['width']}, {item['height']}, {item['depth']}) at position {position}")
        print()


def main():
    marchandises = [
        ('Tubes acier', 10, 1, 0.5),
        ('Tubes acier', 9, 2, 0.7),
        ('Tubes acier', 7.5, 1.2, 0.4),
        ('Acide chlorhydrique', 1, 1, 1),
        ('Godet pelleteuse', 2, 2, 1),
        ('Rails', 11, 1, 0.2),
        ('Tubes PVC', 3, 2, 0.6),
        ('Echaffaudage', 3, 1.3, 1.8),
        ('Verre', 3, 2.1, 0.6),
        ('Ciment', 4, 1, 0.5),
        ('Bois vrac', 5, 0.8, 1),
        ('Troncs chênes', 6, 1.9, 1),
        ('Troncs hêtres', 7, 1.6, 1.5),
        ('Pompe à chaleur', 5, 1.1, 2.3),
        ('Cuivre', 6, 2, 1.4),
        ('Zinc', 5, 0.8, 0.8),
        ('Papier', 4, 1.6, 0.6),
        ('Carton', 7, 1, 1.3),
        ('Verre blanc vrac', 9, 0.9, 2.2),
        ('Verre brun vrac', 3, 1.6, 0.9),
        ('Briques rouges', 5, 1.1, 2.4),
        ('Pièces métalliques', 6, 1.6, 1.4),
        ('Pièces métalliques', 7, 0.9, 1.2),
        ('Pièces métalliques', 3, 1.6, 1.9),
        ('Ardoises', 1, 1.8, 1),
        ('Tuiles', 2, 1.2, 2.3),
        ('Vitraux', 4, 0.7, 1.2),
        ('Carrelage', 6, 1.2, 2.5),
        ('Tôles', 7, 0.6, 1.5),
        ('Tôles', 9, 1.7, 1),
        ('Tôles', 6, 1.9, 1.6),
        ('Tôles', 3, 2.2, 2.2),
        ('Tôles', 3, 0.5, 2.2),
        ('Mobilier urbain', 4, 0.7, 1.9),
        ('Lin', 5, 2.2, 0.7),
        ('Textiles à recycler', 6, 1.3, 2.5),
        ('Aluminium', 6, 1.3, 1.2),
        ('Batteries automobile', 7, 1.4, 2.5),
        ('Quincaillerie', 6, 1.1, 1),
        ('Treuil', 7, 0.9, 1.3),
        ('Treuil', 8, 0.5, 0.5),
        ('Acier', 8, 0.9, 1.7),
        ('Laine de bois', 8, 0.9, 1.8),
        ('Ouate de cellusose', 5, 1.7, 1.2),
        ('Chanvre isolation', 2.2, 1.6, 1.1),
        ('Moteur électrique', 4.2, 1.5, 0.8),
        ('Semi conducteurs', 5.3, 2.1, 1.1),
        ('Tuiles terre cuite', 3, 0.6, 1.2),
        ('Aluminium', 6, 1, 0.8),
        ('Aluminium', 5, 1.3, 0.6),
        ('Aluminium', 4, 2.1, 2.1),
        ('Aluminium', 6, 1.5, 1.9),
        ('Aluminium', 4, 0.8, 2.1),
        ('Aluminium', 2, 2, 2.3),
        ('Aluminium', 4, 1, 1.1),
        ('Aluminium', 6, 1.8, 1.1),
        ('Lithium', 6, 1.9, 0.9),
        ('Lithium', 3, 2, 2.2),
        ('Lithium', 4, 1.5, 0.9),
        ('Lithium', 4, 2.1, 2.5),
        ('Lithium', 2, 1.2, 1.5),
        ('Lithium', 6, 1.3, 2),
        ('Lithium', 2, 0.8, 1.1),
        ('Contreplaqué', 4, 1.4, 2),
        ('Contreplaqué', 5, 0.6, 0.5),
        ('Contreplaqué', 5, 0.6, 1.8),
        ('Contreplaqué', 4, 0.7, 1.4),
        ('Contreplaqué', 6, 0.5, 0.7),
        ('Contreplaqué', 3, 1.5, 1.8),
        ('Contreplaqué', 3, 1.4, 2),
        ('Contreplaqué', 3, 2, 2.3),
        ('Contreplaqué', 5, 1.5, 0.7),
        ('Contreplaqué', 5, 2.2, 0.5),
        ('Contreplaqué', 6, 1.2, 1.2),
        ('Poutre', 5, 0.8, 0.7),
        ('Poutre', 3, 0.5, 1.9),
        ('Poutre', 5, 1.4, 0.7),
        ('Poutre', 6, 0.7, 0.7),
        ('Poutre', 6, 1.2, 2),
        ('Poutre', 3, 1.7, 1.1),
        ('Poutre', 5, 1.6, 2.1),
        ('Pneus', 3, 1.3, 1.7),
        ('Pneus', 4, 1.5, 1.7),
        ('Pneus', 3, 1.5, 1.9),
        ('Pneus', 3, 0.6, 1.9),
        ('Pneus', 5, 1.8, 0.5),
        ('Pneus', 3, 1.8, 0.7),
        ('Pneus', 4, 1.7, 1.4),
        ('Pneus', 4, 1.5, 0.5),
        ('Pneus', 2, 2.1, 1.8),
        ('Pneus', 2, 0.7, 1.1),
        ('Pneus', 6, 1.2, 1.3),
    ]

    cuboids = [create_cuboid(m[1], m[2], m[3]) for m in marchandises]
    start_time = time.time()
    bins = bin_packing_3d(11.583, 2.294, 2.569, cuboids)  # Example bin dimensions (width, height, depth)
    end_time = time.time()
    print_bins(bins)
    print(f"Execution time: {end_time - start_time} seconds")


main()