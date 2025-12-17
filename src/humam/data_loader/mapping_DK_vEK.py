"""
Mapping from the Desikan & Killiany regions
to the areas in von Economo & Koskinas
based on (Goulas et al. bioRxiv 2016, Table 1).

Returns
-------
dk_to_vEK : dict
    Mapping dictionary
"""

dk_to_vEK = {
    "bankssts": ["PH"],
    "caudalanteriorcingulate": ["LA1", "LA2"],
    "caudalmiddlefrontal": ["FC", "FB"],
    "cuneus": ["OA", "OB"],
    "entorhinal": ["HA", "HB"],
    "fusiform": ["TF"],
    "inferiorparietal": ["PG"],
    "inferiortemporal": ["TE"],
    "isthmuscingulate": ["LD", "LC2"],
    "lateraloccipital": ["OA"],
    "lateralorbitofrontal": ["FG"],
    "lingual": ["OA", "OB", "PH"],
    "medialorbitofrontal": ["FH", "FL"],
    "middletemporal": ["TE"],
    "parahippocampal": ["HC", "HD"],
    "paracentral": ["PA", "PB1", "PB2", "PC"],
    "parsopercularis": ["FCBm"],
    "parsorbitalis": ["FF"],
    "parstriangularis": ["FDt"],  # TODO Is u'FDt' really FDGamma?
    "pericalcarine": ["OC"],
    "postcentral": ["PC"],
    "posteriorcingulate": ["LC1", "LC2", "LC3"],
    "precentral": ["FA"],
    "precuneus": ["PE"],
    "rostralanteriorcingulate": ["LA1", "LA2"],
    "rostralmiddlefrontal": ["FD\u0394", "FD", "FC"],
    "superiorfrontal": ["FC", "FD", "FB"],
    "superiorparietal": ["PE"],
    "superiortemporal": ["TA"],
    "supramarginal": ["PF"],
    "frontalpole": ["FE"],
    "temporalpole": ["TG"],
    "transversetemporal": ["TC", "TD"],
    "insula": ["IA", "IB"],
}
