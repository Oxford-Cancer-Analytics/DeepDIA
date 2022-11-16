# predict
python src/predict_ms2.py --in data/peptides/Pan_human_charge2.peptide.csv --model data/models/charge2/epoch_035.hdf5 --charge 2 --out data/Pan_human_charge2.prediction.ions.json
python src/predict_ms2.py --in data/peptides/Pan_human_charge3.peptide.csv --model data/models/charge3/epoch_034.hdf5 --charge 3 --out data/Pan_human_charge3.prediction.ions.json
python src/predict_rt.py --in data/peptides/Pan_human.peptide.csv --model data/models/irt/epoch_082.hdf5 --out data/Pan_human.prediction.irt.csv
# generate library
python src/build_assays_from_prediction.py --peptide data/peptides/Pan_human.peptide.csv --ions data/Pan_human_charge2.prediction.ions.json data/Pan_human_charge3.prediction.ions.json --rt data/Pan_human.prediction.irt.csv --out data/Pan_human.prediction.assay.pickle
# convert to spectro and diann
python src/convert_assays_to_Spectronaut_library.py --in data/Pan_human.prediction.assay.pickle --out data/Pan_human.prediction.library.xls