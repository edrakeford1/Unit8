"""
8-3
T-Shirt
Write a function called make_shirt() that accepts a size and the text of a message that should be printed
on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguements to make a shirt. Call the function a second time using keyword arguements. 
"""

def make_shirt(size, message):
    """Make a shirt with a size and a message"""
    print(f"A shirt of size {size.upper()} will have the folliwng message printed on it: \n{message}\n")

make_shirt('xl', 'hang in there')
make_shirt('l', 'need a coffee')
