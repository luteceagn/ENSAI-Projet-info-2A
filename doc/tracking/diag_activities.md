---
title : Diagramme d'activité de l'application
---
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