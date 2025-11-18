def Qui_suis_je(langage):
    if langage == "JavaScript":
        return "Tu es un développeur web."
    elif langage == "Python":
        return "Tu es un développeur IA."
    elif langage == "Java":
        return "Tu es un développeur logiciel."
    elif langage == "ReactJS":
        return "Tu es un développeur mobile."
    else :
        return "Un jour, je serai le meilleur développeur…"

print(Qui_suis_je("JavaScript"), end="\n \n")
print(Qui_suis_je("Python"), end="\n \n")
print(Qui_suis_je("Java"), end="\n \n")
print(Qui_suis_je("ReactJS"), end="\n \n")
print(Qui_suis_je("CSS"), end="\n \n")