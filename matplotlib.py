import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url)
data_2007 = data[data["year"] == 2007]

fig, ax = plt.subplots()

ax.scatter(x=data_2007["gdpPercap"], y=data_2007["lifeExp"], alpha=0.5)

ax.set_xscale("log")

ax.set_xlabel("GDP (USD) per capita")
ax.set_ylabel("life expectancy (years)")
