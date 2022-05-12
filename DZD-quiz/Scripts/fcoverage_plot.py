#Plotting the frational coverage 
import matplotlib.pyplot as plt
data = pd.read_csv('fractional_coverage.csv')
  
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
  
# Plot the data using bar() method
plt.bar(X, Y, color='m')
plt.title("Genome fractional coverage")
plt.xlabel("Sample")
plt.ylabel("Fractional coverage")
  
# Show the plot
plt.show()
plt.savefig('fcov.png')
