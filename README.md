# Youtube-Live-Checker
Checks if people are live on YouTube. Is subject to change if YouTube decides to change their Live icon, since that is what the script is programmed to track. 
As of March 21 2021, however, it still works. So it's great.

The script has three main functions:
LiveChecker(), to initialize the object itself (obj = LiveChecker()),\n
gettp(), to get streamer states (obj.gettp()),\n
and getRes(), to get the states formatted into a string, usually in Alphabetical or Numerical order. (print(obj.getRes))

By default, it tracks no one. You can add YouTubers to track yourself, however, by manually changing the dictionary that the gettp() function loops through, self.streamers.

To update it:
    obj = LiveChecker()
    streamer = [('Gura', 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g')]
    obj.streamers.update(streamer)
    #OR
    streamer2 = {'Gura' : 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g'}
    obj.streamers.update(streamer2)
    #OR v2
    obj.streamers['Gura'] = 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g'
    
As you've probably noticed, the key must be a string, and the name of the channel you're tracking (or a nickname you'd refer to them as). The value MUST be a url string that
leads directly to their main channel page. If it isn't a link, the script will raise an error and stop the process. If it doesn't lead to their main page, it will keep returning
Offline.

