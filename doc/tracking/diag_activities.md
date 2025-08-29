# Diagramme d'activité
stateDiagram-v0
[*]--> Accueil
Accueil --> Se connecter
Accueil --> Créer un compte
Accueil --> Quitter
Se connecter --> Créer une playlist
Se connecter --> Voir sa playlist
Se connecter --> Se déconnecter 
Créer une playlist --> Sauvegarder la Playlist
Créer une playlist --> Modifier la Playlist
Modifier la Playlist --> Sauvegarder la Playlist
Sauvegarder la Playlist --> [*]

> Ce diagramme UML d'activité modélise le flux de travail d'un processus, il montre la séquence d'activités et de décisions dans notre système. Il illustre comment les actions s'enchaînent et comment les choix sont faits.

```mermaid
stateDiagram
    login : Se connecter
    logon : Créer un compte
    create_playlist : Créer une playlist
    modifie_playlist : Modifier une playlist
    save_playlist : Sauvegarder la playlist
    logout : Se déconnecter
    
    [*] --> Accueil
    
    Accueil --> login
    login --> create_playlist
    
    Accueil --> logon
    
    Accueil --> quitter
    quitter --> [*]
    
    state create_playlist {
    	[*] --> save_playlist
    	[*] --> modifie_playlist
    	[*] --> logout
        logout --> [*]:retour accueil
    }
```