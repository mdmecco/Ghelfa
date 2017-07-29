pi@raspberrypi:~ $ cd desktop
bash: cd: desktop: File o directory non esistente
pi@raspberrypi:~ $ dir
2017-06-02-175305_976x736_scrot.png  Downloads	net-snmp  python_games	Videos
Desktop				     java	Pictures  Scratch
Documents			     Music	Public	  Templates
pi@raspberrypi:~ $ cd Desktop
pi@raspberrypi:~/Desktop $ dir
ETH484	ghelfa.sh  VNC-Server-5.3.2-Linux-ARM.deb
pi@raspberrypi:~/Desktop $ cd cd ETH484
bash: cd: cd: File o directory non esistente
pi@raspberrypi:~/Desktop $ cd ETH484
pi@raspberrypi:~/Desktop/ETH484 $ dir
Denkovi.py   Global.pyc		       network_socket.py
Denkovi.pyc  LetturaTelecamereWEB.py   network_socket.pyc
eth484.py    LetturaTelecamereWEB.pyc  PyGameModule.py
eth484.pyc   LGlobale.py	       PyGameModule.pyc
#Ghelfa.py   LGlobale.pyc
Global.py    main.py
pi@raspberrypi:~/Desktop/ETH484 $ git clone 
Devi specificare un repository da clonare.

   uso: git clone [options] [--] <repo> [<dir>]

    -v, --verbose         più dettagliato
    -q, --quiet           meno dettagliato
    --progress            force progress reporting
    -n, --no-checkout     don't create a checkout
    --bare                create a bare repository
    --mirror              create a mirror repository (implies bare)
    -l, --local           to clone from a local repository
    --no-hardlinks        don't use local hardlinks, always copy
    -s, --shared          setup as shared repository
    --recursive           initialize submodules in the clone
    --recurse-submodules  initialize submodules in the clone
    --template <template-directory>
                          directory from which templates will be used
    --reference <repo>    reference repository
    -o, --origin <name>   use <name> instead of 'origin' to track upstream
    -b, --branch <branch>
                          checkout <branch> instead of the remote's HEAD
    -u, --upload-pack <path>
                          path to git-upload-pack on the remote
    --depth <depth>       create a shallow clone of that depth
    --single-branch       clone only one branch, HEAD or --branch
    --separate-git-dir <gitdir>
                          separate git dir from working tree
    -c, --config <key=value>
                          set config inside the new repository

