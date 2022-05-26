from tkinter import *
import time

class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        #self.lapstr = StringVar()
        self.e = 0
        self.m = 0
        self.makeWidgets()
        self.laps = []
        self.lapmod2 = 0
        self.today = time.strftime("%d %b %Y %H-%M-%S", time.localtime())
        
    def makeWidgets(self):                         
    """ Make the time label. """
    l1 = Label(self, text='STOPWATCH')
    l1.pack(fill=X, expand=NO, pady=1, padx=2)

    self.e = Entry(self)
    self.e.pack(pady=2, padx=2)
    
    l = Label(self, textvariable=self.timestr)
    self._setTime(self._elapsedtime)
    l.pack(fill=X, expand=NO, pady=3, padx=2)

    l2 = Label(self, text='----Laps----')
    l2.pack(fill=X, expand=NO, pady=4, padx=2)

    scrollbar = Scrollbar(self, orient=VERTICAL)
    self.m = Listbox(self,selectmode=EXTENDED, height = 5,
                     yscrollcommand=scrollbar.set)
    self.m.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=2)
    scrollbar.config(command=self.m.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
