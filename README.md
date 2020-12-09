# Curso Django Alura
Repositório criado para acompanhar a formação de Django da Alura

**Readme em construção**

## Dependências do projeto

### Banco de dados
Este projeto utiliza conexão com o banco de dados do PostgreSQL, que está configurado somente para acesso local, por isso é necessário que tenha esse servidor de banco de dados instalado e ativo na sua máquina antes de rodar o comando para rodar o projeto localmente.

### Versão do Python
Ao clonar o repositório, certifique-se de que possui instalado na sua máquina a versão 3.7.4 do Python para evitar problemas de compatibilidade, logo é recomendável utilzar a versão que foi  utilizada originalmente no projeto. Nesses casos é interessante usar um administrador de versões, como o pyenv, por exemplo.

### Ambiente virtual do Python
Após instalar a versão do Pytno mencionada acima, acesse a pasta do projeto e crie o ambiente virtual do Python com o comando `python3 -m venv ./venv`, assim será possível instalar as dependências utilizadas neste projeto.

### Ativar o ambiente virtual do Python (venv)
Esta ativação precisa ser realizada toda vez que quiser rodar o projeto localmente ou para instalar dependências (seja novas ou as que já estão sendo utilizadas). Para ativar a venv rode o comando `source /caminho/da/pasta/raiz/do/projeto/venv/bin/activate`.
**Dica:** Para saber o caminho da raiz do projeto até o arquivo `activate` da pasta `venv`, rode o comando `pwd` (para sistemas Linux e iOS). Esse comando retornará o caminho completo da pasta do projeto desde a raiz da sua máquina, como por exemplo, `/home/usuario/projetos/curso_django_alura/`. Sendo assim basta então concatenar esse resultado com `venv/bin/activate`, para poder rodar o comando de ativação da venv: `source /home/usuario/projetos/curso_django_alura/venv/bin/activate`, se considerar o exemplo deste dica.

### Como instalar as dependências já utilizadas
As dependências deste projeto estão listadas no arquivo `requirements.txt`. Após ativar seu ambiente virtual é possível instalar as dependências através do comando `pip install -r requirements.txt`.

### Listar dependências adicionadas ao projeto
Para listar novas dependências que foram adicionadas ao projeto, precisa atualizar o arquivo requirements.txt. É possível fazer isso de forma automática através do comando: `pip freeze > requirements.txt`.

### Rodar o projeto localmente
Rode o comando `python manage.py runserver` a partir da pasta raiz do projeto.
