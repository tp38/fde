#!/home/th/Code/Python/FdE/bin/python3
from datetime import datetime, date

from DayResultDaoSqlite import DayResultDaoSqlite
from InDialog import InDialog
from bcolors import bcolors

class DayResult:
    def __init__(self, dao, day):
        self.day = day
        self.dao = dao
        # yy, ww, dd = self.day.isocalendar()
        # if ( dd == 6 ) | ( dd == 7 ) :
        #     self.ca = 0
        #     self.hours = 0.0
        #     self.hsup = 0.0
        #     self.comment = 'Non travaillé'
        #     self.new = True
        # else :
        d = self.dao.read_data( day )
        if d is None :
            self.ca = 0
            self.hours = 0.0
            self.hsup = 0.0
            self.comment = None
            self.new = True
        else :
            self.ca = int( d[1] )
            self.hours = float( d[2] )
            self.hsup = d[3]
            self.comment = d[4]
            self.new = False

    def get_date(self) :
        return self.day.split('-')

    def get_ca(self) :
        return self.ca

    def get_hours(self) :
        return self.hours

    def get_hsup(self) :
        return self.hsup

    def get_comment(self) :
        return self.comment

    def set_ca(self) :
        end = False
        while not end :
            val = input( f"\tEntrer le chiffre d'affaire ({self.ca}) : " )
            try :
                self.ca = int( val )
                end = True
            except ValueError :
                print( f"\tWrong ca format. Must be an integer\nPlease retry ..." )

    def set_time(self) :
        end = False
        while not end :
            val = input( f"\tEntrer le nombre d'heure ({self.hours}) : " )
            try :
                self.hours = float( val )
                end = True
            except ValueError :
                print( f"\tWrong hours format. Must be a double\nPlease retry ..." )

    def set_hsup(self) :
        end = False
        while not end :
            val = input( f"\tEntrer le nombre d'heure sup ({self.hsup}) : " )
            try :
                self.hsup = float( val )
                end = True
            except ValueError :
                print( f"\tWrong hours format. Must be a double\nPlease retry ..." )

    def set_comment(self) :
        val = input( f"\tEntrer un commentaire éventuel ({self.comment}): " )
        self.comment = None if len( val ) == 0 else val

    def display_new(self):
        color = bcolors.FAIL if self.new else bcolors.OKGREEN
        print( f"{color}( {self.day} : {self.ca:>4} / {self.hours:>3.2} ({self.hsup:>3.2}) [{'' if self.comment is None else self.comment}] ){bcolors.ENDC}" )

    def display_ca(self):
        color = bcolors.FAIL if self.ca < (self.hours * 25) else bcolors.OKGREEN
        if self.comment == 'Non travaillé' :
            print( f"( {self.day} : {self.ca:>4} / {self.hours:>3.2} ({self.hsup:>3.2}) = {self.ca/self.hours:>3.1f}€/h [{'' if self.comment is None else self.comment}] )" )
        else :
            print( f"{color}( {self.day} : {self.ca:>4} / {self.hours:>3.2} ({self.hsup:>3.2}) = {self.ca/self.hours:>3.1f}€/h [{'' if self.comment is None else self.comment}] ){bcolors.ENDC}" )

    def save(self) :
        if self.new :
            self.dao.create_data( (self.day, self.ca, self.hours, self.hsup, self.comment ) )
            self.new = False
        else :
            self.dao.update_data( (self.day, self.ca, self.hours, self.hsup, self.comment, self.day) )

    def delete(self) :
        self.dao.destroy_data( self.day )
        self.ca = 0
        self.hours = 0.0
        self.comment = None
        self.new = True

    def xml(self, dec) :
        s = ""
        s = s + dec + "<DayResult>\n"
        s = s + dec + f"\t<Date>{self.day}</Date>\n"
        s = s + dec + f"\t<Hours>{self.hours}</Hours>\n"
        s = s + dec + f"\t<Ca>{self.ca}</Ca>\n"
        s = s + dec + f"\t<HSup>{self.hsup}</HSup>\n"
        s = s + dec + f"\t<Average>{self.ca/self.hours:.2f}</Average>\n"
        s = s + dec + f"\t<Comment>{'' if self.comment is None else self.comment}</Comment>\n"
        s = s + dec + "</DayResult>\n"
        return  s

if __name__ == "__main__" :
    dao = DayResultDaoSqlite()
    dao.create_connection(r"fildeclair.sq3")

    diag = InDialog()
    day = diag.getDate()

    r = DayResult( dao, day )
    r.display_new()
    end = False
    while not end :
        val = input( "Voulez-vous modifier [m] / sauvegarder [s] / supprimer [d] cet enregistrement ou quitter [q] ? ")

        if val == "m" :
            r.set_ca()
            r.set_time()
            r.set_hsup()
            r.set_comment()
        elif val == "s" :
            r.save()
        elif val == "d" :
            r.delete()
        elif val == "q" :
            end = True
        else :
            print( "nothing to do ... " )
            print( r.xml() )
        if not end :
            r.display_new()
    dao.close()
