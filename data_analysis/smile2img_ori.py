import re
from rdkit import Chem
from rdkit.Chem import Draw

i = 0
n = 0
TargetFileName = "ga/demo_c_11-23.txt"
with open(TargetFileName,'r') as TempFile:
    for Line in TempFile.readlines():
        b = re.findall("\s.*\t(.*)$",Line)
        Smiles = re.sub("\s--> RX\w*_TOP\w*,", "\t", b[0]).split('\t')
        j = 0
#        print(Smiles)
        for smile in Smiles:
            mol = Chem.MolFromSmiles(smile)
            if (mol is None):
                n =+ 1
                print(n)
                break
            else:
                canonical_smi = Chem.MolToSmiles(mol)
                canonical_mol = Chem.MolFromSmiles(canonical_smi)
                Draw.MolToImageFile(canonical_mol,"ga/demo_c/mol_route{}_num_{}.jpg".format(i,j+1))
            j += 1
        i += 1