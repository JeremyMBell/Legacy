def autoLineBreak(uf_string):
    """
        Function: autoLineBreak
        Parameters: uf_string - an unformatted string
        Returns a string dressed up with the <p> html tag
    """
    print "breaking up the lines!"
    lines = uf_string.split('\n')
    newLines = ""
    for line in lines:
        newLines += "<p>" + line + "</p>"
    print newLines
    return newLines