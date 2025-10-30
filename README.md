# Ativ-MITM

Download do aplicativo Wireshark
=> https://www.wireshark.org/download.html


**Wireshark e Lightshot**


## 🔹 Wireshark

**O que é:**
Ferramenta gratuita e de código aberto usada para **analisar pacotes de rede** (protocolos TCP/IP, HTTP, HTTPS, DNS etc.).

**Para que serve:**

* Monitorar e diagnosticar o tráfego de rede;
* Detectar vulnerabilidades e ataques (*Man-in-the-Middle*);
* Ver dados transmitidos em texto claro (em conexões sem HTTPS).

**Como funciona:**
Captura pacotes em tempo real e os exibe detalhadamente — IPs, portas, protocolo e conteúdo.
No seminário, foi usado para capturar a requisição:

```
POST /login.html
user=teste&password=12345
```

mostrando como um MITM pode ler dados não criptografados.

**Principais recursos:**

* Filtros de captura e exibição (ex.: `http`, `tcp.port==80`);
* Exportação de pacotes `.pcap`;
* Visualização detalhada das camadas de rede.

**Site oficial:** [https://www.wireshark.org/](https://www.wireshark.org/)



## 🔹 Lightshot

**O que é:**
Aplicativo leve de **captura de tela rápida**, ideal para registrar prints de testes e resultados técnicos.

**Para que serve:**

* Documentar evidências (telas do Wireshark, configurações, erros);
* Editar prints com setas, textos e destaques;
* Salvar ou gerar link direto para compartilhamento.

**Como funciona:**
Pressione **PrtScn**, selecione a área da tela, edite e salve (`Ctrl + S`) ou envie (`Ctrl + D`).
No seminário, foi usado para capturar os prints das etapas práticas do MITM.

**Site oficial:** [https://app.prntscr.com/](https://app.prntscr.com/)


## 🔸 Conclusão

| Ferramenta    | Tipo                  | Função no Seminário                           |
| ------------- | --------------------- | --------------------------------------------- |
| **Wireshark** | Analisador de pacotes | Demonstrar interceptação e análise de tráfego |
| **Lightshot** | Captura de tela       | Registrar prints e evidências visuais         |

---

Quer que eu adicione esse resumo formatado no **final do documento do seminário** (como anexo técnico “Ferramentas Utilizadas”)? Posso gerar o `.docx` atualizado agora.
