from rdkit import Chem
import itertools
mol = Chem.MolFromSmiles('c1ccc(Cn2ccnn2)cc1')  # CCCC1CCCCC1-C2CCCCC2CCC

patt = Chem.MolFromSmarts('[!R][!R,R]')  # 断键规则
all_bond_idx = []
for bond in mol.GetBonds():  # 遍历所有非环上的键
    if not bond.IsInRing():
        all_bond_idx.append(bond.GetIdx())
# all_match_idx = mol.GetSubstructMatches(patt)

# all_bond_idx = [mol.GetBondBetweenAtoms(*l).GetIdx() for l in all_match_idx]
for i in range(1,len(all_bond_idx)):
    cut_bs_total = list(itertools.combinations(all_bond_idx,i))
    for cs in cut_bs_total:
        print(cs)
        cs = list(set(cs))
        all_fff = Chem.FragmentOnBonds(mol,cs, addDummies=False)
        all_fragment_mol = Chem.GetMolFrags(all_fff, asMols=True)
        all_fragment_smiles = [Chem.MolToSmiles(m) for m in all_fragment_mol]
        print(all_fragment_smiles)