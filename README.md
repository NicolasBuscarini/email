# SETAR AMBIENTE

`set APP_ENV=development  # Windows`
`export APP_ENV=development  # Linux/macOS`
# ou
`set APP_ENV=PRODUCTION  # Windows`
`export APP_ENV=PRODUCTION  # Linux/macOS`

# Gerar executável com PyInstaller

Essa é a forma mais estável, multiplataforma e fácil de manter.
Instalação:

`pip install pyinstaller`

## 🔧 Comando básico (Windows ou Linux)

Dentro da pasta do seu projeto (onde está send_email.py):

`pyinstaller --onefile --name send_email --add-data ".env.development;." --add-data "body.txt;." send_email.py`


### 📘 Explicando:

| Parâmetro |	Função |
| -- | -- |
| `--onefile` |	Gera um único executável compacto |
| `--name send_email` |	Define o nome do executável final |
| `--add-data` |	Inclui arquivos necessários (.env.development, body.txt) dentro do binário |
| `send_email.py` | 	Seu script principal |

* ⚠️ No Linux, o separador de caminho em --add-data é : em vez de ;:
  `--add-data ".env.development:."`

* 📦 Saída
  Após o build, o executável ficará em:

   - dist/send_email.exe     (Windows)
   ou
   - dist/send_email         (Linux)


Você pode copiar apenas esse arquivo e o .env (se preferir externo) para o servidor.