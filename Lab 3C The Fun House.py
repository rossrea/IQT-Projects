import re

def madlib(template):
    """
    Given a template that contains blanks like __(Noun)__,
    prompt the user to enter suggestions to fill in the blanks,
    and return the completed story as a string.
    """
    def fill_blank(match):
        while True:
            ans = input(match.group(1) + '> ')
            if ans:
                return ans
            print("Please don't leave anything blank. It kills the experience.")

    blank_re = re.compile('__\((.+?)\)__')
    blank_count = len(blank_re.findall(template))
    print("There are {} blanks in this Mad Lib.".format(blank_count))
    return blank_re.sub(fill_blank, template)

print(madlib("""On the __(Adjective)__ trip to __(Place)__, my __(Adjective)__ friend and I decided to invent a game. Since this would be a rather __(Adjective)__ trip, it would need to be a game with __(Noun, plural)__ and __(Noun, plural)__. Using our __(Noun)__ to __(Verb)__, we tried to get the __(Noun)__ next to us to play too, but they just __(Verb)__ed at us and __(Action verb)__ away. After a few rounds, we thought the game could use some __(Noun, plural)__, so we turned on the __(Noun)__ and started __(Verb that ends in "ing")__ to the __(Noun)__ that came on. This lasted for __(Measurement of time)__ before I got __(Adjective)__ and decided to __(Action verb)__. I'll never __(Verb)__ that trip, it was the __(Adjective)__ road trip of my __(Possessive noun)__."""))
