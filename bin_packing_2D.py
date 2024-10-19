"""
Autheur :
Ilan Jaffeux-Cheniout <ilan.jaffeux--cheniout@isen-ouest.yncrea.fr>

Tous les commentaires sont rédigés par IA 
"""
import time 
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
    ('Semi conducteurs', 3.7, 0.9, 1.4),
    ('Semi conducteurs', 5.6, 0.5, 1.4),
    ('Semi conducteurs', 4.9, 0.9, 2.5),
    ('Semi conducteurs', 8.7, 1.3, 1.3),
    ('Semi conducteurs', 6.1, 2.2, 2.3),
    ('Semi conducteurs', 3.3, 1.8, 2.3),
    ('Semi conducteurs', 2.6, 1.6, 2.3),
    ('Semi conducteurs', 2.9, 1.6, 2),
    ('Aluminium', 2, 1.1, 0.6),
    ('Aluminium', 3, 0.6, 1.2),
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
def create_rectangle(length, width):
    """
    Crée un rectangle.

    Args:
        width: La largeur du rectangle.
        length: La longueur du rectangle.

    Returns:
        Un dictionnaire représentant le rectangle avec les clés 'width' et 'height'.
    """
    return {'length': length, 'width': width}



def create_bin(length, width):
    """
    Crée un conteneur (bin).

    Args:
        width: La largeur du conteneur.
        length: La longueur du conteneur.

    Returns:
        Un dictionnaire représentant le conteneur avec les clés 'width', 'height', 'items' (liste des rectangles placés) et 'free_spaces' (liste des espaces libres restants).
    """
    return {'length': length, 'width': width, 'items': [], 'free_spaces': [(0, 0, length, width)]}



def can_fit(free_space, rectangle):
    """
    Vérifie si un rectangle peut tenir dans un espace libre.

    Args:
        free_space: Un tuple représentant l'espace libre (x, y, longueur, largeur).
        rectangle: Un dictionnaire représentant le rectangle avec les clés 'width' et 'height'.

    Returns:
        True si le rectangle peut tenir dans l'espace libre, False sinon.
    """
    return rectangle['length'] <= free_space[2] and rectangle['width'] <= free_space[3]

def subtract_space(free_space, rectangle, position):
    """
    Calcule les nouveaux espaces libres après avoir placé un rectangle.

    Args:
        free_space: Un tuple représentant l'espace libre initial (x, y, longueur, largeur).
        rectangle: Un dictionnaire représentant le rectangle avec les clés 'length' et 'width'.
        position: Un tuple représentant la position (x, y) du rectangle dans l'espace libre.

    Returns:
        Une liste de tuples représentant les nouveaux espaces libres.
    """
    new_spaces = []
    x, y, free_length, free_width = free_space
    rect_x, rect_y = position
    rect_l, rect_h = rectangle['length'], rectangle['width']

    # Diviser l'espace libre en nouveaux espaces en fonction du rectangle placé
    if rect_x + rect_l < x + free_length:
        new_spaces.append((rect_x + rect_l, y, x + free_length - (rect_x + rect_l), free_width))  # Espace à droite
    if rect_y + rect_h < y + free_width:
        new_spaces.append((x, rect_y + rect_h, free_length, y + free_width - (rect_y + rect_h)))  # Espace en haut
    
    return new_spaces

def add_to_bin(bin, rectangle, container_length, container_width):
    """
    Essaie d'ajouter un rectangle à un conteneur.

    Args:
        bin: Un dictionnaire représentant le conteneur.
        rectangle: Un dictionnaire représentant le rectangle à ajouter.
        container_length: La longueur du conteneur.
        container_width: La largeur du conteneur.

    Returns:
        True si le rectangle a été ajouté avec succès, False sinon.
    """
    #rectangles.sort(key=lambda c: c['length'] * c['width'] , reverse=True)
    for i, free_space in enumerate(bin['free_spaces']):
        if can_fit(free_space, rectangle):
            # Calcul des coordonnées du rectangle dans le conteneur
            x, y, _, _ = free_space

            # Vérification des bords du conteneur
            if x + rectangle['length'] > container_length or y + rectangle['width'] > container_width:
                continue

            bin['items'].append((rectangle, (x, y)))

            # Mettre à jour les espaces libres (en utilisant subtract_space)
            new_free_spaces = subtract_space(free_space, rectangle, (x, y))
            bin['free_spaces'].pop(i)
            bin['free_spaces'].extend(new_free_spaces)
            return True
    return False



def rotate_rectangle(rectangle):
    """
    Tourne un rectangle de 90 degrés.

    Args:
        rectangle: Un dictionnaire représentant le rectangle à tourner.

    Returns:
        Un nouveau dictionnaire représentant le rectangle tourné.
    """
    return create_rectangle(rectangle['width'], rectangle['length'])


def bin_packing_2d(bin_length, bin_width, rectangles, container_length, container_width):
    """
    Effectue le bin packing 2D.

    Args:
        bin_length: La largeur des sous espaces.
        bin_width: La hauteur des conteneurs.
        rectangles: Une liste de dictionnaires représentant les rectangles à placer.
        container_length: La longueur du conteneur global.
        container_width: La largeur du conteneur global.

    Returns:
        Une liste de conteneurs avec les rectangles placés.
    """
    bins = []
    for rectangle in rectangles:
        placed = False
        for bin in bins:
            if add_to_bin(bin, rectangle, container_length, container_width) or add_to_bin(bin, rotate_rectangle(rectangle), container_length, container_width):
                placed = True
                break
        if not placed:
            new_bin = create_bin(bin_length, bin_width)
            if not add_to_bin(new_bin, rectangle, container_length, container_width) and not add_to_bin(new_bin, rotate_rectangle(rectangle), container_length, container_width):
                raise ValueError("Rectangle too large to fit in a new bin.")
            bins.append(new_bin)
    return bins

def print_bins(bins, container_length, container_width):
    """
    Affiche le contenu des conteneurs.

    Args:
        bins: Une liste de conteneurs.
        container_width: La largeur du conteneur global.
        container_height: La hauteur du conteneur global.
    """
    for i, bin in enumerate(bins):
        fits = all(
            item[0]['length'] + item[1][0] <= container_length and item[0]['width'] + item[1][1] <= container_width
            for item in bin['items']
        )
        print(f"Bin {i+1}: {'[OK]' if fits else '[NE RENTRE PAS]'}")
        for item, position in bin['items']:
            print(f"  Rectangle({item['length']}, {item['width']}) at position {position}")


rectangles = [create_rectangle(m[1], m[2]) for m in marchandises]
start_time = time.time()
bins = bin_packing_2d(11.583, 2.294, rectangles, 11.583, 2.294)  # Ajout des dimensions du conteneur
end_time = time.time()
print_bins(bins, 11.583, 2.294) 
print(f"Temps d'exécution: {end_time - start_time} secondes")