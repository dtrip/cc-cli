from cement.core import controller
#from cement.utils.misc import init_defaults
from colorama import init, Fore, Back, Style

class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Credit Card Automation tool'


        #defaults = init_defaults('cc')
        #defaults['cc']['debug'] = False
        # defaults['cc']['foo'] = 'bar'

        config_defaults = {}

        arguments = [
                (['-b', '--bin'], dict(action='store', help='BIN Lookup')),
                # (['-c', '--check'], dict(action='store', help='Check card number to ensure its valid (complies with luhn algorithm)')),
                (['-v', '--verbose'], dict(action='store_true', help='Verbose Output'))
                ]

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        print(Style.BRIGHT + "Try 'cc --help' for more information" + Style.RESET_ALL)
