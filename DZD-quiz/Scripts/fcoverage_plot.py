#Plotting the frational coverage 
import matplotlib.pyplot as plt
y=df['coverage']
x=df['sample']
  
# Plot the data using bar() method
plt.bar(x, y, color='m')
plt.title("Genome fractional coverage")
plt.xlabel("Sample")
plt.ylabel("Fractional coverage")
  
# Show the plot
plt.show()
plt.savefig('fcov.png')
