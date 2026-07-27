import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualize(data, generator, title, size):
    fig, ax = plt.subplots()

    bars = ax.bar(range(len(data)), data)

    ax.set_title(title)
    ax.set_xlim(0, size)
    ax.set_ylim(0, int(size*1.1))

    def update(arr):
        for bar, val in zip(bars, arr):
            bar.set_height(val)

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=generator,
        interval=50,
        repeat=False
    )

    plt.show()
