from html import escape

user_input = input("Enter text: ")
safe_html = escape(user_input)  # Escapes special characters like <, >, &, ", '
print(f"<p>{safe_html}</p>")