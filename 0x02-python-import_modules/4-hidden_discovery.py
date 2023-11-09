#!/usr/bin/python3
# file: 4-hidden_discovery.py
# Auth: kelechi nnadi <@alx swe>

if __name__ == '__main__':
    """ function that import module"""
    import importlib.util

    name = 'path/to/hidden_4.pyc'
    spec = importlib.util.spec_from_file_location('hidden_4', name)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    name_defined = dir(module)

    for name in sorted(names_defined):
        if not name.startswith("__"):
            print(name)
