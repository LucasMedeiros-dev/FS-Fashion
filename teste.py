from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Cupom de Compra', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')


def gerar_pdf_80mm(nome_loja, produtos, arquivo_saida):
    pdf = PDF(orientation='P', unit='mm', format=(80, 210))
    pdf.add_page()

    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, f'Loja: {nome_loja}', 0, 1, 'C')
    pdf.cell(
        0, 0, "-------------------------------------------------------------", 0, 1, 'C')
    for produto in produtos:
        pdf.cell(0, 10, f"{produto['nome']}: R$ {produto['preco']:.2f}", 0, 1)

    total = sum(produto['preco'] for produto in produtos)
    pdf.cell(0, 10, f'Total: R$ {total:.2f}', 0, 1)

    pdf.output(arquivo_saida)


# Exemplo de uso da função
produtos = [
    {"nome": "Produto A", "preco": 10.0},
    {"nome": "Produto B", "preco": 20.0},
    {"nome": "Produto C", "preco": 30.0}
]

gerar_pdf_80mm("Minha Loja", produtos, "nota_fiscal_80mm.pdf")
