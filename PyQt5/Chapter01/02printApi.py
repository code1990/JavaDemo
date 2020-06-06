import sys

from PyQt5.QtWidgets import QWidget

out = sys.stdout

sys.out=open(r"F:\github\PyQt\PyQt5\Chapter01\\api.txt","w")

help(QWidget)

sys.stdout.close()

sys.stdout=out

