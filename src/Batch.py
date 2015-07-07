
from cement.core import controller

class Batch(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'Batch'
        description = 'Batch CSV of bins'
        stacked_on = 'base'


    @controller.expose(help='Batch CSV file of BIN numbers')
    def csv(self):
        print("Batching...")
        return True

