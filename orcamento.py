import csv


class OrcamentoAluguel:

    def __init__(self):
        self.tipo = ""
        self.quartos = 0
        self.valor_aluguel = 0.0
        self.parcelas = 1
        self.valor_parcela_contrato = 0.0
        self.valor_total_mensal = 0.0

    # =========================
    # VALIDAÇÕES
    # =========================

    def ler_numero_inteiro(self, mensagem, minimo=None, maximo=None):

        while True:

            try:
                numero = int(input(mensagem))

                if minimo is not None and numero < minimo:
                    print(f"Digite um número maior ou igual a {minimo}.")
                    continue

                if maximo is not None and numero > maximo:
                    print(f"Digite um número menor ou igual a {maximo}.")
                    continue

                return numero

            except ValueError:
                print("Entrada inválida! Digite apenas números.")

    def ler_sim_ou_nao(self, mensagem):

        while True:

            resposta = input(mensagem).strip().lower()

            if resposta in ["s", "n"]:
                return resposta

            print("Digite apenas 's' para sim ou 'n' para não.")

    # =========================
    # ESCOLHA DO IMÓVEL
    # =========================

    def escolher_imovel(self):

        print("=" * 40)
        print("      ORÇAMENTO DE ALUGUEL")
        print("=" * 40)

        while True:

            self.tipo = input(
                "Tipo do imóvel (apartamento/casa/estudio): "
            ).strip().lower()

            if self.tipo in ["apartamento", "casa", "estudio"]:
                break

            print("Tipo de imóvel inválido!")

    # =========================
    # CÁLCULO DO ALUGUEL
    # =========================

    def calcular_aluguel(self):

        # APARTAMENTO
        if self.tipo == "apartamento":

            self.valor_aluguel = 700

            self.quartos = self.ler_numero_inteiro(
                "Quantidade de quartos: ",
                minimo=1
            )

            if self.quartos == 2:
                self.valor_aluguel += 200

            garagem = self.ler_sim_ou_nao(
                "Deseja garagem? (s/n): "
            )

            if garagem == "s":
                self.valor_aluguel += 300

            filhos = self.ler_sim_ou_nao(
                "Possui filhos? (s/n): "
            )

            if filhos == "n":
                desconto = self.valor_aluguel * 0.05
                self.valor_aluguel -= desconto

        # CASA
        elif self.tipo == "casa":

            self.valor_aluguel = 900

            self.quartos = self.ler_numero_inteiro(
                "Quantidade de quartos: ",
                minimo=1
            )

            if self.quartos == 2:
                self.valor_aluguel += 250

            garagem = self.ler_sim_ou_nao(
                "Deseja garagem? (s/n): "
            )

            if garagem == "s":
                self.valor_aluguel += 300

        # ESTÚDIO
        elif self.tipo == "estudio":

            self.valor_aluguel = 1200

            vagas = self.ler_numero_inteiro(
                "Quantidade de vagas de estacionamento: ",
                minimo=0
            )

            if vagas >= 2:

                self.valor_aluguel += 250

                if vagas > 2:
                    self.valor_aluguel += (vagas - 2) * 60

    # =========================
    # CONTRATO
    # =========================

    def calcular_contrato(self):

        contrato = 2000

        self.parcelas = self.ler_numero_inteiro(
            "Quantidade de parcelas do contrato (1 a 5): ",
            minimo=1,
            maximo=5
        )

        self.valor_parcela_contrato = contrato / self.parcelas

        self.valor_total_mensal = (
            self.valor_aluguel + self.valor_parcela_contrato
        )

    # =========================
    # RESULTADO FINAL
    # =========================

    def mostrar_resultado(self):

        print("\n" + "=" * 40)
        print("        RESULTADO FINAL")
        print("=" * 40)

        print(f"Tipo do imóvel: {self.tipo}")

        if self.tipo != "estudio":
            print(f"Quantidade de quartos: {self.quartos}")

        print(f"Valor do aluguel: R$ {self.valor_aluguel:.2f}")

        print(
            f"Contrato parcelado em "
            f"{self.parcelas}x de "
            f"R$ {self.valor_parcela_contrato:.2f}"
        )

        print(
            f"Valor total mensal: "
            f"R$ {self.valor_total_mensal:.2f}"
        )

    # =========================
    # GERAR CSV
    # =========================

    def gerar_csv(self):

        try:

            with open(
                "orcamento.csv",
                "w",
                newline="",
                encoding="utf-8"
            ) as arquivo:

                writer = csv.writer(arquivo)

                writer.writerow(
                    [
                        "Mes",
                        "Valor Aluguel",
                        "Parcela Contrato",
                        "Total Mensal"
                    ]
                )

                for mes in range(1, 13):

                    if mes <= self.parcelas:
                        contrato_mes = self.valor_parcela_contrato
                    else:
                        contrato_mes = 0

                    total_mes = (
                        self.valor_aluguel + contrato_mes
                    )

                    writer.writerow(
                        [
                            mes,
                            f"R$ {self.valor_aluguel:.2f}",
                            f"R$ {contrato_mes:.2f}",
                            f"R$ {total_mes:.2f}"
                        ]
                    )

            print("\nArquivo 'orcamento.csv' gerado com sucesso!")

        except Exception as erro:
            print(f"Erro ao gerar CSV: {erro}")

    # =========================
    # EXECUÇÃO DO SISTEMA
    # =========================

    def executar(self):

        self.escolher_imovel()

        self.calcular_aluguel()

        self.calcular_contrato()

        self.mostrar_resultado()

        self.gerar_csv()


# =========================
# INÍCIO DO PROGRAMA
# =========================

sistema = OrcamentoAluguel()

sistema.executar()