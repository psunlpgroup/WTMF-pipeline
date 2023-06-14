from scipy.stats import pearsonr as pearson
import sys

gs_path = sys.argv[1]
sys_path = sys.argv[2]


def convertSC(file):
    lines = open(file).readlines()
    nums = list(map(float, lines))
    return nums


gs = convertSC(gs_path)
preds = convertSC(sys_path)
if len(gs) != len(preds):
    print("ERROR: Grould truth number of lines not match with prediction")

sc, alpha = pearson(gs, preds)
print("Pearson Correlation: {} with alpha {}".format(sc, alpha))


