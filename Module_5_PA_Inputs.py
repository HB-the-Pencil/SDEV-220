def remove_letters(string: str, letters: tuple) -> str:
    """
    Function to remove selected letters from a string.
    :param string: String to reverse.
    :param letters: Tuple of letters to remove.
    :return: Returns the original string, minus the selected letters.
    """
    for i in set(letters):
        string = string.replace(i, "")

    return string