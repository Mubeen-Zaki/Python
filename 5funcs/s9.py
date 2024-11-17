# def even_numbers(limit):
#     for i in range(2,limit + 1,2):
#         print(i)

# even_numbers(11)

def even_generators(limit):
    for i in range(2, limit + 1, 2):
        yield i

for i in even_generators(10):
    print(i)