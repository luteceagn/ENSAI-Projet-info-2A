class Playlist:
    """Une playlist composée de musiques
    ---------
    Attributs
    ---------
    theme : string
        le thème de la playlist donné par l'utilisateur
    musiques : list
        Liste des musiques présentes dans la playlist
    nb_musique : int
        Nombre de musiques dans la playlist
    """

    def __init__(self, theme, musiques, nb_musique):
        """Constructeur"""
        self.theme = theme
        self.musiques = musiques
        self.nb_musique = nb_musique

    def add_song(self, playlist, musique: int):
        if musique == 0 or musique < 0:
            return ValueError("Le numéro de la musique doit être strictement positif.")
        musiques = musiques.pop(musique-1)
        return musiques
    
    def add_song(self,playlist, musique:int):
        if musique == 0 or musique < 0:
            return ValueError("Le numéro de la musique doit être strictement positif.")
        playlist +=
        #ajouter la musique demandée à la playlist
