"""enum for workflow languagae type"""

from enum import Enum


class WfLangType(Enum):
    """enumerate workflow language types"""

    CWL = "cwl"
    """cwl language"""

    WDL = "wdl"
    """wdl language"""

    NEXTFLOW = "nextflow"
    """nextflow  language"""

    SNAKEMAKE = "snakemake"
    """snakemake language"""
