#!/home/th/Code/Python/FdE/bin/python3
import sys

from datetime import datetime, date

from MonthResultDaoSqlite import MonthResultDaoSqlite
from DayResultDaoSqlite import DayResultDaoSqlite
from DayResult import DayResult
from bcolors import bcolors

class MonthResult:
    def __init__(self, mdao, rdao, year, month, seuil):
        self.mdao = mdao
        # self.rdao = rdao
        self.year = f"{year}" if isinstance( year, int) else year
        self.month = f"{month:02}" if isinstance( month, int ) else month
        self.seuil = f"{seuil}" if isinstance(seuil, float ) else seuil
        self.dresults = []

        days = self.mdao.get_days( self.year, self.month )
        for d in days :
            day = datetime.strptime( d, '%Y-%m-%d').date()
            r = DayResult(rdao, day)
            self.dresults.append( r )

    def display_summary(self) :
        prime = self.mdao.get_prime( self.year, self.month, self.seuil )
        ca = self.mdao.get_ca( self.year, self.month )
        hours = self.mdao.get_hours( self.year, self.month )
        hsup = self.mdao.get_hsup( self.year, self.month )

        color = bcolors.FAIL if prime < 0.0 else bcolors.OKGREEN
        print( f"{color}{self.year}-{self.month} : {ca}€ / {hours}h ({hsup}) [prime : {prime:.2f}]{bcolors.ENDC}" )

    def get_average(self) :
        ca = self.mdao.get_ca( self.year, self.month )
        hours = self.mdao.get_hours( self.year, self.month )
        return ca/hours

    def display_detail(self) :
        for r in self.dresults :
            print( f"\t", end='' )
            r.display_ca()

    def xml(self) :
        ca = self.mdao.get_ca( self.year, self.month )
        hours = self.mdao.get_hours( self.year, self.month )
        prime = self.mdao.get_prime( self.year, self.month, self.seuil )
        hsup = self.mdao.get_hsup( self.year, self.month )

        s = f"<MonthResult>\n"
        s = s + f"\t<Year>{self.year}</Year>\n"
        s = s + f"\t<Month>{self.month}</Month>\n"
        s = s + f"\t<Ca>{ca}</Ca>\n"
        s = s + f"\t<Hours>{hours}</Hours>\n"
        s = s + f"\t<HSup>{hsup}</HSup>\n"
        s = s + f"\t<Delta>{prime:.2f}</Delta>\n"
        s = s + f"\t<Prime>{ca * 0.02 if prime >= 0 else 0:.2f}</Prime>\n"
        s = s + "\t<Results>\n"
        for r in self.dresults :
            s = s + r.xml( '\t\t')
        s = s + "\t</Results>\n"
        s = s + '</MonthResult>\n'
        return s

if __name__ == "__main__" :
    day = date.today()
    if len(sys.argv) >= 2 :
        argv=sys.argv[1:]
        kwargs={kw[0]:kw[1] for kw in [ar.split('=') for ar in argv if ar.find('=')>0]}
        args=[arg for arg in argv if arg.find('=')<0]

        try:
            d = kwargs['date']
            day = datetime.strptime( d, '%d/%m/%Y').date()
        except ValueError :
            print( f"Wrong date format. Must be '%d/%m/%Y'\nUsing current date ..." )
        except KeyError :
            print( f"Using current date ..." )

    mdao = MonthResultDaoSqlite()
    mdao.create_connection(r"fildeclair.sq3")
    rdao = DayResultDaoSqlite()
    rdao.create_connection(r"fildeclair.sq3")

    mresult = MonthResult( mdao, rdao, day.year, day.month, 3421.15  )
    mresult.display_summary()
    mresult.display_detail()

    # with open( "report.xml", "w" ) as f :
    #     f.write( "<?xml version='1.0' encoding='UTF-8'?>\n" )
    #     f.write( "<?xml-stylesheet type='text/xsl' href='html_report.xsl'?>\n" )
    #     f.write( mresult.xml() )
