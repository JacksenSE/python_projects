def hello():
    print("Hello, user!")


def pack(a,b,c,):
    return [a,b,c]


def eat_lunch(lunch_box):
 if len(lunch_box) == 0:
    print("starve")
 else:
    for i in range(len(lunch_box)):
     if i == 0:
        print(f"I always eat {lunch_box[0]} first")
     else:
        print(f"After that I eat {lunch_box[i]} next")


hello()
print(pack("w","o","c"))
print(pack(4,5,7))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])