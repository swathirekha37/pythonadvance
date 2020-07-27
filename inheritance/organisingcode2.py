from organisingcode1 import House,Office
from house import Home

class Corporate(Home,House,Office):
    def corpmsg(self):
        return "This is a corporate world!!!"