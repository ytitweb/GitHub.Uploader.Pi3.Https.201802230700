from database.Database import Database as Db

class Accounts:
    def __init__(self, db):
        #self.__db = Database().Accounts
        #self.__db = Db()._Database__Initializers[self.__class__.__name__].Db
        self.__db = db # dataset.connect('sqlite:///' + .../GitHub.Accounts.sqlite3) 呼出元: DatabaseMeta.__init__()

    @property
    def Db(self): return self.__db

    # --------------------
    # UserRegister.py
    # --------------------
    def Regist(self, record):
        self.__db['Accounts'].insert(record)
    def Delete(self): pass
    #def GetUserForBasic(self): pass
    #def GetUserForToken(self): pass
    #def GetUserForTwoFactor(self): pass

    # --------------------
    # Uploader.py
    # --------------------
    def GetAccount(self, username=None):
        if None is username: return self.__db['Accounts'].find().next()
        else:                return self.__db['Accounts'].find_one(Username=username)
    def GetAccounts(self):
        for account in self.__db['Accounts'].find(): yield account

