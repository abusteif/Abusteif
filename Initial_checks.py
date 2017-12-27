import pip
import imp

class Initial_check:

    def __init__(self):
        return

    def check_modules(self):
        modules_list = ["requests",
                        "json",
                        "time",
                        "datetime",
                        "MySQLdb",
                        "collections",
                        "BeautifulSoup"]
        print "Checking modules"
        for module in modules_list:
            try:
                imp.find_module(module)
                print module + " already installed"
            except ImportError as e:
                print module + " not found. Installing using pip"
                pip.main(['install', module])

    def load_Base_tables(self):
        from classes import DATABASE_DETAILS, Database
