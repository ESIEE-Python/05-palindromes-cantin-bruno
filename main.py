import translate

#### Fonction secondaire


def ispalindrome(p):
    
    p = p.translate(str.maketrans('', '', '0123456789àéè¤ôâêûäöë!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    p = ''.join(c.lower() for c in p if c.isalpha())
    return p == p[::-1]

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(f"({s}, {ispalindrome(s)})")


if __name__ == "__main__":
    main()