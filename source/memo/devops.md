# Devops

## Liens

- [OWASP](https://owasp.org/)
- [Pre-Commit](https://pre-commit.com/)
- [Pulumi](https://www.pulumi.com/docs/)
- [Github Actions](https://docs.github.com/fr/actions)
- [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Localstack](https://localstack.cloud/)

## Outils Générique
- [vscode](https://code.visualstudio.com/)

### Windows
- [Windows Terminal](https://github.com/microsoft/terminal)  (Les commandes doivent être executé dans un powershell en tant qu'administrateur)
  - Aller sur le [tag](https://github.com/microsoft/terminal/tags) le plus récent
  - en bas de page, récupérer le fichier `.msixbundle` correspondant a votre système (Windows 10 ou Windows 11)
  - Executer la commande `$ Add-AppxPackage Path/Vers/LeFichier.msixbundle`
- [WSL 2](https://learn.microsoft.com/fr-fr/windows/wsl/install-manual) (Les commandes doivent être executé dans un powershell en tant qu'administrateur)
  - Réaliser les étapes 1 et 3
  - Rédémarrer
  - Réaliser l'étape 4 et 5
  - puis executer la commande `$ wsl --install -d NomDeladistribution`
    - par exemple: `$ wsl --install -d Ubuntu`
- [docker desktop](https://docs.docker.com/engine/install/)

> Attention: Si vous obtenez une erreur dans votre WSL2 en faisant `sudo apt update`, il faut faire quelque
> modification:
> - ajouté le un fichier `/etc/wsl.conf` contenant les informations suivantes:
>   ```bash
>   [network]
>   generateResolvConf = false
>   ```
> - remplacer le contenu du fichier `/etc/resolv.conf` par:
>   ```bash
>   nameserver 8.8.8.8
>   ```

### UNIX

Dans la distribution WSL2:
- [zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH), un shell non-casesensitive, extrèmement configurable
  - `$ sudo apt install zsh`
  - `$ chsh -s $(which zsh)`
- [oh-myzsh](https://github.com/ohmyzsh/ohmyzsh), un framework pour configurer et adapter votre shell a vos envies (themes, plugins, etc)
  - [installation](https://github.com/ohmyzsh/ohmyzsh#manual-inspection)
  - exemple de [plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins):
    - `git`
    - `gitfast`
    - `pip`
    - `python`
    - `screen`
    - `themes`
    - `ubuntu`
    - `timer`
    - `docker`
    - `docker-compose`
    - `virtualenvwrapper` (il faut faire `pip install virtualenvwrapper` pour qu'il fonctionne, un message d'erreur persiste mais peut être ignoré)
  - [page des themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)
- [docker](https://docs.docker.com/engine/install/ubuntu/)


## Configuration Git

### Configurer le ssh
Générer des clés ssh avec:
```bash
$ ssh-keygen
```
puis ajouté votre clé public dans l'[espace github](https://github.com/settings/keys)

### Configurer un PAT (Personnal Access token)

- accéder à la page github [personnal access token](https://github.com/settings/tokens)
- configurer un token avec au moins les droits en lecture suivant:
  - `repo`
  - `read:org`
  - `read:public_key`
  - `read:repo_hook`
  - `notification`
  - `user`
  - `read:discussion`
  - `read:audit_log`
  - `read:project`

Pour ne pas avoir a rentrer votre 'PAT' a chaque fois, effectuer la commande suivante:
- ```bash
  `$ git config --global credential.helper store
  ```

> **Attention**: Lors de votre premier `$ git clone`, si votre nom d'utilisateur vous est demandé
> suivi d'un champ mot de passe, ce dernier doit être rempli avec le PAT
