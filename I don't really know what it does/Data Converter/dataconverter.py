import os
import sys
import argparse
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import FastICA
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import SparsePCA
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.decomposition import DictionaryLearning
from sklearn.decomposition import NMF


def read_data(file_name):

    if not os.path.exists(file_name):
        print("file not found: {}".format(file_name))

    df = pd.read_csv(file_name)

    return df


def write_data(df, file_name):

    if not os.path.exists(file_name):
        print("file not found: {}".format(file_name))

    df.to_csv(file_name, index=False)

    return df


def convert_label(df, cols):

    for col in cols:

        le = LabelEncoder()

        df[col] = le.fit_transform(df[col])

    return df


def convert_onehot(df, cols):

    for col in cols:

        ohe = OneHotEncoder()

        df[col] = ohe.fit_transform(df[col])

    return df


def convert_standardize(df, cols):

    for col in cols:

        sc = StandardScaler()

        df[col] = sc.fit_transform(df[col])

    return df


def convert_minmax(df, cols):

    for col in cols:

        mm = MinMaxScaler()

        df[col] = mm.fit_transform(df[col])

    return df


def convert_robust(df, cols):

    for col in cols:

        rs = RobustScaler()

        df[col] = rs.fit_transform(df[col])

    return df


def convert_normalize(df, cols):

    for col in cols:

        nm = Normalizer()

        df[col] = nm.fit_transform(df[col])

    return df


def convert_binarize(df, cols):

    for col in cols:

        bn = Binarizer()

        df[col] = bn.fit_transform(df[col])

    return df


def convert_pca(df, cols):

    pca = PCA()

    df[cols] = pca.fit_transform(df[cols])

    return df


def convert_tsvd(df, cols):

    tsvd = TruncatedSVD()

    df[cols] = tsvd.fit_transform(df[cols])

    return df


def convert_ica(df, cols):

    ica = FastICA()

    df[cols] = ica.fit_transform(df[cols])

    return df


def convert_fa(df, cols):

    fa = FactorAnalysis()

    df[cols] = fa.fit_transform(df[cols])

    return df


def convert_spca(df, cols):

    spca = SparsePCA()

    df[cols] = spca.fit_transform(df[cols])

    return df


def convert_kpca(df, cols):

    kpca = KernelPCA()

    df[cols] = kpca.fit_transform(df[cols])

    return df


def convert_mbdl(df, cols):

    mbdl = MiniBatchDictionaryLearning()

    df[cols] = mbdl.fit_transform(df[cols])

    return df


def convert_dl(df, cols):

    dl = DictionaryLearning()

    df[cols] = dl.fit_transform(df[cols])

    return df


def convert_nmf(df, cols):

    nmf = NMF()

    df[cols] = nmf.fit_transform(df[cols])

    return df


def main():

    parser = argparse.ArgumentParser(description="data converter")

    parser.add_argument("--input", "-i", type=str, default="", help="input file")
    parser.add_argument("--output", "-o", type=str, default="", help="output file")
    parser.add_argument("--label", "-l", type=str, default="", help="label column")
    parser.add_argument("--id", "-id", type=str, default="", help="id column")
    parser.add_argument("--convert", "-c", type=str, default="standardize", help="convert method")
    parser.add_argument("--columns", "-cols", type=str, default="all", help="convert columns")

    args = parser.parse_args()

    if args.input == "":
        print("input file not found")
        sys.exit(1)

    if args.output == "":
        print("output file not found")
        sys.exit(1)

    if args.convert == "":
        print("convert method not found")
        sys.exit(1)

    df = read_data(args.input)

    if args.label != "":

        label = df[args.label]

        df = df.drop([args.label], axis=1)

    if args.id != "":

        id = df[args.id]

        df = df.drop([args.id], axis=1)

    if args.columns == "all":

        cols = list(df)

    else:

        cols = args.columns.split(",")

    if args.convert == "label":

        df = convert_label(df, cols)

    elif args.convert == "onehot":

        df = convert_onehot(df, cols)

    elif args.convert == "standardize":

        df = convert_standardize(df, cols)

    elif args.convert == "minmax":

        df = convert_minmax(df, cols)

    elif args.convert == "robust":

        df = convert_robust(df, cols)

    elif args.convert == "normalize":

        df = convert_normalize(df, cols)

    elif args.convert == "binarize":

        df = convert_binarize(df, cols)

    elif args.convert == "pca":

        df = convert_pca(df, cols)

    elif args.convert == "tsvd":

        df = convert_tsvd(df, cols)

    elif args.convert == "ica":

        df = convert_ica(df, cols)

    elif args.convert == "fa":

        df = convert_fa(df, cols)

    elif args.convert == "spca":

        df = convert_spca(df, cols)

    elif args.convert == "kpca":

        df = convert_kpca(df, cols)

    elif args.convert == "mbdl":

        df = convert_mbdl(df, cols)

    elif args.convert == "dl":

        df = convert_dl(df, cols)

    elif args.convert == "nmf":

        df = convert_nmf(df, cols)
    
    else:
        
        print("unknown method: {}".format(args.convert))
        
        sys.exit(1)
 
    if args.label != "":

        df[args.label] = label

    if args.id != "":

        df[args.id] = id

    write_data(df, args.output)


if __name__ == "__main__":

    main()