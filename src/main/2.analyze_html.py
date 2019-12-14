# Extract Text
import os
from shutil import copyfile
from bs4 import BeautifulSoup

# Copy manually extracted html files
for filename in os.listdir("manual_html"):
    copyfile("manual_html/{}".format(filename), "html/{}".format(filename))

# Read all html files
text = []
for filename in os.listdir("html"):
    html = open("html/{}".format(filename)).read()
    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.decompose()
    location = soup.title.text.split(" - ")[0]
    print(location)
    try:
        html = html[html.index('id="Foes"'):]
    except:
        continue
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
    string = location + "\n" + \
    "W: " + str(classes[0]) + "  R: " + str(classes[1]) + "  Mo:" + str(classes[2]) + "\n" + \
    "N: " + str(classes[3]) + "  Me:" + str(classes[4]) + "  E: " + str(classes[5]) + "\n" + \
    "A: " + str(classes[6]) + "  Ri:" + str(classes[7]) + "  P: " + str(classes[8]) + "  D: " + str(classes[9]) + "\n" + \
    "physical: " + str(physical) + "\n" + \
    "spell_users: " + str(spell_users) + "\n" + \
    "healers: " + str(healers) + "\n" + \
    "melee: " + str(melee) + "\n" + \
    "nukers: " + str(nukers)
    text.append(string)
with open('../../data/processed/output.txt', 'w') as file:
    file.write("\n\n".join(text))
