import asciibars

def show_list(data: list, size: int, title: str = "Values (larger are taller)") -> None:
    """
    Shows a list horizontally, with vertical bars corresponding to the size of the number.
    """

    labels = map(str, list(range(1, size+1, 1)))
    data = list(zip(labels, data))
    asciibars.plot(data)