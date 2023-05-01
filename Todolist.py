"""to do list en python
I) demander à l'utilisateur les taches a faire et montrer leurs statues.
II) afficher une to do liste
III) demander a l'utilisateur les taches qui sont terminer

1- verifier à l'infini que les taches sont terminées
2-readme pour ce projet
3-readme de l'autre projet
4-reviser les dictionnaires
"""


def print_to_do_list(dictionnaire_todolist):
  print("--------------------Liste à faire--------------------")
  for tache in dictionnaire_todolist.keys():
    if dictionnaire_todolist[tache] == "oui":
      print("[x]", tache)
    else:
      print("[ ]", tache)


def to_do_list_projet():
  to_do_list = {}
  while True:
    print("Quel est ta tache a faire?")
    tache = input()
    print("Est ce que ta tache est terminer ou non?")
    status = input()
    to_do_list[tache] = status
    print("veux tu ajouter des taches?")
    reponse = input()
    if reponse == "non":
      print_to_do_list(to_do_list)
      break

  print("Quellles sont les taches qui sont terminer?")
  tache_finie = input()
  if tache_finie in to_do_list:
    to_do_list[tache_finie] = "oui"
    print_to_do_list(to_do_list)


to_do_list_projet()