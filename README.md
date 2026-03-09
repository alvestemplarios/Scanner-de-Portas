# 🔎 Port Scanner em Python

Projeto simples de **Scanner de Portas** desenvolvido em **Python** para fins educacionais e prática de conceitos de redes e cibersegurança.

Este programa verifica quais portas estão abertas em um host ou servidor utilizando conexões TCP.

---

## 📌 Objetivo do Projeto

Este projeto foi criado para praticar:

* Programação em **Python**
* Conceitos de **Redes de Computadores**
* Fundamentos de **Cibersegurança**
* Uso de **Sockets**
* Automação de tarefas

O scanner tenta se conectar a várias portas de um host e informa quais estão abertas.

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Biblioteca padrão `socket`

---

## 📂 Estrutura do Projeto

```
port-scanner-python
│
├── scanner.py
└── README.md
```

---

## 💻 Código do Scanner

```python
import socket

alvo = input("Digite o IP ou site para escanear: ")

print("Escaneando portas...")

for porta in range(1, 1025):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)

    resultado = cliente.connect_ex((alvo, porta))

    if resultado == 0:
        print("Porta aberta:", porta)

    cliente.close()

print("Escaneamento finalizado.")
```

---

## ▶️ Como Executar o Projeto

1. Clone o repositório

```
git clone https://github.com/SEU-USUARIO/port-scanner-python.git
```

2. Entre na pasta do projeto

```
cd port-scanner-python
```

3. Execute o programa

```
python scanner.py
```

---

## 📊 Exemplo de Execução

```
Digite o IP ou site para escanear: scanme.nmap.org

Escaneando portas...

Porta aberta: 22
Porta aberta: 80
Porta aberta: 443

Escaneamento finalizado.
```

---

## ⚠️ Aviso Importante

Este projeto foi desenvolvido **apenas para fins educacionais**.

Não utilize este programa para escanear redes ou sistemas sem autorização.

O uso indevido pode violar leis de segurança digital.

---

## 👨‍💻 Autor

**Julio Cesar Alves de Oliveira**

Estudante de tecnologia, redes de computadores e segurança da informação.

---

## ⭐ Contribuição

Sinta-se à vontade para:

* abrir **issues**
* sugerir melhorias
* enviar **pull requests**

---

## 📚 Aprendizados

Este projeto ajuda a compreender:

* funcionamento de **portas TCP**
* comunicação entre **cliente e servidor**
* automação com Python
* fundamentos de **segurança ofensiva e defensiva**

---

## 🚀 Melhorias Futuras

* Scanner mais rápido usando **threads**
* Identificação de **serviços rodando nas portas**
* Exportar resultados para **arquivo JSON ou CSV**
* Interface gráfica

---

