# BLV Motors

Sistema de terminal em Python para gerenciar o banco de dados da concessionária fictícia BLV Motors.
Trabalho da disciplina Projeto de Banco de Dados (CESMAC).

## Primeiro administrador

Com as dependências instaladas e o `.env` configurado, execute na raiz:

```bash
python -m src.criar_primeiro_admin
```

A tabela `funcionarios` precisa existir; o script não cria tabelas. Esta execução
grava no banco configurado, portanto use somente quando for realizar o cadastro.
O cargo é definido como `admin`, e só é possível cadastrar se a tabela estiver
vazia. O bloqueio da tabela, a consulta e o INSERT usam a mesma transação;
o commit confirma o cadastro e o rollback desfaz em caso de erro.

A senha é lida com `getpass` e armazenada apenas como hash bcrypt com salt.
Exige no mínimo 8 caracteres e no máximo 72 bytes em UTF-8, sem remover espaços
nem truncar. O CPF é validado pelo formato de 11 dígitos, sem validar os dígitos
verificadores. Nome, telefone e login são obrigatórios e respeitam os limites SQL.

## Estrutura de pastas

```
src/
├── config/          # conexão com o banco (Neon)
├── repositories/    # comandos SQL
├── services/        # validações e regras de negócio
├── views/           # telas do terminal (menus, input e print)
├── utils/           # funções reaproveitadas por todos
└── main.py          # menu principal
sql/                 # script do banco (apenas referência)
```

### O que cada pasta faz

