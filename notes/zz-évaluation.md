# le devoir pour l'évaluation

## reprendre l'application 'notes'

voir le devoir précédent, et le gif associé que je vous remets dans ce message

**rappel**: il s'agit de faire un petit service de notes:

- on peut créer les notes depuis le terminal avec

```bash
http :5001/api/notes title="devoirs" content="faire le devoir d'info"
http :5001/api/notes title="dentiste" content="mercredi 14h"
```

- on peut afficher les notes en pointant le navigateur sur http://localhost:5001/  
  (qui en fait redirige vers http://localhost:5001/front/notes)

- depuis le navigateur on peut marquer une note comme faite ou pas faite  
  l'information est alors stockée dans la base de données  
  (dit autrement, si on ouvre maintenant un autre navigateur sur cette page, on voit la note marquée comme faite ou pas faite)

## en supplément

en sus de la première consigne, on ajoute une fonctionnalité de synchro entre les navigateurs:

- lorsque deux navigateurs sont ouverts sur la page, les modifications faites dans l'un sont visibles dans l'autre

je vous joins également une vidéo de démonstration de cette fonctionnalité

## les supports

pour vous aider, je vous renvoie aux supports de cours suivant:

- le pas à pas pour notre application de chat, qu'on a vue en cours

  https://ue22-p24.github.io/backend-flask-chatapp/

- ce premier support explique pas à pas comment on en arrive au code final, qui se trouve ici

  https://github.com/ue22-p24/backend-flask-chatapp-steps

## délai et modalités

- vous le rendez dans votre repo `backend-homework` dans le dossier `notes`
- je vous laisse jusqu'à **fin mai** pour le faire
