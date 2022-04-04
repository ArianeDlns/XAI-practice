test_size = 0.2
random_state = 420
matricules = X_enc["matricule"].unique()

# TO COMPLETE
mat_train, mat_test = train_test_split(
    matricules, test_size=test_size, random_state=random_state)
idx_mat_train = X_enc[X_enc["matricule"].isin(mat_train)].index
idx_mat_test = X_enc[X_enc["matricule"].isin(mat_test)].index

X_train = X_enc.loc[idx_mat_train].reset_index(drop=True)
X_test = X_enc.loc[idx_mat_test].reset_index(drop=True)

Y_train = Y[idx_mat_train]
Y_test = Y[idx_mat_test]

# Assert distribution is the same

_, dist_init = np.unique(Y, return_counts=True)
_, dist_train = np.unique(Y_train, return_counts=True)
_, dist_test = np.unique(Y_test, return_counts=True)

print("Label distribution in the global dataset :", dist_init[1]/dist_init[0])
print("Label distribution in the train dataset :", dist_train[1]/dist_train[0])
print("Label distribution in the test dataset :", dist_test[1]/dist_test[0])
