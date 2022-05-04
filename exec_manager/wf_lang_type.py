from enum import Enum


class WfLangType(Enum):
    CWL = "cwl"
    WDL = "wdl"
    NEXTFLOW = "nextflow"
    SNAKEMAKE = "snakemake"
