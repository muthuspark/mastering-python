selected_cols = df[[col for col in df.columns if col.startswith('col')]]
print("\nBoolean indexing:\n", selected_cols)