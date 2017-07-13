def hello():
    import subprocess
    output = subprocess.check_output("c:\python27\getipadd.py '192.168.2.0/24'")
    form = SQLFORM(db.vminventory)
    return locals()
