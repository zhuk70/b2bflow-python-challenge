# B2BFlow Python Challenge

Projeto desenvolvido para o processo seletivo de Estágio em Desenvolvimento Python da b2bflow.

## Funcionalidades

* Busca contatos cadastrados no Supabase.
* Limita a leitura para até 3 contatos.
* Envia mensagens personalizadas via Z-API.
* Utiliza variáveis de ambiente para configuração.

Mensagem enviada:

Olá, <nome_contato> tudo bem com você?

## Estrutura da tabela

Tabela: Contatos

Campos:

* Id (int8)
* Nome (text)
* Telefone (text)

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python src/main.py
```
