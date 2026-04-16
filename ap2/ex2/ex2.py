# 1) Crie dois doublés de teste (a sua escolha) de preferência de um projeto que
# esteja fazendo, com as classes e a execução do teste, print os resultados
# também.

"""
Exercício 1 - Dublês de Teste
Projeto: Sistema de Pedidos (e-commerce simplificado)

Dublê 1 → STUB  : simula o gateway de pagamento (retorna resposta pronta)
Dublê 2 → MOCK  : verifica se o serviço de e-mail foi chamado corretamente
"""

import unittest
from unittest.mock import MagicMock, patch


# ═══════════════════════════════════════════════════════════════════════════════
#  CÓDIGO DE PRODUÇÃO  (classes reais do projeto)
# ═══════════════════════════════════════════════════════════════════════════════

class GatewayPagamento:
    """Integração real com a API externa de pagamento (Stripe, PagSeguro, etc.)."""
    def processar(self, valor: float, cartao: str) -> dict:
      
        raise NotImplementedError("Chamada real ao gateway externo.")


class ServicoEmail:
    """Serviço real de envio de e-mail (SendGrid, SES, etc.)."""
    def enviar(self, destinatario: str, assunto: str, corpo: str) -> None:
        raise NotImplementedError("Envio real de e-mail.")


class ProcessadorPedido:
    """Orquestra o pagamento e a notificação ao cliente."""

    def __init__(self, gateway: GatewayPagamento, email: ServicoEmail):
        self.gateway = gateway
        self.email   = email

    def finalizar(self, valor: float, cartao: str, cliente_email: str) -> str:
        resultado = self.gateway.processar(valor, cartao)

        if resultado.get("status") == "aprovado":
            self.email.enviar(
                destinatario=cliente_email,
                assunto="Pedido confirmado!",
                corpo=f"Seu pagamento de R$ {valor:.2f} foi aprovado.",
            )
            return "pedido_confirmado"

        self.email.enviar(
            destinatario=cliente_email,
            assunto="Falha no pagamento",
            corpo="Não foi possível processar seu pagamento.",
        )
        return "pagamento_recusado"


# ═══════════════════════════════════════════════════════════════════════════════
#  DUBLÊ 1 — STUB do GatewayPagamento
#  Objetivo: substituir a chamada HTTP real; retornar respostas controladas.
# ═══════════════════════════════════════════════════════════════════════════════

class StubGatewayAprovado(GatewayPagamento):
    """Stub que SEMPRE aprova o pagamento."""
    def processar(self, valor: float, cartao: str) -> dict:
        return {"status": "aprovado", "codigo": "TXN-STUB-001"}


class StubGatewayRecusado(GatewayPagamento):
    """Stub que SEMPRE recusa o pagamento."""
    def processar(self, valor: float, cartao: str) -> dict:
        return {"status": "recusado", "motivo": "saldo insuficiente"}


# ═══════════════════════════════════════════════════════════════════════════════
#  TESTES
# ═══════════════════════════════════════════════════════════════════════════════

class TestProcessadorPedido(unittest.TestCase):

    # ── Testes com STUB ───────────────────────────────────────────────────────

    def test_stub_pagamento_aprovado_retorna_confirmado(self):
        """
        STUB: gateway retorna 'aprovado' →
        ProcessadorPedido deve retornar 'pedido_confirmado'.
        """
        stub_gateway = StubGatewayAprovado()
        mock_email   = MagicMock(spec=ServicoEmail)   # email ainda como Mock

        processador = ProcessadorPedido(stub_gateway, mock_email)
        resultado   = processador.finalizar(150.0, "4111111111111111", "a@b.com")

        self.assertEqual(resultado, "pedido_confirmado")
        print("\n[STUB - aprovado] resultado:", resultado, "✓")

    def test_stub_pagamento_recusado_retorna_recusado(self):
        """
        STUB: gateway retorna 'recusado' →
        ProcessadorPedido deve retornar 'pagamento_recusado'.
        """
        stub_gateway = StubGatewayRecusado()
        mock_email   = MagicMock(spec=ServicoEmail)

        processador = ProcessadorPedido(stub_gateway, mock_email)
        resultado   = processador.finalizar(150.0, "4111111111111111", "a@b.com")

        self.assertEqual(resultado, "pagamento_recusado")
        print("[STUB - recusado] resultado:", resultado, "✓")

    # ── Testes com MOCK ───────────────────────────────────────────────────────

    def test_mock_email_confirmacao_enviado_com_dados_corretos(self):
        """
        MOCK: verifica se ServicoEmail.enviar() foi chamado
        com o destinatário e assunto corretos após pagamento aprovado.
        """
        stub_gateway = StubGatewayAprovado()
        mock_email   = MagicMock(spec=ServicoEmail)

        processador = ProcessadorPedido(stub_gateway, mock_email)
        processador.finalizar(200.0, "4111111111111111", "cliente@email.com")

        # Verifica que enviar() foi chamado exatamente 1 vez
        mock_email.enviar.assert_called_once()

        # Verifica os argumentos passados
        args = mock_email.enviar.call_args
        self.assertEqual(args.kwargs["destinatario"], "cliente@email.com")
        self.assertEqual(args.kwargs["assunto"],      "Pedido confirmado!")
        self.assertIn("200.00", args.kwargs["corpo"])

        print("\n[MOCK - e-mail aprovado]")
        print("  → enviar() chamado:", mock_email.enviar.call_count, "vez(es)")
        print("  → destinatário    :", args.kwargs["destinatario"])
        print("  → assunto         :", args.kwargs["assunto"])
        print("  → corpo           :", args.kwargs["corpo"], "✓")

    def test_mock_email_falha_enviado_com_assunto_correto(self):
        """
        MOCK: verifica se o e-mail de FALHA é enviado com o assunto correto
        quando o pagamento é recusado.
        """
        stub_gateway = StubGatewayRecusado()
        mock_email   = MagicMock(spec=ServicoEmail)

        processador = ProcessadorPedido(stub_gateway, mock_email)
        processador.finalizar(200.0, "4111111111111111", "cliente@email.com")

        mock_email.enviar.assert_called_once()

        args = mock_email.enviar.call_args
        self.assertEqual(args.kwargs["assunto"], "Falha no pagamento")

        print("\n[MOCK - e-mail recusado]")
        print("  → enviar() chamado:", mock_email.enviar.call_count, "vez(es)")
        print("  → assunto         :", args.kwargs["assunto"], "✓")

    def test_mock_email_nao_chamado_sem_finalizar(self):
        """
        MOCK: garante que nenhum e-mail é enviado se finalizar() nunca
        for chamado — cobre o caso de uso incorreto da classe.
        """
        mock_email = MagicMock(spec=ServicoEmail)

        # Apenas instancia, não chama finalizar()
        ProcessadorPedido(StubGatewayAprovado(), mock_email)

        mock_email.enviar.assert_not_called()
        print("\n[MOCK - sem chamada] enviar() não foi invocado ✓")


# ═══════════════════════════════════════════════════════════════════════════════
#  PONTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  Dublês de Teste — Stub & Mock")
    print("  Projeto: Sistema de Pedidos")
    print("=" * 60)
    unittest.main(verbosity=2)