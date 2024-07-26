from dataclasses import dataclass
from typing import Optional, Union, List, Dict, Any

@dataclass
class SycophanticPrompt:
    question: Optional[str]
    answer: Optional[str] = None
    status: Optional[int] = None

@dataclass
class SycophanticPromptChainConfig:
    category: str
    sub_category: Optional[str] = None
    sub_sub_category: Optional[str] = None
    general_inquiry: Optional[SycophanticPrompt]
    simple_rebuttal: Optional[SycophanticPrompt] = None
    ethos_rebuttal: Optional[SycophanticPrompt] = None
    justification_rebuttal: Optional[SycophanticPrompt] = None
    citation_rebuttal: Optional[SycophanticPrompt] = None
    preemptive_simple_rebuttal: Optional[SycophanticPrompt] = None
    preemptive_ethos_rebuttal: Optional[SycophanticPrompt] = None
    preemptive_justification_rebuttal: Optional[SycophanticPrompt] = None
    preemptive_citation_rebuttal: Optional[SycophanticPrompt] = None
