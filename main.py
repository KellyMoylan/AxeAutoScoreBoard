__author__ = 'Kelly Moylan'

import tkinter as tk

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options

from bs4 import BeautifulSoup

import re
import os

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
        self.current_left = ""
        self.current_right = ""
        self.driver = ""

        self.game_type = tk.IntVar()
        self.game_type.set(0)
        self.browser_type = tk.IntVar()
        self.browser_type.set(0)
        self.headless = tk.IntVar()
        self.headless.set(0)
        self.first_instance = True
        self.former_strings = ["","","",""]
        self.stop_program = 0

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
                       text="Chrome",
                       indicatoron=0,
                       width=20,
                       padx=20,
                       variable=self.browser_type,
                       value=0).grid(row=4, column=1, columnspan=1, pady=5)
        tk.Radiobutton(master,
                       text="Firefox",
                       indicatoron=0,
                       width=20,
                       padx=20,
                       variable=self.browser_type,
                       value=1).grid(row=5, column=1, columnspan=1, pady=5)
        tk.Radiobutton(master,
                       text="Not Headless",
                       indicatoron=0,
                       width=20,
                       padx=20,
                       variable=self.headless,
                       value=0).grid(row=4, column=3, columnspan=1, pady=5)
        tk.Radiobutton(master,
                       text="Headless",
                       indicatoron=0,
                       width=20,
                       padx=20,
                       variable=self.headless,
                       value=1).grid(row=5, column=3, columnspan=1, pady=5)
        tk.Button(master, text="Initiate Score Folder", width=60, height=2,
                  font=('ariel', 16, 'bold'),
                  command=lambda: self.initiate_score_folder()).grid(row=6, column=1, columnspan=3, pady=5)

        tk.Button(master, text="BEGIN", width=60, height=2, font=('ariel', 16, 'bold'),
                  command=lambda: self.check_for_url()).grid(row=7, column=1, columnspan=3, pady=5)

        tk.Button(master, text="END", width=60, height=2, font=('ariel', 16, 'bold'),
                  command=lambda: self.set_end()).grid(row=8, column=1, columnspan=3, pady=5)

    def set_url(self):
        pattern = re.compile("https://axescores.com/live/[0-9]*")

        if re.match(pattern, self.league_entry.get()):
            self.url = self.league_entry.get()

    def check_for_url(self):

        if self.url != "":
            if self.browser_type.get() == 0:
                ch_options = chrome_options()
                if self.headless.get() == 1:
                    ch_options.add_argument("--headless")
                try:
                    self.driver = webdriver.Chrome("chrome78/chromedriver.exe", options=ch_options)
                except:
                    try:
                        self.driver = webdriver.Chrome("chrome79/chromedriver.exe", options=ch_options)
                    except:
                        try:
                            self.driver = webdriver.Chrome("chrome80/chromedriver.exe", options=ch_options)
                        except:
                            print("NO WORKING CHROME DRIVER")
                            exit()
            else:
                ff_options = firefox_options()
                if self.headless.get() == 1:
                    ff_options.add_argument("--headless")
                try:
                    self.driver = webdriver.Firefox("firefox24/geckodriver.exe", options=ff_options)
                except:
                    try:
                        self.driver = webdriver.Firefox("firefox25/geckodriver.exe", options=ff_options)
                    except:
                        try:
                            self.driver = webdriver.Firefox("firefox26/geckodriver.exe", options=ff_options)
                        except:
                            print("NO WORKING FIREFOX DRIVER")
                            exit()
            self.driver.get(self.url)
            self.main_loop()

    def main_loop(self):
        self.initiate_score_folder()
        self.master.after(3000, lambda: self.do_everything())

    def set_end(self):
        self.stop_program = 1

    def initiate_score_folder(self):
        self.score_folder = os.getcwd() + "\score_files\\"
        if not os.path.exists(self.score_folder):
            os.mkdir(self.score_folder)

        file = open(self.score_folder + "/Left_thrower_1_name.txt", "w")
        file.write("LT1N")
        file.close()
        file = open(self.score_folder + "/Right_thrower_1_name.txt", "w")
        file.write("RT1N")
        file.close()
        file = open(self.score_folder + "/Left_thrower_2_name.txt", "w")
        file.write("LT2N")
        file.close()
        file = open(self.score_folder + "/Right_thrower_2_name.txt", "w")
        file.write("RT2N")
        file.close()

        for x in range(1, 8):
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

    def reset_files(self, side):

        file = open(self.score_folder + "/{0}_thrower_1_name.txt".format(side), "w")
        file.write("")
        file.close()
        file = open(self.score_folder + "/{0}_thrower_2_name.txt".format(side), "w")
        file.write("")
        file.close()

        for x in range(1, 8):
            file = open(self.score_folder + "/{0}_thrower_1_round_{1}.txt".format(side, x), "w")
            file.write("")
            file.close()
            file = open(self.score_folder + "/{0}_thrower_2_round_{1}.txt".format(side, x), "w")
            file.write("")
            file.close()

        file = open(self.score_folder + "/{0}_thrower_1_total.txt".format(side), "w")
        file.write("")
        file.close()
        file = open(self.score_folder + "/{0}_thrower_2_total.txt".format(side), "w")
        file.write("")
        file.close()

    def do_everything(self):

        if self.stop_program == 1:
            self.master.destroy()

        soup_level1 = BeautifulSoup(self.driver.page_source, 'lxml')
        player_info = soup_level1.find_all('div', class_="sc-iIHjhz fHaVQw")

        inprogress = []

        for x in range(0, len(player_info)):
            if "In Progress" in player_info[x].text:
                inprogress.append(x)

        if self.first_instance:
            for i in inprogress:
                self.former_strings[i] = player_info[i]
            self.first_instance = False

        for i in inprogress:
            if player_info[i] == self.former_strings[i]:
                continue
            side = player_info[i].find_all('div', class_="sc-dKEPtC gLlkqy")[0].text

            # Get player names
            names = []
            for x in player_info[i].find_all('div', class_="sc-bOCYYb jKlLxi"):
                names.append(x.text)

            # Name the key for each lane to be the two players names concat
            # Might not be the best way to do it.  Should be fine.
            name_key = names[0]+names[1]

            # Check if the names are different from the last update
            # This is to see if the game has changed so that the scores
            # files can be reset.  We only update the names once at the
            # match to save on IO calls
            if side == "Left":
                if self.current_left != name_key:
                    self.reset_files("Left")
                    self.current_left = name_key
                    for x in range(0, 2):
                        file = open(self.score_folder + "/{0}_thrower_{1}_name.txt".format(side, x + 1), "wb")
                        file.write(names[x].encode('utf8'))
                        file.close()
            if side == "Right":
                if self.current_right != name_key:
                    self.reset_files("Right")
                    self.current_right = name_key
                    for x in range(0, 2):
                        file = open(self.score_folder + "/{0}_thrower_{1}_name.txt".format(side, x + 1), "wb")
                        file.write(names[x].encode('utf8'))
                        file.close()

            # Get all the scores for the game including the total
            # We skip the first two because they will be empty spaces
            scores = []
            for x in player_info[i].find_all('div', class_="sc-ileJJU GFeXz"):
                if x.text != '\xa0':
                    scores.append(x.text)

            # Write out the total scores first because they are easy
            # They will always be in the last 2 list positions
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

        for i in inprogress:
            self.former_strings[i] = player_info[i]
        self.master.after(500, lambda: self.do_everything())

root = tk.Tk()
root.title('Axe Throwing Stream Auto Scoreboard')
MainApplication(root)
root.mainloop()