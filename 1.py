from os import getenv
print(getenv("MY_NAME", "aviel"))
a = "hello world"
b = 4
isMarried = False

e = ("moshe", 43, False)
d = ["aviel", 31, True]
f = {"name": "aviel", "age": 31, "isMarried": True,
     "hobbies": ["ski", "guitar"], "work": {"position": "devops", "salary": "2M"}}
print(a)
print(b)
d[1] = 32
print(d[1])
print(e[2])
print(f.values())

g = "aviel"
h = "buskila"
i = g + " " + h
j = 4
k = g + str(j)
lm = f"{g} {str(h)}"
print(lm)
# define lk
lk = "%s %s" % (g, h)
lt = "aviel\n\t \"buskila\""
print(lt)

if j == 4:
    print("a is 4")
print("aviel")
