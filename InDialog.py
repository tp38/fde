from datetime import datetime, date



class InDialog() :
    def __init__(self) :
        pass

    def getDate(self):
        end = False
        while not end :
            val = input( "Entrer la date concernée : " )
            try :
                day = datetime.strptime( val, '%d/%m/%Y').date()
                end = True
            except ValueError :
                print( f"Wrong date format. Must be '%d/%m/%Y'\nPlease retry ..." )

        return day
