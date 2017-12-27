import imp

modules_list = ["requests",
                "json",
                "time",
                "datetime",
                "MySQLdb",
                "collections"]

for module in modules_list:
    imp.find_module(module)