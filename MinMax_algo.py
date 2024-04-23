import random
class Node:
 def __init__(self, value=None):
     self.value = value
     self.children = []
def build_game_tree(depth, current_depth=0):
     if current_depth == len(branching_vector):
     # Atteint la profondeur maximale, assigne une valeur de gain arbitraire
            return Node(value=current_depth)
     node = Node()
     # Simule la création des nœuds enfants
     for _ in range(branching_vector[current_depth]): # Supposons que chaque nœud a deux enfants
        node.children.append(build_game_tree(branching_vector, current_depth + 1))
     return node

def assign_values(node,maximizing_player,values):
     if not node.children:
     # Si c'est une feuille, assigne une valeur de gain
        node.value = values.pop(0)
        return node.value
     if maximizing_player:
         node.value = max(assign_values(child,False , values) for child in node.children)# niveau Min
     else:
         node.value = min(assign_values(child,True, values) for child in node.children)
     # Sinon, récursivement affecte les valeurs aux enfants
     return node.value


def find_best_move(node):
    best_value = float('-inf')
    best_move = None
    for child in node.children:
        if child.value > best_value:
            best_value = child.value
    best_move = child.value
    return best_move
def display_game_tree(node, indent=0):
     print(' ' * indent + f"Value: {node.value}")
     for child in node.children:
        display_game_tree(child, indent + 4)
# Exemple d'utilisation
ranching_vector = [2, 3, 2]
# Construction de l'arbre de jeu
branching_vector = [2, 3, 2] # Vecteur de branchement prédéfini pour chaque

game_tree = build_game_tree(branching_vector)
# Affectation des valeurs de gain aux feuilles de l'arbre
values= input("Enter the number of values: ").split()
values= [int(value) for value in values ]#Convertir les entrees en enetires
assign_values(game_tree,True, values.copy())
# Affichage de l'arbre
display_game_tree(game_tree)
