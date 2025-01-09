def is_young(age):
  return age < 25

df['Young'] = df['Age'].apply(is_young)
young_customers = df[df['Young']]
print(young_customers)