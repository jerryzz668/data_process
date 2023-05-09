import re, os
from rdkit import Chem
from rdkit.Chem import Draw
from utils import read_txt


smiles = ['Fc1cccc(F)c1CBr.NC(=O)c1c[nH]nn1', 
'COC(=O)c1cn(Cc2c(F)cccc2F)nn1', 
'N.O=C(O)c1cn(Cc2c(F)cccc2F)nn1',
'COC(=O)c1cn(Cc2c(F)cccc2F)nn1.N',
'C#CC(N)=O.[N-]=[N+]=NCc1c(F)cccc1F',
'CON(C)C(=O)c1cn(Cc2c(F)cccc2F)nn1',
'COC(OC)c1cn(Cc2c(F)cccc2F)nn1',
'CCOC(=O)c1cn(Cc2c(F)cccc2F)nn1.N',
'CON(C)C(=O)c1cn(Cc2c(F)cccc2F)nn1.N',
'CCOC(=O)c1cn(Cc2c(F)cccc2F)nn1']

output_dir = '/home/jerry/Desktop/CS_TEAM_MCTS/xxx'
for j,smile in enumerate(smiles):
        mol = Chem.MolFromSmiles(smile)
        if mol is None: # 如果当前路线中的某个化合物mol无效，则退出当前路线
            print('第{}条路线无效'.format(i+1))
            break
        else:
            canonical_smi = Chem.MolToSmiles(mol)
            canonical_mol = Chem.MolFromSmiles(canonical_smi)
            # Draw.MolToImageFile(canonical_mol, output_dir + "/mol_route{}_num_{}.jpg".format(i+1,j+1))
            Draw.MolToFile(canonical_mol, output_dir + "/num_{}.png".format(j+1), size=(600, 600), imageType='png', dpi=1200)