__author__ = 'Kelly'

import tkinter as tk
from selenium import webdriver

from bs4 import BeautifulSoup

import re
import os
import time

bgcolour = "white"

url = ""
score_folder = ""
stop_program = -1
driver = ""


class MainApplication:

    def __init__(self, master):
        self.master = master
        self.url = ""
        self.league_entry = ""
        self.score_folder = ""
        self.game_type = tk.IntVar()
        self.game_type.set(0)
        self.stop_program = -1
        self.driver = ""
        self.current_left = ""
        self.current_right = ""

        master.configure(background=bgcolour)
        league_label = tk.LabelFrame(master, bg=bgcolour, width=1000, text="League URL", relief=tk.GROOVE,
                                     font=("ariel", 16, "bold"))
        league_label.grid(row=2, column=1, columnspan=3, padx=50)
        self.league_entry = tk.Entry(league_label, width=40, font=('ariel', 10, 'bold'), relief=tk.SUNKEN,
                                     borderwidth=3)
        tk.Button(
            league_label, text="Set", command=lambda: self.set_url()).grid(row=2, column=3, sticky=tk.W, padx=(0, 100))

        self.league_entry.grid(row=2, column=2, sticky=tk.E, padx=(100, 0))

        tk.Radiobutton(master,
                       text="League",
                       indicatoron=0,
                       width=20,
                       padx=20,
                       variable=self.game_type,
                       value=0).grid(row=4, column=1, columnspan=3, pady=5)
        tk.Radiobutton(master,
                       text="Playoffs",
                       indicatoron=0,
                       width=20,
                       padx=20,
                       variable=self.game_type,
                       value=1).grid(row=5, column=1, columnspan=3, pady=5)

        tk.Button(master, text="Initiate Score Folder", width=60, height=2,
                  font=('ariel', 16, 'bold'),
                  command=lambda: self.initiate_score_folder()).grid(row=6, column=1, columnspan=1, pady=5)

        tk.Button(master, text="BEGIN", width=60, height=2, font=('ariel', 16, 'bold'),
                  command=lambda: self.check_for_url()).grid(row=7, column=1, columnspan=3, pady=5)

        tk.Button(master, text="END", width=60, height=2, font=('ariel', 16, 'bold'),
                  command=lambda: self.set_end()).grid(row=8, column=1, columnspan=3, pady=5)

    def set_url(self):
        pattern = re.compile("https://axescores.com/live/[0-9]*")

        if re.match(pattern, self.league_entry.get()):
            self.url = self.league_entry.get()

    def check_for_url(self, count=0):
        # if self.url != "":
        #     self.driver = webdriver.Chrome()
        #     self.driver.get("https://axescores.com/live")
        if self.stop_program != 1:
            self.do_everything()
            print(count)
            self.master.after(10000, lambda: self.check_for_url(count+1))
        else:
            self.master.destroy()

    def set_end(self):
        self.stop_program *= -1

    def initiate_score_folder(self):
        self.score_folder = os.getcwd() + "\score_files\\"
        if not os.path.exists(self.score_folder):
            os.mkdir(self.score_folder)

        file = open(self.score_folder + "/Left_thrower_1_name.txt", "w")
        file.write("LT1")
        file.close()
        file = open(self.score_folder + "/Right_thrower_1_name.txt", "w")
        file.write("LT2")
        file.close()
        file = open(self.score_folder + "/Left_thrower_2_name.txt", "w")
        file.write("RT1")
        file.close()
        file = open(self.score_folder + "/Right_thrower_2_name.txt", "w")
        file.write("RT2")
        file.close()

        if self.game_type.get() == 0:
            for x in range(1,4):
                file = open(self.score_folder + "/Right_thrower_1_round_{0}.txt".format(x), "w")
                file.write("RT1R{0}".format(x))
                file.close()
                file = open(self.score_folder + "/Right_thrower_2_round_{0}.txt".format(x), "w")
                file.write("RT2R{0}".format(x))
                file.close()
                file = open(self.score_folder + "/Left_thrower_1_round_{0}.txt".format(x), "w")
                file.write("LT1R{0}".format(x))
                file.close()
                file = open(self.score_folder + "/Left_thrower_2_round_{0}.txt".format(x), "w")
                file.write("LT2R{0}".format(x))
                file.close()
        else:
            for x in range(1,8):
                file = open(self.score_folder + "/Right_thrower_1_round_{0}.txt".format(x), "w")
                file.write("RT1R{0}".format(x))
                file.close()
                file = open(self.score_folder + "/Right_thrower_2_round_{0}.txt".format(x), "w")
                file.write("RT2R{0}".format(x))
                file.close()
                file = open(self.score_folder + "/Left_thrower_1_round_{0}.txt".format(x), "w")
                file.write("LT1R{0}".format(x))
                file.close()
                file = open(self.score_folder + "/Left_thrower_2_round_{0}.txt".format(x), "w")
                file.write("LT2R{0}".format(x))
                file.close()
        file = open(self.score_folder + "/Right_thrower_1_total.txt", "w")
        file.write("RT1T")
        file.close()
        file = open(self.score_folder + "/Right_thrower_2_total.txt", "w")
        file.write("RT2T")
        file.close()
        file = open(self.score_folder + "/Left_thrower_1_total.txt", "w")
        file.write("LT1T")
        file.close()
        file = open(self.score_folder + "/Left_thrower_2_total.txt", "w")
        file.write("LT2T")
        file.close()

    def reset_files(self):
        file = open(self.score_folder + "/Left_thrower_1_name.txt", "w")
        file.write("")
        file.close()
        file = open(self.score_folder + "/Right_thrower_1_name.txt", "w")
        file.write("")
        file.close()
        file = open(self.score_folder + "/Left_thrower_2_name.txt", "w")
        file.write("")
        file.close()
        file = open(self.score_folder + "/Right_thrower_2_name.txt", "w")
        file.write("")
        file.close()

        if self.game_type.get() == 0:
            for x in range(1, 4):
                file = open(self.score_folder + "/Right_thrower_1_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
                file = open(self.score_folder + "/Right_thrower_2_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
                file = open(self.score_folder + "/Left_thrower_1_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
                file = open(self.score_folder + "/Left_thrower_2_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
        else:
            for x in range(1, 8):
                file = open(self.score_folder + "/Right_thrower_1_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
                file = open(self.score_folder + "/Right_thrower_2_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
                file = open(self.score_folder + "/Left_thrower_1_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
                file = open(self.score_folder + "/Left_thrower_2_round_{0}.txt".format(x), "w")
                file.write("")
                file.close()
            file = open(self.score_folder + "/Right_thrower_1_total.txt", "w")
            file.write("")
            file.close()
            file = open(self.score_folder + "/Right_thrower_2_total.txt", "w")
            file.write("")
            file.close()
            file = open(self.score_folder + "/Left_thrower_1_total.txt", "w")
            file.write("")
            file.close()
            file = open(self.score_folder + "/Left_thrower_2_total.txt", "w")
            file.write("")
            file.close()

    def do_everything(self):

        driver.get(url)
        soup_level1=BeautifulSoup(driver.page_source, 'lxml')
        player_info = soup_level1.find_all('div', class_="sc-iIHjhz fHaVQw")

        inprogress = []
        for x in range(0, len(player_info)):
            if "In Progress" in player_info[x].text:
                inprogress.append(x)
        for i in inprogress:

            side = player_info[i].find_all('div', class_="sc-dKEPtC gLlkqy")[0].text

            # Write out player names
            names = []
            for x in player_info[i].find_all('div', class_="sc-bOCYYb jKlLxi"):
                names.append(x.text)

            name_key = names[0]+names[1]

            if side == "Left":
                if self.current_left != name_key:
                    self.reset_files()
                    self.current_left = name_key
            if side == "Right":
                if self.current_right != name_key:
                    self.reset_files()
                    self.current_right = name_key

            for x in range(0,2):
                file = open(self.score_folder + "/{0}_thrower_{1}_name.txt".format(side,x+1), "w")
                file.write(names[x])
                file.close()

            # Get all the scores for the game including the total
            scores = []
            for x in player_info[i].find_all('div', class_="sc-ileJJU GFeXz"):
                if x.text != '\xa0':
                    scores.append(x.text)

            # Write out the total scores first because they are easy
            file = open(self.score_folder + "/{0}_thrower_1_total.txt".format(side), "w")
            file.write(scores[len(scores)-2])
            file.close()
            file = open(self.score_folder + "/{0}_thrower_2_total.txt".format(side), "w")
            file.write(scores[len(scores) - 1])
            file.close()

            # Write out the scores for each round.  Do thrower 1 and 2 at the same time to
            # make it easier.  Could probably make this more efficient by only changing the
            # current round.
            round = 1
            for x in range(0, len(scores)-2, 2):
                file = open(self.score_folder + "/{0}_thrower_1_round_{1}.txt".format(side, round), "w")
                file.write(scores[x])
                file.close()
                file = open(self.score_folder + "/{0}_thrower_2_round_{1}.txt".format(side, round), "w")
                file.write(scores[x+1])
                file.close()
                round += 1


root = tk.Tk()
root.title('Axe Throwing Stream Auto Scoreboard')
MainApplication(root)
root.mainloop()