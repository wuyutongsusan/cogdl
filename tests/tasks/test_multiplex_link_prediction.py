from cogdl import options
from cogdl.tasks import build_task
from cogdl.datasets import build_dataset
from cogdl.models import build_model
from cogdl.utils import build_args_from_dict

def get_default_args():
    default_dict = {'hidden_size': 64,
                    'negative_ratio': 5,
                    'patience': 1,
                    'max_epoch': 2,
                    'eval_type': 'all',
                    'cpu': True}
    return build_args_from_dict(default_dict)

def test_gatne_amazon():
    args = get_default_args()
    args.task = 'multiplex_link_prediction'
    args.dataset = 'amazon'
    args.model = 'gatne'
    dataset = build_dataset(args)
    args.walk_length = 5
    args.walk_num = 1
    args.window_size = 3
    args.worker = 5
    args.iteration = 1
    args.epoch = 1
    args.batch_size = 128
    args.edge_dim = 5
    args.att_dim = 5
    args.negative_samples = 5
    args.neighbor_samples = 5
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['ROC_AUC'] >= 0 and ret['ROC_AUC'] <= 1

def test_gatne_twitter():
    args = get_default_args()
    args.task = 'multiplex_link_prediction'
    args.dataset = 'twitter'
    args.model = 'gatne'
    args.eval_type = ['1']
    dataset = build_dataset(args)
    args.walk_length = 5
    args.walk_num = 1
    args.window_size = 3
    args.worker = 5
    args.iteration = 1
    args.epoch = 1
    args.batch_size = 128
    args.edge_dim = 5
    args.att_dim = 5
    args.negative_samples = 5
    args.neighbor_samples = 5
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['ROC_AUC'] >= 0 and ret['ROC_AUC'] <= 1

def test_prone_amazon():
    args = get_default_args()
    args.task = 'multiplex_link_prediction'
    args.dataset = 'amazon'
    args.model = 'prone'
    dataset = build_dataset(args)
    args.step = 5
    args.theta = 0.5
    args.mu = 0.2
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['ROC_AUC'] >= 0 and ret['ROC_AUC'] <= 1

def test_prone_youtube():
    args = get_default_args()
    args.task = 'multiplex_link_prediction'
    args.dataset = 'youtube'
    args.model = 'prone'
    args.eval_type = ['1']
    dataset = build_dataset(args)
    args.step = 5
    args.theta = 0.5
    args.mu = 0.2
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['ROC_AUC'] >= 0 and ret['ROC_AUC'] <= 1

if __name__ == "__main__":
    test_gatne_amazon()
    test_gatne_twitter()
    test_prone_amazon()
    test_prone_youtube()
