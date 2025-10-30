#!/usr/bin/env python3
# run_mitm_server.py
# Servidor HTTP simples que serve /mitm_test/login.html e trata POSTs.
# Uso: python run_mitm_server.py
# Acesse: http://localhost:8000/mitm_test/login.html

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from urllib.parse import parse_qs

PORT = 8000
SITE_DIR = os.path.join(os.getcwd(), "mitm_test")
HTML_FILENAME = "login.html"

HTML_CONTENT = """<!doctype html>
<html>
<head><meta charset="utf-8"><title>Login Test</title></head>
<body>
  <h1>Login Teste (HTTP)</h1>
  <form method="POST" action="/mitm_test/login.html">
    Usuário: <input name="user" /><br/>
    Senha:  <input type="password" name="password" /><br/>
    <button type="submit">Entrar</button>
  </form>
  <p>Teste: usuário=teste senha=12345</p>
</body>
</html>
"""

# garante que a pasta e o arquivo existam
os.makedirs(SITE_DIR, exist_ok=True)
html_path = os.path.join(SITE_DIR, HTML_FILENAME)
if not os.path.isfile(html_path):
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[+] Arquivo criado em: {html_path}")
else:
    print(f"[+] Arquivo já existe: {html_path}")

class SimpleMITMHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the login.html for the exact path, or simple 404 otherwise
        if self.path == f"/mitm_test/{HTML_FILENAME}" or self.path == "/mitm_test/":
            try:
                with open(html_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_error(500, f"Erro ao ler o arquivo: {e}")
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        # Handle form submission from /mitm_test/login.html
        if self.path == f"/mitm_test/{HTML_FILENAME}":
            content_length = int(self.headers.get('Content-Length', 0))
            body_bytes = self.rfile.read(content_length)
            body = body_bytes.decode('utf-8', errors='replace')
            # Parse form data (application/x-www-form-urlencoded)
            parsed = parse_qs(body)
            user = parsed.get('user', [''])[0]
            password = parsed.get('password', [''])[0]

            # Log to console
            print("=== REQUISIÇÃO POST RECEBIDA ===")
            print(f"Raw body: {body}")
            print(f"user = {user}")
            print(f"password = {password}")
            print("=================================")

            # Save to a file (evidence)
            received_path = os.path.join(SITE_DIR, "received.txt")
            with open(received_path, "a", encoding="utf-8") as rf:
                rf.write(f"user={user}&password={password}\n")

            # Respond with a simple HTML confirmation
            response_html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Enviado</title></head>
<body>
  <h1>Dados recebidos</h1>
  <p>Usuário: {user}</p>
  <p>Senha: {password}</p>
  <p><a href="/mitm_test/login.html">Voltar</a></p>
</body></html>"""
            resp_bytes = response_html.encode('utf-8')
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(resp_bytes)))
            self.end_headers()
            self.wfile.write(resp_bytes)
        else:
            self.send_error(404, "Not Found")

    def log_message(self, format, *args):
        # opcional: reduz logs automáticos do server (mantém prints personalizados)
        return

if __name__ == "__main__":
    server_address = ("", PORT)  # '' = all interfaces (localhost included)
    httpd = HTTPServer(server_address, SimpleMITMHandler)
    print(f"[+] Servidor HTTP iniciado em http://localhost:{PORT}/mitm_test/login.html")
    print("[+] Pare o servidor com CTRL+C")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Servidor interrompido pelo usuário")
    finally:
        httpd.server_close()
