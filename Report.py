#!/home/th/Code/Python/FdE/bin/python3
from datetime import datetime, date
from paramiko import SSHClient
from scp import SCPClient
import matplotlib.pyplot as plt
import subprocess
import json


from MonthResult import MonthResult
from MonthResultDaoSqlite import MonthResultDaoSqlite
from DayResultDaoSqlite import DayResultDaoSqlite
from DayResult import DayResult
from config.py import SERVER, S_PATH, LOGIN, PASSWORD


def scp():
    with SSHClient() as ssh:
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect("ip", username="username", password="password")
        ssh.load_system_host_keys()
        ssh.connect( SERVER, username=LOGIN, password=PASSWORD )

        with SCPClient(ssh.get_transport()) as scp:
            scp.put('out/report.xml', remote_path=S_PATH)
            scp.put('out/html_report.xsl', remote_path=S_PATH)
            scp.put('out/style.css', remote_path=S_PATH)
            scp.put('out/suivi_results.png', remote_path=S_PATH)

def draw_results_chart(lmr):
    x = []
    y = []
    fig, ax = plt.subplots()
    for r in lmr :
        x.append( f"{r.year}-{r.month}" )
        y.append( r.get_average() )

    rects = ax.bar( x, y )

    ax.set_ylabel( 'Euros €')
    for bars in ax.containers :
        ax.bar_label(bars, padding=3)
    ax.set_title( f"moyenne €/h par mois" )

    fig.tight_layout()
    # plt.show()
    plt.savefig( "out/suivi_results.png" )
    plt.close()

if __name__ == "__main__" :
    try:
        with open('in/period.json') as json_file:
            periods = json.load(json_file)
    except FileNotFoundError :
        periods = { 2022 : [11, 12, ], 2023 : [1, 2, 3, 4,5] }
        with open('in/period.json' , 'w') as json_file:
            json.dump(periods, json_file)
    lmr = []
    day = date.today()

    mdao = MonthResultDaoSqlite()
    mdao.create_connection(r"fildeclair.sq3")
    rdao = DayResultDaoSqlite()
    rdao.create_connection(r"fildeclair.sq3")

    for y in periods :
        for m in periods[y] :
            mresult = MonthResult( mdao, rdao, y, m, 3421.15  )
            lmr.append( mresult )

    # lmr[-1].display_summary()
    # lmr[-1].display_detail()

    draw_results_chart(lmr)

    with open( "out/report.xml", "w" ) as f :
        f.write( "<?xml version='1.0' encoding='UTF-8'?>\n" )
        f.write( "<?xml-stylesheet type='text/xsl' href='html_report.xsl'?>\n" )
        f.write( lmr[-1].xml() )

    scp()

    # print( "launching report viewer." )
    # subprocess.Popen(['/usr/bin/epiphany', f"https://{SERVER}/fildeclair/report.xml" ])
