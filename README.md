# Agenda em Python usando Flask 

Este projeto foi elaborado para permitir o aprendizados de conceitos como 
MVC (Model-View-Controller), framework Flask e seus componentes, variáveis
de ambiente, paradigma de programação orientado a objetos e reforço de
fundamentos da linguagem de programação Python.

Para implemetar este objeto locamente, siga os seguintes passos:

1. Faça um fork deste repositório,clicando no botão `Fork`

2. clone este repositório localmente 

~~~bash 
git clone <url_repositorio>
~~~

3. Abra o projeto utilizando seu IDE preferido 

4. Crie, preferencialmente, um ambiente virtual utilizando uma versão do 
Python >3.12.10:

~~~bash
puthon -m venv .venv
~~~

5. Ative seu ambiente virtual.

    No bash:

    ~~~bash
    sourc .venv/Scripts/Activate
    ~~~

    No PowerShell
    ~~~
    .\.venv\Scripts\Activate.ps1
    ~~~

6. Instale todas as dependências contantes no arquivo   'requirements.txt':

~~~python 
pip insall -r requirements.txt
~~~

7. Copie o arquivo `.env.example`, cole na raiz do projeto e renomeie a copia para `.env`


8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`. Exemplo

~~~env
DATABASE= './data /meubanco.db'
~~~

9. Rode a aplicação no Python utilizando o comande:

~~~bash
flask run 
~~~

10. Acesse a aplicação no endereço e porta indicados no terminal. Exemplo:
``http://127.0.0.1:5000` 