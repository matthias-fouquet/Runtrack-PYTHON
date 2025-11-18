def Qui_suis_je(type,saison):
    if type == "fruits" and saison == "hiver":
        return(f"{type} d'{saison} : orange, mandarine et kiwi.")
    elif type == "fruits" and saison == "été":
        return(f"{type} d'{saison} : poire, fraise et cassis.")
    elif type == "légumes" and saison == "hiver":
        return(f"{type} d'{saison} : carotte, topinambour et endive.")
    elif type == "légumes" and saison == "été":
        return(f"{type} d'{saison} : artichaut, aubergine et navet.")

print(Qui_suis_je("fruits","été"))
print(Qui_suis_je("légumes","été"))