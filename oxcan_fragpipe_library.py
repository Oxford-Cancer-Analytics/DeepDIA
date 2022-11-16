import pandas as pd
import json

df = pd.read_csv("library.tsv", sep="\t")


json_result = []
for peptide in df.PeptideSequence.unique():
    print(peptide)

    peptide_df = df[df.PeptideSequence == peptide]

    ions = {
        "b1": [0]*(len(peptide)-1),
        "b2": [0]*(len(peptide)-1),
        "bn1": [0]*(len(peptide)-1),
        "bn2": [0]*(len(peptide)-1),
        "bo1": [0]*(len(peptide)-1),
        "bo2": [0]*(len(peptide)-1),
        "y1": [0]*(len(peptide)-1),
        "y2": [0]*(len(peptide)-1),
        "yn1":[0]*(len(peptide)-1),
        "yn2": [0]*(len(peptide)-1),
        "yo1": [0]*(len(peptide)-1),
        "yo2": [0]*(len(peptide)-1),
    }

    for charge in peptide_df.FragmentCharge.unique():
        if charge <= 2:  # up to charge 2 only
            for i,r in peptide_df.iterrows():
                if type(r.FragmentLossType)==float:  # is nan?
                    loss = ''
                else:
                    loss = r.FragmentLossType
                row_key = f"{r.FragmentType}{loss}{charge}"
                ions[row_key][r.FragmentSeriesNumber-1]=r.LibraryIntensity
        

        json_result.append({"peptide": peptide, "charge": int(charge), "ions": ions})

# format
# [{"peptide":"TFSHELSDFGLESTAGEIPVVAIR","charge":2,"score":535.37,"assigned":0.3,"ions":{"b1":[],"b2":[],"bn1":[],"bn2":[],"bo1":[],"bo2":[],"y1":[],"y2":[],"yn1":[],"yn2":[],"yo1":[],"yo2":[]},

with open("pm_lc_toronto_22.charge2.ions.json", "w") as f:
    json.dump(json_result, f)



print("done")