import mysql.connector
import os


"""purpose of this tool is to take a backup of databases using the selected number"""
"""code by Prudhvi Mutluri"""


def sql_logic():
    conn = mysql.connector.connect(user="", password="", port="3306", host="")  """Enter the User,Hostname and Password"""
    cursor = conn.cursor()
    cursor.execute("show databases;")
    d = (cursor.fetchall())
    dic = dict(enumerate(d))
    print(dic)
    a = int(input("Please select one of the above :     "))
    b = str(dic[a])
    bad_chars = [';', ':', '!', "*", ",", "'", "(", ")"]
    final_db = ''.join((filter(lambda i: i not in bad_chars, b)))
    print(final_db)
    db_par = " --single-transaction --hex-blob --set-gtid-purged=OFF --dump-date --master-data=2"
    space = os.popen(" du -sh /var/mysql/ ")
    file_name = str(input("Please enter the file name /var/mysql/_____.sql:    "))
    os.system('mysqldump' + db_par + '--databases ' + final_db + ' > /var/mysql/' + file_name + '.sql')
    print("Database backup is done")
    dump_file = os.system("du -sh" + " /var/mysql/" + file_name + ".sql")


sql_logic()





