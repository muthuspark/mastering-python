expected_ids = np.array([101, 102, 103, 104, 105])
observed_ids = np.array([101, 103, 105])

missing_ids = np.setdiff1d(expected_ids, observed_ids)
print(f"Missing IDs: {missing_ids}") # Output: Missing IDs: [102 104]