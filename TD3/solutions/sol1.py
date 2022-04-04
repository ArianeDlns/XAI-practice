# FOR YOU TO ANSWER

# How many different employees are gathered in this dataset ?
n_employees = X["matricule"].nunique()
print("Number of different employees in the dataset :", n_employees)

# How many employees did resignate within the next six months in the dataset ?
_, Y_distribution = np.unique(Y, return_counts=True)
print("Number of resignated employees :", Y_distribution[1])
print("Proportion of resignated employees in the dataset :",
      Y_distribution[1]/Y_distribution[0])

# Consider a random employee who decided to resignate. Take a look at his evolution in the company from his
# hiring until his resignation
idx_resignate = np.where(Y == 1)[0]
rand_idx = np.random.choice(idx_resignate, size=1)[0]
resignated_employee = X.iloc[rand_idx]["matricule"]

evolution_employee = X[X["matricule"] == resignated_employee]

display(evolution_employee)
