
import matplotlib.pyplot as plt
import torch

t1 = torch.randn(56,56)

print(t1)

plt.imshow(t1, cmap='viridis')
plt.colorbar()
plt.title('Right bone level heatmap', fontsize = 14) # title with fontsize 20
plt.xlabel('Years', fontsize = 15) # x-axis label with fontsize 15
plt.ylabel('Monthes', fontsize = 15) # y-axis label with fontsize 15
plt.show()