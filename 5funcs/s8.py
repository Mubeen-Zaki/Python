def dictFunc(**kwargs):
    for k,v in kwargs.items():
        print(f"{type(k)} {type(v)}")
        print(k,":",v)

dictFunc(name="khabib", enemy="conor")
dictFunc(power="striking")