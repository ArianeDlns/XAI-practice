def correct_categorical_features(set_cat_features):
    output = (set_cat_features == {
              "Famille d'emploi", "Etablissement", "Parent",
              "Niveau hiérarchique",
              "Statut marital",
              "Véhicule",
              "matricule"})

    return "Well done !" if output else "Wrong categorical features selection"
