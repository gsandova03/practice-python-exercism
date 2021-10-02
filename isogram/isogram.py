def is_isogram(string):
    lower_string = string.lower()
    clean_string = [ c for c in lower_string if c.isalpha() ]
    return ( len( list(clean_string) ) == len( set( clean_string ) ) )

