"""
Corporate Standard Module: external_platforms
Mock integration with generic 'outras plataformas'.
"""
import logging
from typing import List, Dict, Any

class ExternalPlatformConnector:
    """
    Conector genérico para injetar dados anonimizados de plataformas externas
    (pagamentos, contabilidade) sem citar nomes comerciais.
    """
    
    def __init__(self):
        self.platform_name = "Plataforma Externa de Pagamentos"
        self.is_connected = False
        
    def connect(self) -> bool:
        """Simula a conexão OAuth ou autenticação com a plataforma."""
        logging.info(f"Conectando com {self.platform_name}...")
        self.is_connected = True
        return self.is_connected
        
    def fetch_recent_transactions(self) -> List[Dict[str, Any]]:
        """Simula o resgate de transações webhooks ou polling."""
        if not self.is_connected:
            raise ValueError(f"Não conectado a {self.platform_name}")
            
        logging.info(f"Buscando transações de {self.platform_name}...")
        
        return [
            {
                "id": "ext_txn_1001",
                "amount": 2500.0,
                "currency": "USD",
                "counterparty_tin": "99-9999999",
                "status": "completed",
                "date": "2026-07-20T10:00:00Z"
            },
            {
                "id": "ext_txn_1002",
                "amount": 10500.0,
                "currency": "USD",
                "counterparty_tin": "88-8888888",
                "status": "pending",
                "date": "2026-07-20T10:05:00Z"
            }
        ]
