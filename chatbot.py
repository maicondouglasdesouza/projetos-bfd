import customtkinter as ctk

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")  # temas: "dark", "light", "system"
ctk.set_default_color_theme("blue")

# Função para processar mensagens
def enviar():
    msg = entrada.get().strip().lower()
    if not msg:
        return

    respostas = {
        "oi": "Olá! Como vai você?",
        "ola": "Oi! Tudo bem por aí?",
        "tudo bem": "Estou ótimo, e você?",
        "qual seu nome": "Eu sou o ChatPy, seu assistente feito em Python!",
        "quem te criou": "Fui criado por um programador curioso usando Python e CustomTkinter 😄",
        "o que voce faz": "Eu converso com você e posso ser programado para fazer várias coisas!",
        "sair": "Até mais 👋",
        "bom dia": "Bom dia! ☀️ Que seu dia seja incrível!",
        "boa tarde": "Boa tarde! Espero que esteja indo tudo bem 😄",
        "boa noite": "Boa noite 🌙, descanse bem!",
        "qual a sua linguagem": "Fui criado em Python 🐍",
        "me conta uma piada": "Por que o livro foi ao médico? Porque ele estava com muitas histórias! 😂",
        "obrigado": "De nada! 😊",
    }

    resposta = respostas.get(msg, "Desculpe, não entendi... pode repetir?")

    # Mostra no chat
    chat.insert(ctk.END, f"🧑 Você: {msg}\n")
    chat.insert(ctk.END, f"🤖 Bot: {resposta}\n\n")

    entrada.delete(0, ctk.END)

    if msg == "sair":
        janela.after(1500, janela.destroy)  # fecha após 1,5s

# Cria a janela principal
janela = ctk.CTk()
janela.title("Chatbot com CustomTkinter")
janela.geometry("500x500")

# Título
titulo = ctk.CTkLabel(janela, text="🤖 ChatBot Python", font=("Arial", 22, "bold"))
titulo.pack(pady=10)

# Área de chat
chat = ctk.CTkTextbox(janela, width=460, height=350, corner_radius=10)
chat.pack(pady=10)
chat.insert(ctk.END, "👋 Olá! Eu sou o ChatPy. Envie uma mensagem para começar.\n\n")

# Frame para entrada e botão
frame = ctk.CTkFrame(janela)
frame.pack(pady=5)

entrada = ctk.CTkEntry(frame, width=340, placeholder_text="Digite sua mensagem...")
entrada.pack(side="left", padx=5, pady=5)

botao = ctk.CTkButton(frame, text="Enviar", command=enviar)
botao.pack(side="left", padx=5)

# Permite enviar com Enter
janela.bind("<Return>", lambda event: enviar())

# Inicia o app
janela.mainloop()
