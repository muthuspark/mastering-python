def make_sandwich(*ingredients):
    """Makes a sandwich with the given ingredients."""
    print("\nMaking a sandwich with:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('bread', 'cheese', 'tomato', 'lettuce')
make_sandwich('bread', 'ham')