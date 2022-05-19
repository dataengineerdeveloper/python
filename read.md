>>> GIT <<<

RESUMO DE COMANDOS MAIS USADOS

1. git branch bug-123 >>> criar um novo branch,  para nao estar a trabalhar no master
2. git checkout master >>> NO CASO PRECISARMOS DE MUDAR OARA O BRANCH DE MASTER
3. git pull >>> no caso de estarmos num branch,  mas precismos de receber a a ultimas alteracoes que forma feitas
4. git add .  >>> adicionar alteracoes ao staging,  antes de ser feito o commit
5. git commit meuarquivo.txt -m "minha mensagem de commit"
6. git push -u origin master >>> primeiro pusha que faca tem de de ter o branch e repo
7. git push  >>> push que preciso de fazer de seguida nao preciso de colocar o branch nem repo
8. git checkout master
9. git merge bug-123
10. git push

11. git clone git@github.com:leocomelli/curso-git.git
12. git merge bug-123 >>> imginemos que vamos trabahar num branch ao lado do master depois tem de ser feito merge
13. git branch -d bug-123 >>> no fim quando tiver sido feit o merge posso fazer o delete do branch





comandos em detalhe git:

como criar um novo branch >>> 
trabalhar sobre a versão do master >>> git push --set-upstream origin 'mome da feature'

como add novas alteraçoes >>> git add .

como fazer o commit >>> git commit -m 'nova feature'

como ver o status do versionamento >>>  git status

como fazer o push das minhas alteraçoes >>>

como fazer o merge do meu branch para o master >>>

como criar um folder nova >>>

como adicionar ficheiros numa folder >>>

Geral

git config --global user.name "Leonardo Comelli"
git config --global user.email leonardo@software-ltda.com.br

Repositorio local

git init >>> criar um novo repositorio
git status >>> validar o estado dos arquivos

Adicionar oarquivos

git add . >>> adicionar tofdos os arquivos / diretorios
git add meu_diretorio >>> add um diretorio 
git add meu_arquivo.txt >>> add um arquivo em especifico


Commit

git commit meu_arquivo.txt  >>> commit de um arquivo
git commit meu_arquivo.txt meu_outro_arquivo.txt >>> commit de varios arquivos
git commit meuarquivo.txt -m "minha mensagem de commit" >>> fazer o commit com mensagem

Remover

git rm meu_arquivo.txt >>> remover um arquivo
git rm -r diretorio >>> remover diretorio

Visualizaçao de historico

git log >>> exibir os historico
git log -p -2 >>> exibir historico com as duas ultimas alteraçoes
git log --stat >>> exibir resumo do historico

repositorio remoto

git remote >>> apresenta todos os repositorios atuais

git remote add origin git@github.com:leocomelli/curso-git.git >>> vincular um repositorio loval com um repo remoto

git remotes show origin >>> exibir informaçao sobre o repo remoto
git remote rename origin curso-git >>> renomear um repo remoto
git remote rm curso-git >>> desvincular um repo remoto

Envio de de arquivos e diretoria para o repo remoto

git push -u origin master >>> o primeiro push deve de conter sempre o nome do repo remmoto e o brnach 

git push >>> o proximos push nao precisam da informaçao de repo remoto e branch

atualizar o repo local como o que está no repo remoto

git pull >>> atualizar conforme o branch remoto, que normalmente é a versao mais atual
git fetch >>> ir buscar as alteracoes mais recentes, mas nao aplicar no branch atual

clonar um repo ja existente

git clone git@github.com:leocomelli/curso-git.git

NOTA: o master e o branch principal do git

git branch bug-123 >>> criar um novo branch
git checkout bug-123 >>> trocar para um branch ja existente

git checkout -b bug-456 >>> imaginemos que precisamos de criar um novo branch e ao mesmo tempo fazer a troca
git checkout master >>> voltar para o branch principal

NOTA: imaginemos que estava  desenvolver este novo bugfix, para que seja possivel fazer o merge tenho de estar no branch que vai receber as alteracoes neste o caso no master

git merge bug-123 >>> resolver o merge entre os branch


NOTA: depois de terminado o desenvolvimento e ter feito merge,  posso simplesmte apagar o branch que criar para o desenvolvimento fo bugfix

git branch -d bug-123 >>> apagar um branch
git branch >>> se precisar de uma lista dos branchs existentes
git branch -v >>> quando preciso de listar informacao dos ultimos branchs que foram commitados
git branch --merged >>>  lista de brnachs que ja foram realizados os merges
git branch --no-merged >>> fazer a lista dos branch que nao foram feitos os merges

















