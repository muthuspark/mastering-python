older_than_25 = df['Age'] > 25
print(older_than_25)  # This shows the boolean mask
selected_customers = df[older_than_25]
print(selected_customers)