# Welcome
This repo contains some of the samples for exploring NLP.
## Converting evaluation result json into csv file
OCI Language custom models stores evaluation result in a json, which can be retrieved through command in OCI Cloudshell

```bash
oci ai language evaluation-result list --all --model-id __MODEL_OCID_HERE__ >evalres.json
```

Since json is diffifult to read for humans, issue below command to convert json  into a csv
Please note the script only supports custom text classification
```bash
python3 evalres.py --evalres './evalres.json' -d './train_data.csv' --output './eval_data.csv'
```

## Running inferences through batch API for custom text classification model
Please refer to  [Calling Custom Classification API in OCI Language](batch-txtc-inference-produce-confusion-matricx.ipynb)
