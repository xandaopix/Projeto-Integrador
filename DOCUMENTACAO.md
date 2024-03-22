# Documentação

Crie e ative um ambiente virtual em sua máquina:
 -  Abra o terminal e navegue até o diretório onde deseja criar seu 
    projeto Django.
 -  Execute `py -m venv myenv` para criar um 
    ambiente virtual.
   -  No Windows, execute `myenv\Scripts\activate`.
   -  No macOS e Linux, execute `source myenv/bin/activate`.
 -  Com o ambiente virtual ativado, instale o Django usando
    `pip install django`.
   
Após a instalação do Django em seu ambiente virtual, cole a pasta "projetointegrador" na pasta raiz do ambiente virtual. Com o ambiente virtual ativado, navegue até a pasta utilizando o comando `cd projetointegrador` e, em seguida, utilize o comando `py manage.py runserver`. Abra seu navegador e acesse `http://127.0.0.1:8000`.

Para o usuário cadastrar-se como Professor, é necessário um código 'especial'. Por padrão, esse código é `1155`. Caso deseje modificar:
- acesse o arquivo `views.py`;
- navegue até a função `user_signupprofessor(request)`;
- procure pelo comentário `#Código de autenticação do professor.` e modifique o número do interior das aspas.

## Modelagem de banco de dados

Coloque aqui a modelagem do banco de dados desenvolvido no projeto. Você pode colocar diagramas conceituais e lógicos, ou até mesmo descrever textualmente o que cada uma das tabelas e atributos representam. 