pi@raspberrypi:~/Desktop/ETH484 $ git clone pi@raspberrypi:/Desktop/ETH484
Cloning into 'ETH484'...
The authenticity of host 'raspberrypi (127.0.1.1)' can't be established.
ECDSA key fingerprint is b9:fa:9f:09:82:84:1c:be:05:92:17:85:04:92:94:27.
Are you sure you want to continue connecting (yes/no)? y
Please type 'yes' or 'no': yes
Warning: Permanently added 'raspberrypi' (ECDSA) to the list of known hosts.
pi@raspberrypi's password: 
Permission denied, please try again.
pi@raspberrypi's password: 
Permission denied, please try again.
pi@raspberrypi's password: 
Permission denied (publickey,password).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~/Desktop/ETH484 $ cd..
bash: cd..: comando non trovato
pi@raspberrypi:~/Desktop/ETH484 $ cd\
> 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ git init
Inizializzato un repository Git in /home/pi/.git/
pi@raspberrypi:~ $ dir
2017-06-02-175305_976x736_scrot.png  Downloads	net-snmp  python_games	Videos
Desktop				     java	Pictures  Scratch
Documents			     Music	Public	  Templates
pi@raspberrypi:~ $ git clone pi@raspberrypi:/Desktop/ETH484
Cloning into 'ETH484'...
pi@raspberrypi's password: 
Permission denied, please try again.
pi@raspberrypi's password: 
Permission denied, please try again.
pi@raspberrypi's password: 
Permission denied (publickey,password).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~ $ git clone pi@raspberrypi:/Desktop/ETH484
Cloning into 'ETH484'...
pi@raspberrypi's password: 
Permission denied, please try again.
pi@raspberrypi's password: 
fatal: '/Desktop/ETH484' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~ $ git clone pi@raspberrypi:/Desktop/ETH484
Cloning into 'ETH484'...
pi@raspberrypi's password: 
fatal: '/Desktop/ETH484' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~ $ git clone pi@raspberrypi:/Desktop/ETH484
Cloning into 'ETH484'...
pi@raspberrypi's password: 
Permission denied, please try again.
pi@raspberrypi's password: 
Permission denied, please try again.
pi@raspberrypi's password: 
fatal: '/Desktop/ETH484' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~ $ git add pi@raspberrypi:/Desktop/ETH484/*
fatal: pathspec 'pi@raspberrypi:/Desktop/ETH484/*' did not match any files
pi@raspberrypi:~ $ git add pi@raspberrypi:/Desktop/ETH484/*.*
fatal: pathspec 'pi@raspberrypi:/Desktop/ETH484/*.*' did not match any files
pi@raspberrypi:~ $ git add pi@raspberrypi:/Desktop/ETH484
fatal: pathspec 'pi@raspberrypi:/Desktop/ETH484' did not match any files
pi@raspberrypi:~ $ git add pi@raspberrypi:\Desktop\ETH484\*.*
fatal: pathspec 'pi@raspberrypi:DesktopETH484*.*' did not match any files
pi@raspberrypi:~ $ git add pi@raspberrypi:\Desktop\ETH484\*
fatal: pathspec 'pi@raspberrypi:DesktopETH484*' did not match any files
pi@raspberrypi:~ $ sudo apt-get install giggle
Lettura elenco dei pacchetti... Fatto
Generazione albero delle dipendenze       
Lettura informazioni sullo stato... Fatto
I seguenti pacchetti saranno inoltre installati:
  libgtksourceview-3.0-1 libgtksourceview-3.0-common
Pacchetti suggeriti:
  giggle-personal-details-plugin giggle-terminal-view-plugin
I seguenti pacchetti NUOVI saranno installati:
  giggle libgtksourceview-3.0-1 libgtksourceview-3.0-common
0 aggiornati, 3 installati, 0 da rimuovere e 328 non aggiornati.
È necessario scaricare 2.546 kB di archivi.
Dopo quest'operazione, verranno occupati 7.890 kB di spazio su disco.
Continuare? [S/n] S
Scaricamento di:1 http://mirrordirector.raspbian.org/raspbian/ jessie/main libgtksourceview-3.0-common all 3.14.1-1 [621 kB]
Scaricamento di:2 http://mirrordirector.raspbian.org/raspbian/ jessie/main libgtksourceview-3.0-1 armhf 3.14.1-1 [167 kB]
Scaricamento di:3 http://mirrordirector.raspbian.org/raspbian/ jessie/main giggle armhf 0.7-2+b1 [1.758 kB]
Recuperati 2.546 kB in 9s (267 kB/s)                                           
Selezionato il pacchetto libgtksourceview-3.0-common non precedentemente selezionato.
(Lettura del database... 124806 file e directory attualmente installati.)
Preparativi per estrarre .../libgtksourceview-3.0-common_3.14.1-1_all.deb...
Estrazione di libgtksourceview-3.0-common (3.14.1-1)...
Selezionato il pacchetto libgtksourceview-3.0-1:armhf non precedentemente selezionato.
Preparativi per estrarre .../libgtksourceview-3.0-1_3.14.1-1_armhf.deb...
Estrazione di libgtksourceview-3.0-1:armhf (3.14.1-1)...
Selezionato il pacchetto giggle non precedentemente selezionato.
Preparativi per estrarre .../giggle_0.7-2+b1_armhf.deb...
Estrazione di giggle (0.7-2+b1)...
Elaborazione dei trigger per gnome-menus (3.13.3-6)...
Elaborazione dei trigger per desktop-file-utils (0.22-1)...
Elaborazione dei trigger per mime-support (3.58)...
Elaborazione dei trigger per hicolor-icon-theme (0.13-1)...
Elaborazione dei trigger per man-db (2.7.0.2-5)...
Configurazione di libgtksourceview-3.0-common (3.14.1-1)...
Configurazione di libgtksourceview-3.0-1:armhf (3.14.1-1)...
Configurazione di giggle (0.7-2+b1)...
Elaborazione dei trigger per libc-bin (2.19-18+deb8u1)...
pi@raspberrypi:~ $ git commit -m "prova"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <pi@raspberrypi.(none)>) not allowed
pi@raspberrypi:~ $ git config --global mdmecco@mdmecco.it
error: invalid key: mdmecco@mdmecco.it
pi@raspberrypi:~ $ git config --global pi@raspberrypy "mdmecco@mdmecco.it"
error: key does not contain a section: pi@raspberrypy
pi@raspberrypi:~ $ git config --global mdmecco  "mdmecco@mdmecco.it"
error: key does not contain a section: mdmecco
pi@raspberrypi:~ $ git commit -m "prova"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <pi@raspberrypi.(none)>) not allowed
pi@raspberrypi:~ $ git config --global user.email "mdmecco@mdmecco.it"
pi@raspberrypi:~ $ git config --global user.name "Mecco"
pi@raspberrypi:~ $ git commit -m "prova"
[master (root-commit) c63438f] prova
 16 files changed, 1042 insertions(+)
 create mode 100644 Desktop/ETH484/#Ghelfa.py
 create mode 100644 Desktop/ETH484/Denkovi.py
 create mode 100644 Desktop/ETH484/Denkovi.pyc
 create mode 100644 Desktop/ETH484/Global.py
 create mode 100644 Desktop/ETH484/Global.pyc
 create mode 100644 Desktop/ETH484/LGlobale.py
 create mode 100644 Desktop/ETH484/LGlobale.pyc
 create mode 100644 Desktop/ETH484/LetturaTelecamereWEB.py
 create mode 100644 Desktop/ETH484/LetturaTelecamereWEB.pyc
 create mode 100644 Desktop/ETH484/PyGameModule.py
 create mode 100644 Desktop/ETH484/PyGameModule.pyc
 create mode 100755 Desktop/ETH484/eth484.py
 create mode 100644 Desktop/ETH484/eth484.pyc
 create mode 100755 Desktop/ETH484/main.py
 create mode 100755 Desktop/ETH484/network_socket.py
 create mode 100644 Desktop/ETH484/network_socket.pyc
pi@raspberrypi:~ $ git push origin master
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~ $ git push https://github.com/mdmecco/Ghelfa.git
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

fatal: Il branch corrente master non ha alcun branch upstream.
Per eseguire il push del branch corrente ed impostare remote come upstream, usa

    git push --set-upstream https://github.com/mdmecco/Ghelfa.git master

pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ git push --set-upstream https://github.com/mdmecco/Ghelfa.git master
Username for 'https://github.com': mdmecco@mdmecco.it
Password for 'https://mdmecco@mdmecco.it@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/mdmecco/Ghelfa.git/'
pi@raspberrypi:~ $ git push --set-upstream https://github.com/mdmecco/Ghelfa.git master
Username for 'https://github.com': mdmecco@mdmecco.it
Password for 'https://mdmecco@mdmecco.it@github.com': 
Counting objects: 20, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (18/18), done.
Writing objects: 100% (20/20), 14.55 KiB | 0 bytes/s, done.
Total 20 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/mdmecco/Ghelfa.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from https://github.com/mdmecco/Ghelfa.git.
pi@raspberrypi:~ $ 
