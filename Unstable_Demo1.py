import matplotlib.pyplot as plt
def main():
    print("This is program illustrating chaos example:")
    x = input("Enter a number between 0 and 1:")

    for i in range(10000):
        x=float(x)
        y=3.9*x*(1.0-x)
        print(y)
        plt.plot(i,y, '.', color = 'k', markersize = 2)
        x=y
    plt.show()

main()
