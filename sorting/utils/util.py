import asciibars

def show_list(data: list, size: int, labels: list = None, title: str = "Values (larger are taller)") -> None:
    """
    Shows a list horizontally, with vertical bars corresponding to the size of the number.
    """

    if labels:
        data = list(zip(labels, data))
    else:
        generated_labels = map(str, list(range(1, size+1, 1)))
        data = list(zip(generated_labels, data))

    print(f"{title.capitalize()}\n")
    # data = list(zip(labels, data))
    asciibars.plot(data)