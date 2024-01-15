import plotext as plt

def show_list(data: list) -> None:
    """
    Shows a list horizontally, with vertical bars corresponding to the
    size of the number.
    """

    plt.bar(data)
    plt.title("Most Favored Pizzas in the World")
    plt.show()