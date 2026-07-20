"""
Corporate Standard Module: rules (API)
API endpoints for No-Code Rule Engine.
"""
import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.db_manager import get_db
from app.agents.no_code_compiler import compile_rule_to_json

router = APIRouter(prefix="/rules", tags=["rules"])

class RuleCreate(BaseModel):
    rule_text: str

class RuleResponse(BaseModel):
    id: int
    rule_text: str
    compiled_json: dict
    is_active: bool

@router.post("/compile", response_model=RuleResponse)
async def compile_and_save_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    """
    Recebe uma regra em linguagem natural, compila via LLM, salva e retorna.
    """
    try:
        compiled_json_str = await compile_rule_to_json(rule.rule_text)
        
        insert_query = text(
            "INSERT INTO custom_rules (rule_text, compiled_json, is_active) "
            "VALUES (:rule_text, :compiled_json, 1)"
        )
        result = db.execute(insert_query, {"rule_text": rule.rule_text, "compiled_json": compiled_json_str})
        db.commit()
        
        rule_id = result.lastrowid
        
        return RuleResponse(
            id=rule_id,
            rule_text=rule.rule_text,
            compiled_json=json.loads(compiled_json_str),
            is_active=True
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=list[RuleResponse])
def get_rules(db: Session = Depends(get_db)):
    """
    Retorna todas as regras no-code ativas.
    """
    query = text("SELECT id, rule_text, compiled_json, is_active FROM custom_rules WHERE is_active = 1")
    results = db.execute(query).fetchall()
    
    rules = []
    for row in results:
        rules.append(RuleResponse(
            id=row[0],
            rule_text=row[1],
            compiled_json=json.loads(row[2]),
            is_active=bool(row[3])
        ))
    return rules
