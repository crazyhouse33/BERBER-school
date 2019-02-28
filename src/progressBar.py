#from : https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
class ProgressBar():

    def __init__(self, end, prefix='', suffix='', decimals = 1, length = 50, fill = '█'):
        self.end=end
        self.prefix=prefix
        self.suffix=suffix
        self.decimals=decimals
        self.length=length
        self.fill=fill

    def update(self, iteration ):
        """return True if the end was reached"""
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (iteration / float(self.end)))
        filledLength = int(self.length * iteration // self.end)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        print('\r%s |%s| %s%% %s' % (self.prefix, bar, percent, self.suffix), end = '')

        if iteration == self.end: 
            return False
        return True