- **config/**: conecta no banco usando os dados do `.env`.
- **repositories/**: apenas SQL (insert, select, update, delete). Não usa `input` nem `print`.
- **services/**: validações e regras (CPF válido, veículo disponível etc.). Só existe quando há regra de verdade.
- **views/**: tudo que o usuário vê. Não contém SQL.
- **utils/**: funções de apoio (limpar tela, ler data, formatar CPF). Confira aqui antes de criar uma nova.

### Fluxo

```
main.py → view → service → repository → banco
```

### Padrão de nomes

Cada assunto tem um arquivo por pasta com o mesmo prefixo:

- `repositories/clientes_repository.py`
- `services/clientes_service.py`
- `views/clientes_view.py`

Cada view tem uma função `menu()`, chamada no `main.py`.

---

## Como funciona o Git neste projeto

- **main**: versão final e estável. Ninguém faz commit nem push direto nela.
- **develop**: onde as tarefas de todo mundo são juntadas e testadas.
- **branches de trabalho**: cada pessoa cria a sua a partir da develop, uma por tarefa, e depois junta na develop por Pull Request.

```
feature/sua-tarefa  →  develop  →  main
```

### Padrão de branches

| Prefixo | Quando usar | Exemplo |
|---|---|---|
| `feature/` | funcionalidade nova | `feature/crud-clientes` |
| `fix/` | correção de bug | `fix/validacao-cpf` |
| `config/` | estrutura e configuração do projeto | `config/estrutura-de-pastas` |
| `docs/` | só documentação | `docs/atualiza-readme` |
| `refactor/` | reorganizar código sem mudar o comportamento | `refactor/menu-clientes` |

Use letras minúsculas e palavras separadas por hífen.

### Padrão de commits

Formato: `tipo: descrição curta no presente`

| Tipo | Quando usar | Exemplo |
|---|---|---|
| `feat` | funcionalidade nova | `feat: adiciona cadastro de clientes` |
| `fix` | correção de bug | `fix: corrige validação de CPF` |
| `config` | estrutura, configuração, dependências | `config: cria estrutura de pastas` |
| `docs` | documentação | `docs: adiciona padrão de commits no README` |
| `refactor` | melhoria no código sem mudar o comportamento | `refactor: separa leitura de dados em utils` |
| `style` | formatação, espaços, nomes (sem mudar lógica) | `style: padroniza nomes de variáveis` |

Dicas:

- Um commit por alteração lógica, evitando juntar coisas diferentes.
- Descrição curta e direta, sem ponto final.

---

## Sequência de trabalho

### 1. Configuração inicial (só na primeira vez)

```bash
git clone https://github.com/brenoliraweb/proj-bd-concessionaria.git
```
Baixa o repositório do GitHub para o seu computador, criando a pasta `proj-bd-concessionaria`.

```bash
cd proj-bd-concessionaria
```
Entra na pasta do projeto. Todos os comandos seguintes são rodados daqui.

```bash
python -m venv .venv
```
Cria o ambiente virtual, uma pasta `.venv` onde ficam as bibliotecas só deste projeto.

```bash
.venv\Scripts\activate
```
Ativa o ambiente virtual (Windows). O terminal passa a mostrar `(.venv)` no início da linha. Precisa ativar sempre que abrir um terminal novo.

```bash
pip install -r requirements.txt
```
Instala todas as bibliotecas listadas no `requirements.txt`.

Por último, copie o arquivo `.env.example`, renomeie a cópia para `.env` e preencha com os dados do banco (enviados no privado).

> O arquivo `.env` nunca deve ser enviado ao GitHub. Ele já está no `.gitignore`.

Para rodar o sistema:

```bash
python src/main.py
```

### 2. Começar uma tarefa

```bash
git checkout develop
```
Muda para a branch develop, que é a base de todas as tarefas.

```bash
git pull
```
Baixa do GitHub tudo o que os outros já juntaram na develop, deixando a sua cópia atualizada.

```bash
git checkout -b feature/nome-do-assunto
```
Cria uma branch nova a partir da develop e já muda para ela. O `-b` significa "criar". Use o prefixo certo da tabela de branches.

> Sempre crie a branch a partir da develop atualizada. Nunca a partir da main ou de outra feature.

### 3. Durante o trabalho

```bash
git status
```
Mostra quais arquivos foram alterados, criados ou apagados. Use antes de cada commit para conferir o que vai entrar (e garantir que o `.env` não aparece).

```bash
git add .
```
Prepara todas as alterações para o próximo commit. O `.` significa "tudo nesta pasta". Para adicionar só um arquivo: `git add caminho/do/arquivo.py`.

```bash
git commit -m "feat: adiciona cadastro de funcionários"
```
Salva as alterações preparadas no histórico, com uma mensagem seguindo o padrão de commits. Prefira vários commits pequenos a um commit gigante no final.

### 4. Manter a branch atualizada (se a tarefa demorar)

Se a tarefa levar alguns dias, outras pessoas podem ter juntado coisas na develop nesse meio tempo. Traga essas mudanças para a sua branch para evitar conflitos no final:

```bash
git checkout develop
git pull
```
Atualiza a develop local com o que está no GitHub.

```bash
git checkout feature/nome-do-assunto
```
Volta para a sua branch.

```bash
git merge develop
```
Junta as novidades da develop na sua branch. Se aparecer conflito, o VS Code mostra os trechos em conflito para você escolher qual versão manter. Depois de resolver, faça `git add .` e `git commit`.

### 5. Enviar para o GitHub

```bash
git push -u origin feature/nome-do-assunto
```
Envia a sua branch para o GitHub. O `-u` liga a branch local à remota, então nos próximos envios dessa mesma branch basta usar:

```bash
git push
```

### 6. Abrir o Pull Request

1. No GitHub, vá em **Pull requests > New pull request** (ou clique no aviso amarelo "Compare & pull request").
2. Confira a direção: **base: develop ← compare: feature/nome-do-assunto**. Nunca `base: main`.
3. Coloque um título no mesmo padrão dos commits e uma descrição do que foi feito.
4. Clique em **Create pull request** e avise no grupo para alguém revisar.
5. Depois da revisão, clique em **Merge pull request > Confirm merge** e em **Delete branch**.

### 7. Depois do merge

```bash
git checkout develop
```
Volta para a develop.

```bash
git pull
```
Baixa a develop atualizada, que agora inclui o seu trabalho.

```bash
git branch -d feature/nome-do-assunto
```
Apaga a branch local que já foi usada. Os commits não se perdem, eles já estão na develop.

```bash
git fetch --prune
```
Remove do seu computador as referências de branches que já foram apagadas no GitHub.

Para a próxima tarefa, volte ao passo 2.

### 8. Levar a develop para a main

Feito só quando a develop estiver testada e estável (por exemplo, numa entrega para a professora):

1. No GitHub, abra um Pull Request **base: main ← compare: develop** e faça o merge.
2. No computador, atualize as duas branches:

```bash
git checkout main
git pull
git checkout develop
git merge main
git push
```
Isso deixa a develop igual à main, incluindo o commit do merge.

---

## Regras de ouro

- Nunca fazer commit direto na main nem na develop.
- Nunca enviar o `.env` para o GitHub.
- Sempre dar `git pull` na develop antes de criar uma branch nova.
- Rodar `git status` antes de cada commit.
- Pull Requests sempre para a develop.
- Seguir o padrão do CRUD de clientes ao criar um novo assunto.

## Comandos úteis

| Comando | O que faz |
|---|---|
| `git branch` | lista as branches locais e marca com `*` a atual |
| `git log --oneline -5` | mostra os últimos 5 commits de forma resumida |
| `git diff` | mostra as alterações ainda não adicionadas |
| `git restore arquivo.py` | descarta as alterações de um arquivo (não tem volta) |
| `git rm --cached arquivo` | tira um arquivo do Git sem apagar do computador |
