import re, os
from rdkit import Chem
from rdkit.Chem import Draw
from utils import read_txt

# 输入要求  1. 需要无表头，格式为    序号  分数  路线
# 输入要求  2. 不可以有空行
input_dir = "/home/jerry/Desktop/CS_TEAM_MCTS/multi_step/EA_to-be-verified/demo_d.txt"
data = read_txt(input_dir)
output_dir = input_dir.split('.')[0]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i,line in enumerate(data):
    # b = re.findall("\s.*\t(.*)$",line)  # 过滤有反应路线的行
    # smiles = re.sub("\s--> RX\w*_TOP\w*,", "\t", b[0]).split('\t')  # 转成list存储单个smile
    b = line.split('   ')[-1].replace('\n','')
    smiles = re.sub("\s--> RX\w*_TOP\w*,", "\t", b).split('\t')
    # print(smiles)
    for j,smile in enumerate(smiles):
        mol = Chem.MolFromSmiles(smile)
        if mol is None: # 如果当前路线中的某个化合物mol无效，则退出当前路线
            print('第{}条路线无效'.format(i+1))
            break
        else:
            canonical_smi = Chem.MolToSmiles(mol)
            canonical_mol = Chem.MolFromSmiles(canonical_smi)
            # Draw.MolToImageFile(canonical_mol, output_dir + "/mol_route{}_num_{}.jpg".format(i+1,j+1))
            Draw.MolToFile(canonical_mol, output_dir + "/mol_route{}_num_{}.png".format(i+1,j+1), size=(600, 600), imageType='png', dpi=1200)
