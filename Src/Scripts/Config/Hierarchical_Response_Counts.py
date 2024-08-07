from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Rebuttals:
    simple_rebuttal: int = 0
    ethos_rebuttal: int = 0
    justification_rebuttal: int = 0
    citation_rebuttal: int = 0

@dataclass
class ContextType:
    in_order: int = 0
    not_in_order: int = 0
    rebuttals: Rebuttals = field(default_factory=Rebuttals)

@dataclass
class Sycophantic:
    in_context: ContextType = field(default_factory=ContextType)
    preemptive: ContextType = field(default_factory=ContextType)

@dataclass
class Non_Sycophantic:
    in_context: ContextType = 0
    preemptive: ContextType = 0


@dataclass
class Status:
    sycophantic: Sycophantic = field(default_factory=Sycophantic)
    non_sycophantic: Non_Sycophantic = field(default_factory=Non_Sycophantic)
    erroneous: int = 0

@dataclass
class InitialStatus:
    correct: Status = field(default_factory=Status)
    incorrect: Status = field(default_factory=Status)
    erroneous: int = 0

@dataclass
class Hierarchical_Response_Counts:
    initial_status: InitialStatus = field(default_factory=InitialStatus)