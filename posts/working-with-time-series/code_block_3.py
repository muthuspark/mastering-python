decomposition = seasonal_decompose(time_series, model='additive')
decomposition.plot()
plt.show()