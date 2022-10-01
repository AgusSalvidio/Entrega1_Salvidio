
class AlbumManagementSystem:
      
    def __init__(self,context):
        self.context = context
        self.album = self.configure()

    @classmethod
    def working_with(cls,context):
        return cls(context = context)

    def working_context(self):
        return self.context
        
    def configure(self):
        #Primero hay que crear los AlbumPage en donde cada uno va a tener sus StickerSlots. Una vez hecho esto, recien ahi se puede instanciar el album
        pass