from cogdl.tasks import build_task
from cogdl.datasets import build_dataset
from cogdl.models import build_model
from cogdl.utils import build_args_from_dict

def get_default_args():
    default_dict = {'hidden_size': 64,
                    'num_shuffle': 1,
                    'cpu': True,
                    'enhance': False,
                    'save_dir': ".",}
    return build_args_from_dict(default_dict)

def test_deepwalk_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'deepwalk'
    dataset = build_dataset(args)
    args.walk_length = 10
    args.walk_num = 2
    args.window_size = 3
    args.worker = 5
    args.iteration = 2
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0


def test_line_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'line'
    dataset = build_dataset(args)
    args.walk_length = 10
    args.walk_num = 2
    args.negative = 3
    args.batch_size = 20
    args.alpha = 0.025
    args.order = 1
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0

def test_node2vec_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'node2vec'
    dataset = build_dataset(args)
    args.walk_length = 10
    args.walk_num = 2
    args.window_size = 3
    args.worker = 5
    args.iteration = 2
    args.p = 1.0
    args.q = 1.0
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0

def test_hope_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'hope'
    dataset = build_dataset(args)
    args.beta = 0.001
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0    


def test_grarep_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'grarep'
    dataset = build_dataset(args)
    args.step = 2
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0   
    
def test_netmf_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'netmf'
    dataset = build_dataset(args)
    args.window_size = 2
    args.rank = 128
    args.negative = 3
    args.is_large = False
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0  

def test_netsmf_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'netsmf'
    dataset = build_dataset(args)
    args.window_size = 3
    args.negative = 1
    args.num_round = 3
    args.worker = 5
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0  


def test_prone_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'prone'
    dataset = build_dataset(args)
    args.step = 5
    args.theta = 0.5
    args.mu = 0.2
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0

def test_sdne_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'sdne'
    dataset = build_dataset(args)
    args.hidden_size1 = 500
    args.hidden_size2 = 64
    args.droput = 0.2
    args.alpha = 0.01
    args.beta = 5
    args.nu1 = 1e-4
    args.nu2 = 1e-3
    args.max_epoch = 2
    args.lr = 0.001
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0

def test_dngr_ppi():
    args = get_default_args()
    args.task = 'unsupervised_node_classification'
    args.dataset = 'ppi'
    args.model = 'dngr'
    dataset = build_dataset(args)
    args.hidden_size1 = 500
    args.hidden_size2 = 64
    args.noise = 0.2
    args.alpha = 0.01
    args.step = 3
    args.max_epoch = 2
    args.lr = 0.001
    model = build_model(args)
    task = build_task(args)
    ret = task.train()
    assert ret['Micro-F1 0.9'] > 0
    

if __name__ == "__main__":
    test_deepwalk_ppi()
    test_line_ppi()
    test_node2vec_ppi()
    test_hope_ppi()
    test_grarep_ppi()
    test_netmf_ppi()
    test_netsmf_ppi()
    test_prone_ppi()
    test_sdne_ppi()
    test_dngr_ppi()