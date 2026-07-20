"""
Corporate Standard Module: no_code_compiler
Agente responsável por traduzir regras em linguagem natural para JSON estruturado.
"""
from pydantic import BaseModel, Field
from app.llm_client import get_llm_client

class CompiledRule(BaseModel):
    condition: str = Field(description="The logical condition, e.g., '>', '<', '==', '!=', 'contains'")
    threshold_value: float = Field(description="The numeric threshold if applicable. Default to 0 if not numeric.")
    target_entity: str = Field(description="The entity to monitor, e.g., 'invoice', 'supplier_volume', 'transaction_frequency'")
    action: str = Field(description="The action to take, e.g., 'alert', 'block', 'review'")
    description: str = Field(description="A brief generated description of what this rule does")

async def compile_rule_to_json(user_input: str) -> str:
    """
    Receives a natural language rule from the user and compiles it to a structured JSON rule
    using the LLM.
    """
    llm = get_llm_client()
    system_prompt = (
        "You are an AI assistant that compiles natural language business rules into "
        "structured JSON configurations for a fraud detection and anomaly system."
    )
    
    try:
        structured_output = await llm.complete_structured(
            prompt=f"Compile this rule: {user_input}",
            system_prompt=system_prompt,
            response_model=CompiledRule
        )
        return structured_output.json()
    except Exception as e:
        # Fallback offline simplificado para fins de demonstração
        fallback_rule = CompiledRule(
            condition=">",
            threshold_value=5000.0,
            target_entity="external_platform_transaction",
            action="alert",
            description=f"Fallback rule generated from: {user_input}"
        )
        return fallback_rule.json()
