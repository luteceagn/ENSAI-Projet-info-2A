# Diagramme d'activité

> Ce diagramme UML d'activité modélise le flux de travail d'un processus, il montre la séquence d'activités et de décisions dans notre système. Il illustre comment les actions s'enchaînent et comment les choix sont faits.

```mermaid
stateDiagram
    login : Se connecter
    logon : Créer un compte
    add_song : Ajouter une chanson
    Delete_song : SUpprimer une chanson
    create_playlist : Créer une playlist
    modifie_playlist : Modifier une playlist
    save_playlist : Sauvegarder la playlist
    logout : Se déconnecter
    
    [*] --> Accueil
    
    Accueil --> login
    
    
    Accueil --> logon
    
    Accueil --> quitter
    quitter --> [*]
    
    state login {
        [*]--> create_playlist
        [*]--> see_playlist
        [*]--> logout
    }
    state create_playlist {
    	[*] --> save_playlist
    	[*] --> modifie_playlist
    	[*] --> logout
        logout --> [*]:retour accueil
    }

    state modifie_playlist {
        [*]--> add_song
        [*]--> Delete_song
    }
```