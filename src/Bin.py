
from cement.core import controller
import pprint

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
        print("Looking up bin number: %s" % self.app.pargs.bin)

        return True
