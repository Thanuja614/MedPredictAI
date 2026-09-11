"""
MedPredict AI — Module pharm-tdm-vancomycin Schemas
"""
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum

class Tier_78_1(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_1:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_1 = Tier_78_1.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_2(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_2:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_2 = Tier_78_2.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_3(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_3:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_3 = Tier_78_3.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_4(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_4:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_4 = Tier_78_4.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_5(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_5:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_5 = Tier_78_5.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_6(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_6:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_6 = Tier_78_6.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_7(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_7:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_7 = Tier_78_7.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_8(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_8:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_8 = Tier_78_8.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_9(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_9:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_9 = Tier_78_9.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_10(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_10:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_10 = Tier_78_10.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_11(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_11:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_11 = Tier_78_11.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_12(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_12:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_12 = Tier_78_12.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_13(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_13:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_13 = Tier_78_13.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_14(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_14:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_14 = Tier_78_14.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_15(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_15:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_15 = Tier_78_15.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_16(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_16:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_16 = Tier_78_16.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_17(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_17:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_17 = Tier_78_17.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_18(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_18:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_18 = Tier_78_18.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_19(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_19:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_19 = Tier_78_19.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }

class Tier_78_20(str, Enum):
    TIER_NORMAL = "normal"
    TIER_MILD = "mild"
    TIER_MODERATE = "moderate"
    TIER_SEVERE = "severe"
    TIER_CRITICAL = "critical"

@dataclass
class Schema_78_20:
    patient_id: str = "P_SAMPLE"
    record_epoch: int = 1773200000
    active_tier: Tier_78_20 = Tier_78_20.TIER_NORMAL
    param_1: float = 1.5
    param_2: float = 2.0
    param_3: float = 2.5
    param_4: float = 3.0
    param_5: float = 3.5
    param_6: float = 4.0
    param_7: float = 4.5
    param_8: float = 5.0
    param_9: float = 5.5
    param_10: float = 6.0
    param_11: float = 6.5
    param_12: float = 7.0
    param_13: float = 7.5
    param_14: float = 8.0
    param_15: float = 8.5
    param_16: float = 9.0
    param_17: float = 9.5
    param_18: float = 10.0
    param_19: float = 10.5
    param_20: float = 11.0
    marker_1: str = "normative"
    marker_2: str = "normative"
    marker_3: str = "normative"
    marker_4: str = "normative"
    marker_5: str = "normative"
    marker_6: str = "normative"
    marker_7: str = "normative"
    marker_8: str = "normative"
    marker_9: str = "normative"
    marker_10: str = "normative"
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient_id,
            "epoch": self.record_epoch,
            "tier": self.active_tier.value,
            "p1": self.param_1,
            "p2": self.param_2,
            "p3": self.param_3,
            "p4": self.param_4,
            "p5": self.param_5,
            "p6": self.param_6,
            "p7": self.param_7,
            "p8": self.param_8,
            "p9": self.param_9,
            "p10": self.param_10,
            "p11": self.param_11,
            "p12": self.param_12,
            "p13": self.param_13,
            "p14": self.param_14,
            "p15": self.param_15,
            "p16": self.param_16,
            "p17": self.param_17,
            "p18": self.param_18,
            "p19": self.param_19,
            "p20": self.param_20,
        }
