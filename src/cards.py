
class cards:
    def __init__(self):
        pass

    """ checks to make sure that the card passes a luhn mod-10 checksum """
    """ Thanks To: http://code.activestate.com/recipes/172845-python-luhn-checksum-for-credit-card-validation/ """
    def cardLuhnChecksumIsValid(card_number):

        sum = 0
        num_digits = len(card_number)
        oddeven = num_digits & 1

        for count in range(0, num_digits):
            digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

        return ( (sum % 10) == 0 )


    # gets bin number of a card
    def getBin (self, card_number):

        binNumber = 0

        if not str(card_number).isdigit():
            raise Exception("Credit card numbers do not contain letters")

        # returns card_number if already 6 digits - assumes bin is being passed
        if len(card_number) == 6:
            return card_number

        if len(card_number) < 15 or len(card_number) > 16:
            raise Exception("This is not a credit card number")

        binNumber = str(card_number)[:6]

        return binNumber


