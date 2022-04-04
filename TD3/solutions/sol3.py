# Pick the right features to encode
ONEHOT_ENC_FT = ["Famille d'emploi", "Etablissement", "Statut marital"]
ORDINAL_ENCODER = ["Niveau hiérarchique"]

onehot_encoder = OneHotEncoder(cols=ONEHOT_ENC_FT)
ordinal_encoder = OrdinalEncoder(cols=ORDINAL_ENCODER)

################
# Fit_transform
X_enc = onehot_encoder.fit_transform(X)
X_enc = ordinal_encoder.fit_transform(X_enc)

################
display(X_enc.head())
encoders = [onehot_encoder, ordinal_encoder]
