"""
UI, using Tkinter
"""
import threading
from Tkinter import *
from models import Game, State
from ab import alphabeta_search
import ttk


class Robot(threading.Thread):

    def __init__(self, app, player_move):
        super(Robot, self).__init__()
        self.app = app
        self.player_move = player_move

    def run(self):
        self.app.robot_thinking_time_label.config(text='I am thinking')
        import datetime
        _s = datetime.datetime.now()
        self.app.lock = True
        p = alphabeta_search(
            self.app.state,
            self.app.game,
            self.player_move,
            self.app.robot_level,
            self.app.progress)
        self.app.lock = False
        self.app.block[p].click()
        self.app.robot_thinking_time_label.config(text='Used: %ds' % (
            (datetime.datetime.now() - _s).seconds))


class Block():

    def click(self, event=None):
        if self.position in self.app.game.actions(self.app.state):
            self.draw(self.app.state.to_move)
            self.app.state = self.app.game.result(
                self.app.state,
                self.position)
        else:
            self.app.result_label.config(text="Cannot move!")
        if self.app.game.terminal_test(self.app.state):
            self.app.lock = True
            self.app.result_label.config(
                text='Result: ' + self.app.game.terminal_result(self.app.state))

    def vs_robot_click(self, event=None):
        if not self.app.lock:
            self.click(event)
            if self.app.state.to_move == self.app.game.robot and not self.app.lock:
                Robot(self.app, self.position).start()

    def draw(self, ox):
        if ox == 'o':
            self.canvas.create_oval(10, 10, 90, 90)
        else:
            self.canvas.create_line(10, 10, 90, 90)
            self.canvas.create_line(10, 90, 90, 10)

    def __init__(self, app, position):
        self.app = app
        self.position = position
        self.canvas = Canvas(
            self.app.master, width=100, height=100, bd=-3, bg='#eee')
        self.canvas.pack()
        self.canvas.place(x=position[1] * 100, y=position[0] * 100)
        self.canvas.bind('<1>', self.vs_robot_click)


class Application(Frame):
    block = None
    state = None
    lock = False

    def __init__(self, width=5, height=4):
        master = Tk()
        Frame.__init__(self, master)
        self.pack()
        self.width = width
        self.height = height
        self.master = master
        self.master.title('M N K %d %d %d' % (self.width, self.height, 4))
        self.master.resizable(width=FALSE, height=FALSE)
        self.master.geometry("%dx%d" %
                            (self.width * 100,
                             self.height * 100 + 100))
        self.generate_widgets()
        self.start()

    def start(self):
        self.game = Game(self.width, self.height)
        self.state = State(self.game)
        # generate the blocks
        self.block = {}
        for k in self.state.board.keys():
            self.block[k] = Block(self, k)
        self.pick_weak_robot()
        self.player_first()
        self.result_label.config(text='Playing')
        self.lock = False

    def restart(self):
        self.state.start_new()
        for k in self.block.values():
            k.canvas.delete("all")
        self.result_label.config(text='Playing')
        self.lock = False

        if self.state.to_move == 'x':
            Robot(self, None).start()

    def pick_weak_robot(self):
        self.robot_level = 1
        self.btn_w.config(state='disabled')
        self.btn_m.config(state='normal')
        self.btn_s.config(state='normal')

    def pick_mid_robot(self):
        self.robot_level = 2
        self.btn_w.config(state='normal')
        self.btn_m.config(state='disabled')
        self.btn_s.config(state='normal')

    def pick_strong_robot(self):
        self.robot_level = 3
        self.btn_w.config(state='normal')
        self.btn_m.config(state='normal')
        self.btn_s.config(state='disabled')

    def player_first(self):
        self.btn_pf.config(state='disabled')
        self.btn_rf.config(state='normal')
        self.state = State(self.game, 'o')
        self.restart()

    def robot_first(self):
        self.btn_pf.config(state='normal')
        self.btn_rf.config(state='disabled')
        self.state = State(self.game, 'x')
        self.restart()

    def generate_widgets(self):
        # generate the buttons
        self.btn_pf = Button(
            self.master, text="PlayerFirst", command=self.player_first)
        self.btn_rf = Button(
            self.master, text="RobotFirst", command=self.robot_first)
        self.btn_w = Button(
            self.master, text="Weak", command=self.pick_weak_robot)
        self.btn_m = Button(
            self.master, text="Mid", command=self.pick_mid_robot)
        self.btn_s = Button(
            self.master, text="Strong", command=self.pick_strong_robot)
        self.btn_re = Button(
            self.master, text="Restart", command=self.restart)
        self.btn_w.pack()
        self.btn_m.pack()
        self.btn_s.pack()
        self.btn_re.pack()
        self.btn_pf.pack()
        self.btn_rf.pack()
        self.btn_w.place(x=10, y=self.height * 100 + 25)
        self.btn_m.place(x=70, y=self.height * 100 + 25)
        self.btn_s.place(x=121, y=self.height * 100 + 25)
        self.btn_pf.place(x=10, y=self.height * 100 + 55)
        self.btn_rf.place(x=110, y=self.height * 100 + 55)
        self.btn_re.place(x=210, y=self.height * 100 + 55)
        # generate the progress bar
        self.progress = ttk.Progressbar(self.master,
                                        orient="horizontal",
                                        length=self.width * 100 - 20,
                                        mode="determinate")
        self.progress.pack()
        self.progress.place(x=10, y=self.height * 100 + 5)
        # generate the label
        self.robot_thinking_time_label = Label(self.master, text="Used:0s")
        self.robot_thinking_time_label.pack()
        self.robot_thinking_time_label.place(
            x=self.width * 100 - 150, y=self.height * 100 + 25)
        self.result_label = Label(self.master, text="Result")
        self.result_label.pack()
        self.result_label.place(
            x=self.width * 100 - 150, y=self.height * 100 + 55)


def main():
    app = Application(width=5, height=4)
    app.mainloop()

if __name__ == '__main__':
    main()
