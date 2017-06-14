
from cement.core import controller
from tabulate import tabulate
from pprint import pprint
from colorama import init, Fore, Back, Style

import requests
import json
import cards

class Bin(controller.CementBaseController):

    cards = cards.cards()

    class Meta:
        interface = controller.IController
        label = 'Bin'
        description = 'Search Credit card Bank Identification Number'
        stacked_on = 'base'

    def default(self):
        pass


    @controller.expose(help='Lookup BIN Number')
    def bin(self):

        # if card number is 15 or 16 digits, will verify it passes luh algorithm check
        if len(self.app.pargs.bin) == 15 or len(self.app.pargs.bin) == 16:
            lpass = self.cards.luhn(self.app.pargs.bin)

            if lpass == True:
                print("%s[+] Card number passed luhn algorithm check%s" % (Style.BRIGHT, Style.RESET_ALL))
            else:
                print("%s%s[!] Card does NOT pass luhn algorithm check!%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL))


        self.app.pargs.bin = self.cards.getBin(self.app.pargs.bin)

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

        print("%s[+] Issuer information\n%s" % (Style.BRIGHT,Style.RESET_ALL))
        print tabulate(a, ['Attribute', 'Value'], tablefmt="simple")
        print("\n")

        return True

    # makes HTTP GET request to binlist.net REST api
    # to get credit card bin data in JSON format
    #
    # @return string - JSON bin data
    def __getBinData(self, b):
        # url = "http://www.binlist.net/json/" + b
        url = "https://bins.payout.com/api/v1/bins/" + b

        if (self.app.pargs.verbose):
            print("Pulling Bin data from: %s" % url)

        r = requests.get(url)

        if (self.app.pargs.verbose):
            print("Response Status code %s" % r.status_code)

        #print(tabulate(r.json()))

        return r.json()
