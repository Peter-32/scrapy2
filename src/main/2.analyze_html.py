# Extract Text
# text = []
# for filename in os.listdir("html"):
#     html = open("html/{}".format(filename)).read()
#     soup = BeautifulSoup(html)
#     for script in soup(["script", "style"]):
#         script.decompose()
#     text.append(soup.get_text())
# with open('../../data/processed/text.txt', 'w') as file:
#     file.write(" ".join(text))
