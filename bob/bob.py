def response( frace ):

    frace_clean = frace.strip()

    if (frace_clean.isupper()) :
        return "Whoa, chill out!"
    elif (frace_clean.endswith('?')) :
        return "Sure."
    elif ( not frace_clean ) :
        return "Fine. Be that way!"
    elif ( frace_clean.isupper() and frace_clean.endswith('?')) :
        return "Calm down, I know what I'm doing!"
    else: 
        return "Whatever."