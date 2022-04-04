# 1. Do the parents tend to resignate more in the input dataset ?
# HINT : Use sns.histplot for categorical features

x, y = 'Parent', 'demission'

plt.figure(figsize=(10, 6))
sns.set_theme()
sns.histplot(data=df, hue=y, x=x, fill=True)

# In general, parents tend to be more stable and stay in the company.

# 2. How many months after their last promotion are the employees the most likely to leave the company
# according to the input data ?

x, y = 'Dernière promotion (mois)', 'demission'

plt.figure(figsize=(10, 6))
sns.set_theme()
sns.kdeplot(data=df.groupby(x)[y].value_counts(
    normalize=True).mul(100), x=x, hue=y, fill=True)

# The highest resignation rate is estimated between 10 and 15 months without a new promotion.
