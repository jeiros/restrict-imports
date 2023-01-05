from importlib.abc import MetaPathFinder, Loader

restricted_modules = ['os', 'subprocess']
class RestrictedImportFinder(MetaPathFinder):

    def find_spec(self, fullname, path, target=None):
        if fullname in restricted_modules:
            # Raise an exception to prevent the import
            raise ImportError("Import of module '{}' is not allowed".format(fullname))
        else:
            # Return None to allow the import to proceed normally
            return None

class RestrictedImportLoader(Loader):
    restricted_modules = ['os', 'subprocess']

    def load_module(self, fullname):
        if fullname in restricted_modules:
            # Raise an exception to prevent the import
            raise ImportError("Import of module '{}' is not allowed".format(fullname))
        else:
            # Return None to allow the import to proceed normally
            return None
