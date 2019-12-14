# Extract Text
import os
from bs4 import BeautifulSoup

text = []
for filename in os.listdir("html"):
    html = open("html/{}".format(filename)).read()
    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.decompose()
    location = soup.title.text.split(" - ")[0]
    html = html[html.index('id="Foes"'):]
    print(location)
    # print(html)
    classes = [0]*10
    classes[0] = int(html.count("Warrior-tango-icon-20.png")/2)
    classes[1] = int(html.count("Ranger-tango-icon-20.png")/2)
    classes[2] = int(html.count("Monk-tango-icon-20.png")/2)
    classes[3] = int(html.count("Necromancer-tango-icon-20.png")/2)
    classes[4] = int(html.count("Mesmer-tango-icon-20.png")/2)
    classes[5] = int(html.count("Elementalist-tango-icon-20.png")/2)
    classes[6] = int(html.count("Assassin-tango-icon-20.png")/2)
    classes[7] = int(html.count("Ritualist-tango-icon-20.png")/2)
    classes[8] = int(html.count("Paragon-tango-icon-20.png")/2)
    classes[9] = int(html.count("Dervish-tango-icon-20.png")/2)
    physical = classes[0] + classes[1] + classes[6] + classes[8] + classes[9]
    spell_users = classes[2] + classes[3] + classes[4] + classes[5] + classes[7]
    nukers = classes[5]
    melee = classes[0] + classes[6] + classes[9]
    healers = classes[2] + classes[7]
    string = str(classes) + "\n" + \
    "physical: " + str(physical) + "\n" + \
    "spell_users: " + str(spell_users) + "\n" + \
    "healers: " + str(healers) + "\n" + \
    "melee: " + str(melee) + "\n" + \
    "nukers: " + str(nukers)
    text.append(string)
with open('../../data/processed/output.txt', 'w') as file:
    file.write("\n\n".join(text))
