import argparse
import json
import pandas as pd

parser = argparse.ArgumentParser(description='''
This is a sample application to parse evaluatoin results file from OCI Langauge Custom Text Classification.
Example usage: !python3 evalres.py --evalres './evalres.json' -d './train_data.csv' --output './eval_data.csv'
''')

parser.add_argument("-e", "--evalres", help = "Evaluation Results File Path")
parser.add_argument("-d", "--datafile", help = "training dataset file path")
parser.add_argument("-o", "--output", help = "path to output file")

args = parser.parse_args()
if args.evalres is None or args.datafile is None or args.output is None:
    print('Insufficient number of arguments supplied')
    parser.print_help()

eval_res_file = args.evalres
dataset_file = args.datafile
output_file = args.output

try:
    with open(eval_res_file) as json_file:
        evaluation_results_dic = json.load(json_file)
except:
    print(f'unable load evaluation result file:{eval_res_file}')
else:
    print('loaded evaluation result file successfully.')
    try:
        test_data = pd.read_csv(dataset_file, encoding='utf-8')
    except:
        print(f'unable to load dataset file:{dataset_file}')
    else:
        print('loaded training dataset file successfully')
        locations = [i['location'] for i in evaluation_results_dic['data']['items']]
        text = [test_data.iloc[int(l)-2]['text'] for l in locations]
        predicted_labels = ["|".join(i['predicted-labels']) for i in evaluation_results_dic['data']['items'] ]
        true_labels = ["|".join(i['true-labels']) for i in evaluation_results_dic['data']['items'] ]
        try:
            pd.DataFrame({'line':locations, 'text':text, 'predicted labels':predicted_labels, 'true labels':true_labels}).to_csv(output_file, index=False)
            print(f'Successfully saved output file at {output_file}')
        except IOError as ioer:
            print(f'unable to save output file: {output_file}, error: {ioer}')
        except:
            print(f'unable to save output file: {output_file}')
