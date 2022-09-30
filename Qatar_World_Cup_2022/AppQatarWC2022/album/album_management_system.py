
class AlbumManagementSystem:

    def __init__(self):
        self.glued_stickers_repo = None
        self.new_stickers_repo = None
        self.album = {'countries':['Argentina' 'Brazil'],}
    def new_stickers(self):
        return self.new_stickers_repo

    def glued_stickers(self):
        return self.glued_stickers_repo

    def synchronize_stickers(self,glued_stickers,new_stickers):
        self.glued_stickers_repo = glued_stickers
        self.new_stickers_repo = new_stickers
    

