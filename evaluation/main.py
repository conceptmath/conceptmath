import argparse
import pandas as pd
import os
from multiprocessing import Pool
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from utils.conceptid_utils import get_cate2id
from utils.match_utils import main_exam_number_correct
from utils.file_utils import *

def catelist2metric(cate_right_list,cate_cnt_list,cate2id):
    cate_metric = {}
    n = len(cate_right_list)
    for cate in cate2id:
        id = cate2id[cate]
        if id >= n: continue
        cate_metric[cate] = cate_right_list[id]/cate_cnt_list[id] if cate_cnt_list[id]!= 0 else None
    return cate_metric
def print_metric_sort(cate_metric,path_out=None):
    metric_sort_dic = {}
    metric_sort = sorted(cate_metric.items(),key = lambda item: item[1] if item[1] is not None else 0)
    for item in metric_sort:
        metric_sort_dic[item[0]] = [item[1]]
    metric_sort_dic_pd = pd.DataFrame(metric_sort_dic).T
    metric_sort_dic_pd.to_csv(path_out)
def metric2pd(cate_metric):
    res = {}
    for item in cate_metric:
        res[item] = [cate_metric[item]]
    cate_metric_pd = pd.DataFrame(res).T
    return cate_metric_pd

def main_evaluation(path_in:str,dir_out:str,grade_type:str='element_zh',model:str=None):
    # load dataset
    data = load_data(path_in)
    # prepare cate_id, acc_save_cnt
    cate2id = get_cate2id(type=grade_type) # cate2id
    cate_right_list = [0] * len(cate2id) 
    cate_cnt_list = [0] * len(cate2id)
    step,correct,cate_metric = 0,0,{}
    res,res_right,res_wrong = [],[],[]
    # evaluation
    for line in data:
        cate2,cate1,cate0 = line['cate2'],line['cate1'],line['cate0']
        question,gt,pred = line['question'],str(line['answer']),line['response']
        cate_name0 = cate0
        cate_name1 = '/'.join([cate0,cate1])
        cate_name2 = '/'.join([cate0,cate1,cate2])
        iscorrect = main_exam_number_correct(answer_str=str(gt),response_str=pred,concept_name=cate_name2)
        print('-'*60)
        print('[Step]{}'.format(step))
        print('[Concept]{}|{}|{}'.format(cate0,cate1,cate2))
        print('[Question]{}'.format(question))
        print('[Pred]{}'.format(pred))
        print('[Answer]{}'.format(gt))
        print('[IsCorrect]{}'.format(iscorrect))
        # record for concept metrics
        for cate in [cate_name2,cate_name1,cate_name0]:
            cate_id = cate2id[cate]
            cate_right_list[cate_id] += iscorrect
            cate_cnt_list[cate_id] += 1
        # record for save
        line['iscorrect'] = iscorrect
        if iscorrect: res_right.append(line)
        else: res_wrong.append(line)
        res.append(line)
        correct += iscorrect
        step += 1
    # report metric
    acc = correct/len(data)
    cate_metric = catelist2metric(cate_right_list,cate_cnt_list,cate2id)
    cate_metric['acc'] = acc
    cate_metric_pd = metric2pd(cate_metric)
    print('-'*50)
    print('[知识点得分情况]\n',cate_metric)
    print('[Overall Acc({})]{}'.format(grade_type,acc))
    print('[dir_out]',dir_out)
    assert len(data) == len(res), print(len(data),len(res))
    cate_metric_pd.to_csv(os.path.join(dir_out,f'{model}_{grade_type}_metric.csv'))
    write_data(res,      os.path.join(dir_out,f'{model}_{grade_type}_all.json'))
    write_data(res_right,os.path.join(dir_out,f'{model}_{grade_type}_right.json'))
    write_data(res_wrong,os.path.join(dir_out,f'{model}_{grade_type}_wrong.json'))
    print_metric_sort(cate_metric,os.path.join(dir_out,f'{model}_{grade_type}_msort.csv'))
    print(f'[data cnt]{len(data)}, [right cnt]{len(res_right)}, [wrong cnt]{len(res_wrong)}')
    return acc

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Language Modelling on Grade Math")
    parser.add_argument('--dir_out', default='./inference/Meta-Llama-3-70B-Instruction/', type=str)
    parser.add_argument('--path_in', default='./inference/Meta-Llama-3-70B-Instruction/middle_en.jsonl', type=str)
    parser.add_argument('--model', default='Meta-Llama-3-70B-Instruction', type=str)
    parser.add_argument('--grade', default='middle_en', type=str)
    args = parser.parse_args()

    main_evaluation(path_in= args.path_in
        ,dir_out=args.dir_out
        ,grade_type=args.grade
        ,model=args.model
        )