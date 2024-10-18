import importlib

def dynamic_import(module_name):
    module = importlib.import_module(module_name)
    return module

# Na przykład, dynamicznie importujemy moduł os
os_module = dynamic_import('os')

# Teraz możemy używać os_module, tak jakbyśmy go normalnie zaimportowali
print(os_module.getcwd())
