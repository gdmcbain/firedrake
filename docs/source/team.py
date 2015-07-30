# coding=utf-8
from collections import OrderedDict

team = OrderedDict([
    ("David Ham", "http://www.imperial.ac.uk/people/david.ham"),
    ("Paul Kelly", "http://www.imperial.ac.uk/people/p.kelly"),
    ("Florian Rathgeber",
     "https://kynan.github.io"),
    ("Lawrence Mitchell",
     "http://www.imperial.ac.uk/people/lawrence.mitchell"),
    ("Fabio Luporini", "http://www.imperial.ac.uk/people/f.luporini12"),
    ("Doru Bercea", "http://www.imperial.ac.uk/people/gheorghe-teodor.bercea08"),
    ("Miklós Homolya", "http://www.imperial.ac.uk/people/m.homolya14"),
    ("Graham Markall", "http://www.doc.ic.ac.uk/~grm08/"),
    ("Andrew McRae", "http://www.imperial.ac.uk/people/a.mcrae12"),
    ("Michael Lange", "http://www.imperial.ac.uk/people/michael.lange"),
    ("Simon Funke", "http://www.simonfunke.com"),
    ("Colin Cotter", "http://www.imperial.ac.uk/people/colin.cotter")
])

cols = 4
colwidth = "23%"

coldashes = max(map(len, team.keys())) + 5


def separator(n):
    out.write(("-" * coldashes).join("+" * (n + 1)) + "\n")


def blank(n):
    out.write((" " * coldashes).join("|" * (n + 1)) + "\n")

out = file("teamgrid.rst", "w")

out.write("..\n  This file is generated by team.py. DO NOT EDIT DIRECTLY\n")


images = []
names = []

def imagename(name):
    puny = name.split()[0].lower().decode("utf-8").encode("punycode")
    return puny[:-1] if puny[-1]=="-" else puny 

# Write substitution rules for member images.
for member, url in team.iteritems():
    out.write(".. |" + member + "| image:: /images/" +
              imagename(member) + ".*\n")
    out.write("   :width: 70%\n")
    out.write("   :target: %s\n" % url)
    out.write(".. _" + member + ": " + url + "\n")

    im = " |" + member + "|"
    images.append(im + " " * (coldashes - len(im.decode("utf-8"))))
    nm = " `" + member + "`_"
    names.append(nm + " " * (coldashes - len(nm.decode("utf-8"))))

out.write("\n\n")
separator(cols)

members = iter(zip(images, names))

try:
    while True:
        irow = "|"
        nrow = "|"
        for c in range(cols):
            image, name = members.next()
            irow += image + "|"
            nrow += name + "|"

        out.write(irow + "\n")
        blank(cols)
        out.write(nrow + "\n")

        separator(cols)

except StopIteration:

    if c > 0:
        # Finish the final row.
        for rest in range(c, cols):
            irow += " " * coldashes + "|"
            nrow += " " * coldashes + "|"

        out.write(irow + "\n")
        blank(cols)
        out.write(nrow + "\n")

        separator(cols)
