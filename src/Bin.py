
from cement.core import controller
from tabulate import tabulate
from pprint import pprint
from colorama import init, Fore, Back, Style

import requests
import json

class Bin(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'Bin'
        description = 'Search Credit card Bank Identifacation Number'
        stacked_on = 'base'

    def default(self):
        pass


    @controller.expose(help='Lookup BIN Number')
    def bin(self):

        if (self.app.pargs.verbose):
            print("Looking up bin number: %s" % self.app.pargs.bin)

        d = self.__getBinData(self.app.pargs.bin)
        self.__printTable(d)

        return True

    # outputs bin data to cmd line
    def __printTable(self, d):

        a = []

        for k,v in d.items():
            a.append([k, v])

        print(Style.BRIGHT + "\nIssuer information" + Style.RESET_ALL + "\n")
        print tabulate(a, ['Attribute', 'Value'], tablefmt="simple")
        print("\n")

        return True

    # makes HTTP GET request to binlist.net REST api
    # to get credit card bin data in JSON format
    #
    # @return string - JSON bin data
    def __getBinData(self, b):
        url = "http://www.binlist.net/json/" + b

        if (self.app.pargs.verbose):
            print("Pulling Bin data from: %s" % url)

        r = requests.get(url)

        if (self.app.pargs.verbose):
            print("Response Status code %s" % r.status_code)

        #print(tabulate(r.json()))

        return r.json()
