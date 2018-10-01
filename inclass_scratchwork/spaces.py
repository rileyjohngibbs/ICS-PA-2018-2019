# Good morning! The whitespace is all whack in this program.
# How can we clean it up? Which whitespaces will cause problems if we don't?

def some_function( x,y,   z):
    first_sum= x+y
        second_sum  = y +  z
    return first_sum*second_sum

a,b, c =2, 5,   8
    total = some_function( a,b,c )
print ( total )