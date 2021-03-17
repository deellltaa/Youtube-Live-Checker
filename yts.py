import requests
import time
import collections
import threading


class LiveChecker:
    """
    Editable YouTube streamer checker. Meant to be used with a discord bot.
    
    To change what streamers the script checks, simply update the self.streamer dictionary, with the channel name as
    the key, and link to their main page as a value after initializing the class as an object. Like so:

    streamer = [('Gura', 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g')]
    obj = LiveChecker()
    obj.streamers.update(streamer)

    OR

    obj = LiveChecker()
    obj.streamers['Gura'] = 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g'

    (The Name and Links must be in string form)

    To actually start getting their states though, you have to use the gettp function, and then print it out through
    the console:

    obj.gettp()
    print(obj.getRes()) # This will print out the states in an alphabetical order

    Or through a discord message:

    obj.gettp()
    await ctx.send(obj.getRes())
    """

    def __init__(self):

        self.headers = {'Accept-Encoding' : 'identity'}

        self.streamers = {} 

    def checker(self, name, link):
        live = requests.get(link, headers = self.headers)
        if '{"accessibilityData":{"label":"LIVE"}}},"style":"LIVE","icon":{"iconType":"LIVE"}' in live.text:
            states = "**LIVE**"
        else:
            states = "`Offline`"
        self.toAnswer += [f"{name}: {states}"]

        
    def gettp(self):
        self.toAnswer = []
        threads = []
        for i in self.streamers.keys():
            process = threading.Thread(target = self.checker, args = [i, self.streamers[i]])
            process.start()
            threads.append(process)

        for process in threads:
            process.join()
        print(f"STREAMER STATES: Updated ({time.strftime('%H:%M:%S', time.localtime())})")


    def getRes(self):
        """
        Prints the toAnswer list in Alphabetical Order / Numerical order
        """
        return ('\n'.join(sorted(self.toAnswer)))


if __name__ == '__main__': # Debugging
    from os import system
    system("title yts Debug")
    wl = LiveChecker()
    wl.streamers['Gura'] = 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g'
    while True:
        wl.gettp()
        print(wl.getRes())
        time.sleep(3)
