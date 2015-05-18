def autoLineBreak(uf_string):
    """
        Function: autoLineBreak
        Parameters: uf_string - an unformatted string
        Returns a string dressed up with the <p> html tag
    """
    lines = uf_string.split('\n')
    newLines = ""
    for line in lines:
        if len(line) > 0:
            newLines += "<p>" + line + "</p>"
    return newLines