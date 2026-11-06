import sqlite3

# 1. Conecta ao banco de dados (cria o arquivo chamados.db na mesma pasta)
conn = sqlite3.connect('chamados.db')
cursor = conn.cursor()

# 2. Cria a tabela no banco de dados se ela ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    prioridade TEXT,
    status TEXT,
    usuario TEXT
)
''')
conn.commit()

# 3. Colocamos a sua lista completa aqui para preencher o banco de dados na primeira vez
def popular_banco_inicial():
    # Verifica se o banco já tem dados. Se estiver vazio (0), ele insere sua lista.
    cursor.execute("SELECT COUNT(*) FROM chamados")
    if cursor.fetchone()[0] == 0:
        chamados_iniciais = [
            ("Erro no login", "Alta", "Aberto", "Ana Silva"),
            ("Tela branca no app", "Crítica", "Aberto", "Bruno Costa"),
            ("Atualizar cadastro", "Baixa", "Em progresso", "Carlos Souza"),
            ("Boleto não gerado", "Média", "Aberto", "Daniela Lima"),
            ("Botão quebrado", "Baixa", "Aberto", "Eduardo Rocha"),
            ("Lentidão na busca", "Média", "Em progresso", "Fernanda Alves"),
            ("Recuperar senha", "Alta", "Aberto", "Gabriel Santos"),
            ("Erro no Pix", "Crítica", "Aberto", "Amanda Melo"),
            ("Mudar foto de perfil", "Baixa", "Fechado", "Igor Ribeiro"),
            ("Exportar PDF falhou", "Média", "Aberto", "Juliana Vieira"),
            ("Carrinho esvaziando", "Alta", "Em progresso", "Lucas Martins"),
            ("Cupom inválido", "Média", "Aberto", "Mariana Dias"),
            ("Página 404 no FAQ", "Baixa", "Aberto", "Nicolas Ferreira"),
            ("Atraso na entrega", "Alta", "Aberto", "Patricia Gomes"),
            ("Email de boas-vindas", "Baixa", "Fechado", "Rodrigo Ramos"),
            ("Estorno pendente", "Alta", "Em progresso", "Sabrina Oliveira"),
            ("Alerta de segurança", "Crítica", "Aberto", "Thiago Barbosa"),
            ("Link quebrado no menu", "Baixa", "Aberto", "Vanessa Cunha"),
            ("Nota fiscal sumiu", "Média", "Aberto", "Willian Cardoso"),
            ("Modo escuro travando", "Baixa", "Em progresso", "Yasmim Lopes"),
            ("Erro na API de CEP", "Alta", "Aberto", "Arthur Antunes"),
            ("Notificação duplicada", "Baixa", "Aberto", "Beatriz Mendes"),
            ("Sessão expirando rápido", "Média", "Em progresso", "Caio Nogueira"),
            ("Erro no cartão de crédito", "Crítica", "Aberto", "Diana Prince"),
            ("Traduzir termo em inglês", "Baixa", "Fechado", "Elton John"),
            ("Chat de suporte offline", "Alta", "Aberto", "Fábio Assunção"),
            ("Upload de comprovante", "Média", "Aberto", "Gisele Bündchen"),
            ("Histórico sumiu", "Alta", "Em progresso", "Heitor Villa"),
            ("Termos de uso desatualizados", "Baixa", "Aberto", "Isabela Garcia"),
            ("Erro 500 no checkout", "Crítica", "Aberto", "Jorge Ben"),
            ("Ajustar margem do header", "Baixa", "Em progresso", "Karina Bacchi"),
            ("Filtro por data quebrado", "Média", "Aberto", "Leonardo Dicaprio"),
            ("Assinatura não renovada", "Alta", "Aberto", "Marta Vieira"),
            ("Áudio do vídeo não funciona", "Média", "Aberto", "Neymar Junior"),
            ("Atualizar política de privacidade", "Baixa", "Fechado", "Otávio Mesquita"),
            ("Queda do servidor interno", "Crítica", "Em progresso", "Paula Toller"),
            ("Convite por email falhou", "Baixa", "Aberto", "Quintino Aires"),
            ("Extrato em branco", "Alta", "Aberto", "Renata Vasconcellos"),
            ("ícone errado no painel", "Baixa", "Aberto", "Samuel Rosa"),
            ("Duplicidade de cobrança", "Crítica", "Aberto", "Tais Araújo"),
            ("Validação de CNPJ", "Média", "Em progresso", "Umberto Eco"),
            ("Mensagem de erro confusa", "Baixa", "Aberto", "Valéria Valenssa"),
            ("Problema com fonte negrito", "Baixa", "Aberto", "Wagner Moura"),
            ("Links de redes sociais fora do ar", "Média", "Aberto", "Xuxa Meneghel"),
            ("Sem sinal de geolocalização", "Alta", "Em progresso", "Yuri Gagarin"),
            ("Página recarregando sozinha", "Alta", "Aberto", "Zeca Pagodinho"),
            ("Gráfico de vendas travado", "Média", "Aberto", "Alinne Moraes"),
            ("Impossível remover endereço", "Média", "Em progresso", "Beto Jamaica"),
            ("Vazamento de memória na aba", "Crítica", "Aberto", "Cláudia Raia"),
            ("Ajustar alinhamento do rodapé", "Baixa", "Fechado", "Dado Dolabella")
        ]
        # Aqui ele insere a sua lista de uma vez no banco
        cursor.executemany('''
            INSERT INTO chamados (titulo, prioridade, status, usuario) 
            VALUES (?, ?, ?, ?)
        ''', chamados_iniciais)
        conn.commit()

# Executa a função para garantir que a lista esteja lá
popular_banco_inicial()


# --- Funções do Sistema adaptadas para buscar no banco de dados ---

def usuario():
    user = input("Digite o Usuário: ")
    cursor.execute("SELECT id, titulo, status FROM chamados WHERE usuario LIKE ?", (user,))
    resultados = cursor.fetchall()

    if resultados:
        for row in resultados:
            print(f"ID: {row[0]} | Título: {row[1]} | Status: {row[2]}")
    else:
        print("Usuário não encontrado.")

def prioridade():
    escolha = input("Qual prioridade você quer ver? (Crítica, Alta, Média, Baixa): ")
    print(f"\n--- Chamados com Prioridade: {escolha} ---")
    
    cursor.execute("SELECT id, titulo, usuario FROM chamados WHERE prioridade LIKE ?", (escolha,))
    resultados = cursor.fetchall()

    if resultados:
        for row in resultados:
            print(f"ID: {row[0]} | Título: {row[1]} | Usuário: {row[2]}")
    else:
        print("Nenhum chamado encontrado com essa prioridade.")

def status():
    escolha = input("Qual status você quer ver? (Aberto, Em progresso, Fechado): ")
    print(f"\n--- Chamados com Status: {escolha} ---")
    
    cursor.execute("SELECT id, titulo, usuario FROM chamados WHERE status LIKE ?", (escolha,))
    resultados = cursor.fetchall()

    if resultados:
        for row in resultados:
            print(f"ID: {row[0]} | Título: {row[1]} | Usuário: {row[2]}")
    else:
        print("Nenhum chamado encontrado com esse status.")

def urgencia():
    cursor.execute("SELECT id, titulo, status FROM chamados WHERE status = 'Aberto' AND prioridade = 'Crítica'")
    resultados = cursor.fetchall()
    
    if resultados:
        for row in resultados:
            print(f"{row[0]} | {row[1]} | {row[2]}")
    else:
        print("Nenhum chamado urgente no momento.")

def abrir():
    titulo = input("Digite o nome do Chamado: ")
    prioridade = input("Digite a Prioridade: ")
    status = input("Digite o Status: ")
    user = input("Digite o Usuário: ")
    
    # Adiciona um novo chamado na tabela do banco
    cursor.execute('''
        INSERT INTO chamados (titulo, prioridade, status, usuario) 
        VALUES (?, ?, ?, ?)
    ''', (titulo, prioridade, status, user))
    conn.commit()
    print("Chamado aberto com sucesso!")

def resolver():
    print("--- Tarefas Disponíveis ---")
    cursor.execute("SELECT titulo, status FROM chamados")
    for row in cursor.fetchall():
        print(f"Título: {row[0]} | Status atual: {row[1]}")

    chamado_desejado = input("\nQual tarefa deseja finalizar? ")

    cursor.execute("SELECT id, status FROM chamados WHERE titulo LIKE ?", (chamado_desejado,))
    chamado = cursor.fetchone()

    if chamado:
        id_chamado = chamado[0]
        status_atual = chamado[1]

        if status_atual == "Em progresso":
            # Atualiza o status do chamado no banco de dados
            cursor.execute("UPDATE chamados SET status = 'Fechado' WHERE id = ?", (id_chamado,))
            conn.commit()
            print(f"O Chamado '{chamado_desejado}' foi finalizado com sucesso!")
        else:
            print(f"O Chamado '{chamado_desejado}' não pode ser fechado porque o status atual é: {status_atual}")
    else:
        print("Tarefa não encontrada.")

def fechar():
    print("--- Tarefas Disponíveis ---")
    cursor.execute("SELECT titulo, status FROM chamados")
    for row in cursor.fetchall():
        print(f"Título: {row[0]} | Status atual: {row[1]}")

    chamado_desejado = input("\nQual tarefa deseja fechar? ")

    cursor.execute("SELECT id, status FROM chamados WHERE titulo LIKE ?", (chamado_desejado,))
    chamado = cursor.fetchone()

    if chamado:
        id_chamado = chamado[0]
        status_atual = chamado[1]

        if status_atual == "Aberto":
            # Atualiza o status do chamado no banco de dados
            cursor.execute("UPDATE chamados SET status = 'Fechado' WHERE id = ?", (id_chamado,))
            conn.commit()
            print(f"O Chamado '{chamado_desejado}' foi fechado com sucesso!")
        else:
            print(f"O Chamado '{chamado_desejado}' não pode ser fechado porque o status atual é: {status_atual}")
    else:
        print("Tarefa não encontrada.")


# --- Menu Principal ---
while True:
    print("\n# Lista de Tarefas #")
    print("1 - Pesquisa por Usuário")
    print("2 - Pesquisa por Prioridade")
    print("3 - Pesquisa por Status")
    print("4 - Chamados urgentes (Crítico e Abertos)")
    print("5 - Abrir chamado")
    print("6 - Resolver chamado")
    print("7 - Fechar chamado")
    print("0 - Sair")

    try:
        pergunta = int(input("\nQual opção deseja? "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if pergunta == 1:
        usuario()
    elif pergunta == 2:
        prioridade()
    elif pergunta == 3:
        status()
    elif pergunta == 4:
        urgencia()
    elif pergunta == 5:
        abrir()
    elif pergunta == 6:
        resolver()
    elif pergunta == 7:
        fechar()
    elif pergunta == 0:
        print("Programa Finalizado! Até a Próxima...")
        conn.close() 
        break
    else:
        print("Opção Inválida, tente novamente.")