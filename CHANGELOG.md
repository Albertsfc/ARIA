# Changelog — ARIA

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

## [0.2.0] — 2026-07-20
### Adicionado
- **Motor No-Code**: Interface e agente (LLM) que traduz regras de negócios em linguagem natural para JSON estruturado.
- **Plataformas Externas**: Plugin genérico de integração que simula ingestão de dados de outras plataformas sem expor marcas registradas.
- **Correções**: Resolvidos pequenos erros de sintaxe no roteador e no módulo RAG.

## [0.1.0] — 2026-06-15
### Adicionado
- **Design System Document (SDD)**: Harness completo seguindo o padrão de 16 seções do AXIS.
- **Banco de Dados SQLite**: Schema completo com suporte a alertas, credit score, lender reports, chat e auditoria NIST.
- **Plugins Read-Only**: `afis_reader.py` e `apex_reader.py` integrados de modo seguro.
- **RAG & Underwriting Rules**: Indexador de diretrizes SBA em ChromaDB e fallback textual de busca de similaridade cosseno.
- **Skills e Sub-agentes**: Orquestração completa no LangGraph contendo monitoramento de transações, grafos de rede e cálculo de Credit Score com SHAP.
- **API FastAPI**: Endpoints de status, varredura de riscos, créditos e streaming SSE no advisor chat.
- **Frontend SPA Premium**: CSS roxo/violeta glassmorphic com suporte a todas as 10 animações obrigatórias especificadas.


