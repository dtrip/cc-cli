
from cement.core import foundation, handler
from colorama import Fore, Back, Style

import baseController
import Bin
import Batch

class App:
    def init(self):
        pass

    def run(self):

        try:

            app = foundation.CementApp('CC')

            handler.register(baseController.baseController)
            handler.register(Bin.Bin)
            handler.register(Batch.Batch)

            app.setup()
            # print('\n' + Style.BRIGHT + Back.BLUE + '\nCredit Card Analyzer\n' + Style.RESET_ALL + '\n')

            # app.args.add_argument('-b', '--bin', action='store', metavar='000000', help='Lookup BIN number')

            app.run()

        except Exception as e:
            print("Error: %s" % str(e))
        finally:
            app.close()
