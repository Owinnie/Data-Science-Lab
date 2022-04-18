import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15, 6))
plot_acf(y, ax=ax)
plt.xlabel(<"xLabelvalue">)
plt.ylabel(<"yLabelvalue">)
plt.title(<"yourTitle">);

# Don't delete the code below 👇
plt.savefig("images/3-5-7.png", dpi=150)
