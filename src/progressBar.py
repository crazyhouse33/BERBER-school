# from :
# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console


class ProgressBar():

    def __init__(
            self, end, prefix='', suffix='', decimals=1, length=50, fill='█'):
        self.end = end
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill

    def update(self, iteration):
        """return True if the end was reached"""
        """avoiding race condition here which can lead to crash if payloadsize=0"""
        protectedEnd = self.end
        if protectedEnd == 0:
            iteration = 1
            protectedEnd = 1
        percent = ("{0:." +
                   str(self.decimals) +
                   "f}").format(100 *
                                (iteration /
                                 float(protectedEnd)))
        filledLength = int(self.length * iteration // protectedEnd)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        print(
            '\r%s |%s| %s%% %s' %
            (self.prefix,
             bar,
             percent,
             self.suffix),
            end='')
        if iteration == protectedEnd:
            return False
        return True
