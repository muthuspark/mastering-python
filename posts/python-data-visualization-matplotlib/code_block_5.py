x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=6)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Styled Sine Wave")
plt.show()