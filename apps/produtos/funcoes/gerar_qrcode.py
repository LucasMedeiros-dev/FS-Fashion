from PIL import Image, ImageDraw, ImageFont
import qrcode


def criar_etiqueta(nome_produto, preco, id_produto):
    # Configurações de DPI e dimensões
    dpi = 204
    mm_para_pixels = dpi / 25.4
    largura = int(34.5 * mm_para_pixels)
    altura = int(60 * mm_para_pixels)

    # Criar imagem de fundo
    etiqueta = Image.new('RGB', (largura, altura), 'white')
    draw = ImageDraw.Draw(etiqueta)

    # Configurar fontes
    fonte_marca = ImageFont.truetype("arial.ttf", int(
        6.5 * mm_para_pixels))  # Tamanho proporcional a etiqueta
    fonte_produto = ImageFont.truetype("arial.ttf", int(3 * mm_para_pixels))
    fonte_preco = ImageFont.truetype("arial.ttf", int(7.85 * mm_para_pixels))

    # Desenhar a marca no topo
    texto_marca = "FS Fashion"
    bbox_marca = draw.textbbox((0, 0), texto_marca, font=fonte_marca)
    largura_texto_marca = bbox_marca[2] - bbox_marca[0]
    draw.text(((largura - largura_texto_marca) / 2, 45),
              texto_marca, fill='black', font=fonte_marca)

    # Adicionar nome do produto
    bbox_produto = draw.textbbox((0, 0), nome_produto, font=fonte_produto)
    largura_texto_produto = bbox_produto[2] - bbox_produto[0]
    draw.text(((largura - largura_texto_produto) / 2,
              bbox_marca[3] + 45), nome_produto, fill='black', font=fonte_produto)

    # Adicionar QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=1,
    )
    qr.add_data(id_produto)
    qr.make(fit=True)
    qr_img = qr.make_image(
        fill_color="black", back_color="white").convert('RGB')

    qr_largura, qr_altura = qr_img.size
    x_qr = (largura - qr_largura) / 2
    y_qr = (altura - qr_altura) / 2
    etiqueta.paste(qr_img, (int(x_qr), int(bbox_produto[3] + 105)))

    # Adicionar preço

    preco = f"R${preco}"

    bbox_preco = draw.textbbox((0, 0), preco, font=fonte_preco)
    largura_texto_preco = bbox_preco[2] - bbox_preco[0]
    altura_texto_preco = bbox_preco[3] - bbox_preco[1]

    draw.text(((largura - largura_texto_preco) / 2, altura -
              altura_texto_preco - 55), preco, fill='black', font=fonte_preco)

    return etiqueta


def criar_etiqueta_multiplo(nome_produto, preco, id_produto):
    # Configurações de DPI e dimensões para uma única etiqueta
    dpi = 204
    mm_para_pixels = dpi / 25.4
    largura_etiqueta = int(34.5 * mm_para_pixels)
    altura_etiqueta = int(60 * mm_para_pixels)

    # Criar imagem de fundo para 3 etiquetas
    largura_total = largura_etiqueta * 3
    imagem_total = Image.new('RGB', (largura_total, altura_etiqueta), 'white')

    # Gerar 3 etiquetas e colar na imagem de fundo
    for i in range(3):
        etiqueta = criar_etiqueta(nome_produto, preco, id_produto)
        x_posicao = i * largura_etiqueta
        imagem_total.paste(etiqueta, (x_posicao, 0))

    # Salvar imagem
    imagem_total.save('etiquetas_latest.png')
