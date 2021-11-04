
def generator():
    for i in range(0,3):
        yield i*i # i*i is never stored it is jsut passed back to the for loop to be printed and the func isnt restarted it is resumed

myGen = generator()
for i in myGen:
    print(i)

