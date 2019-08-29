__author__ = 'Kelly'

from tkinter import filedialog
from tkinter import *
# from selenium import webdriver
#
# from bs4 import BeautifulSoup

import re
import os
import time

bgcolour = "white"

class application(Tk):


    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent

        self.url = ""
        self.league_entry = ""
        self.score_folder = ""
        self.game_type = IntVar()
        self.game_type.set(0)

        self.resizable(width=False, height=False)
        self.configure(background=bgcolour)
        self.initialize_ui()
        self.initiate_score_folder()


    def initialize_ui(self):
        league_label = LabelFrame(self, bg=bgcolour, width=1000, text="League URL", relief=GROOVE,
                                          font=("ariel", 16, "bold"))
        league_label.grid(row=2, column=1, columnspan=3, padx=50)

        self.league_entry = Entry(league_label, width=40, font=('ariel', 10, 'bold'), relief=SUNKEN,
                                borderwidth=3)
        league_button = Button(
            league_label, text="Set", command=lambda: self.set_url())

        self.league_entry.grid(row=2, column=2, sticky=E, padx=(100, 0))
        league_button.grid(row=2, column=3, sticky=W, padx=(0, 100))

        Radiobutton(self.parent,
                    text="League",
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=self.game_type,
                    command=self.showChoice,
                    value=0).grid(row=5, column=1, columnspan=3, pady=5)
        Radiobutton(self.parent,
                    text="Playoffs",
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=self.game_type,
                    command=self.showChoice,
                    value=1).grid(row=6, column=1, columnspan=3, pady=5)

        start_button = Button(self, text="BEGIN", width=60, height=2, font=('ariel', 16, 'bold'))
        start_button.grid(row=7, column=1, columnspan=3, pady=5)


    def set_url(self):
        self.url = self.league_entry.get()

        pattern = re.compile("https://axescores.com/live/[0-9]*")

        if re.match(pattern, self.league_entry.get()):
            self.url = self.league_entry.get()


    def initiate_score_folder(self):
        self.score_folder = os.getcwd() + "\score_files\\"
        if not os.path.exists(self.score_folder):
            os.mkdir(self.score_folder)

        file = open(self.score_folder + "/left_thrower_1_name.txt", "w")
        file.write("LT1")
        file.close()
        file = open(self.score_folder + "/right_thrower_1_name.txt", "w")
        file.write("LT2")
        file.close()
        file = open(self.score_folder + "/left_thrower_2_name.txt", "w")
        file.write("RT1")
        file.close()
        file = open(self.score_folder + "/right_thrower_2_name.txt", "w")
        file.write("RT2")
        file.close()

        if self.game_type == 0:

        else:


    def do_everything():
        for iteration in range(0,20):
            driver.get(url)
            time.sleep(10)
            soup_level1=BeautifulSoup(driver.page_source, 'lxml')
            player_info = soup_level1.find_all('div', class_="sc-iIHjhz fHaVQw")
            inprogress = []
            for x in range(0, len(player_info)):
                if "In Progress" in player_info[x].text:
                    inprogress.append(x)
            for i in inprogress:
                side = player_info[i].find_all('div', class_="sc-dKEPtC gLlkqy")[0].text

                names = []
                for x in player_info[i].find_all('div', class_="sc-bOCYYb jKlLxi"):
                    names.append(x.text)

                scores = []
                for x in player_info[i].find_all('div', class_="sc-ileJJU GFeXz"):
                    if x.text != '\xa0':
                        scores.append(x.text)
                print(side)
                print(names[0])
                for x in range(1,int((len(scores)/2))):
                    print(x, end= "\t")
                print("Total")
                for x in range(0,len(scores)-2,2):
                    print(scores[x], end="\t")
                print(scores[len(scores)-2])
                print("")

                for x in range(1,len(scores)-2,2):
                    print(scores[x], end="\t")
                print(scores[len(scores)-1])
                print(names[1])


if __name__ == "__main__":
    app = application(None)
    app.title('Axe Throwing Stream Auto Scoreboard')
    app.mainloop()