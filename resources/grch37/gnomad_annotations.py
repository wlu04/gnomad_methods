from gnomad_hail.resources.resource_utils import TableResource


def _annotations_ht_path(data_type, annotation_type):
    """
    Get sites-level annotations

    :param str data_type: One of "exomes" or "genomes"
    :param str annotation_type: One of "vep", "qc_stats", "family_stats", "frequencies", "rf", "omes_concordance", "NA12878_concordance", "syndip_concordance", "omes_by_platform_concordance"
    :param str hail_version: One of the HAIL_VERSIONs
    :return: Path to annotations Table
    :rtype: str
    """
    return 'gs://gnomad/annotations/hail-{0}/ht/{1}/gnomad.{1}.{2}.ht'.format(data_type, annotation_type)


def vep(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'vep'))


def qc_stats(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'qc_stats'))


def family_stats(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'family_stats'))


def frequencies(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'frequencies'))


def rf(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'rf'))


def omes_concordance(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'omes_concordance'))


def NA12878_concordance(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'NA12878_concordance'))


def syndip_concordance(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'syndip_concordance'))


def omes_by_platform_concordance(data_type) -> TableResource:
    return TableResource(path=_annotations_ht_path(data_type, 'omes_by_platform_concordance'))


