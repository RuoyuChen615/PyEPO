# PyEPO: A PyTorch-based End-to-End Predict-and-Optimize Tool

<p align="center"><img width="100%" src="images/logo1.png" /></p>

## Publication

This repository is the official implementation of the paper:
[PyEPO: A PyTorch-based End-to-End Predict-then-Optimize Library for Linear and Integer Programming](http://www.optimization-online.org/DB_HTML/2022/06/8949.html)

Citation:
```
@article{tang2022pyepo,
  title={PyEPO: A PyTorch-based End-to-End Predict-then-Optimize Library for Linear and Integer Programming},
  author={Tang, Bo and Khalil, Elias B},
  journal={arXiv preprint arXiv:2206.14234},
  year={2022}
}
```


## Introduction

``PyEPO`` (PyTorch-based End-to-End Predict-and-Optimize Tool) is a Python-based, open-source software that supports modeling and solving predict-and-optimize problems with the linear objective function. The core capability of ``PyEPO`` is to build optimization models with [GurobiPy](https://www.gurobi.com/), [Pyomo](http://www.pyomo.org/), or any other solvers and algorithms, then embed the optimization model into an artificial neural network for the end-to-end training. For this purpose, ``PyEPO`` implements SPO+ loss [[1]](https://doi.org/10.1287/mnsc.2020.3922) and differentiable Black-Box optimizer [[3]](https://arxiv.org/abs/1912.02175) as [PyTorch](https://pytorch.org/) autograd functions.


## Documentation

The official ``PyEPO`` docs can be found at [https://khalil-research.github.io/PyEPO](https://khalil-research.github.io/PyEPO).


## Learning Framework

<p align="center"><img width="100%" src="images/learning_framework_e2e.png" /></p>


## Features

- Implement SPO+ [[1]](https://doi.org/10.1287/mnsc.2020.3922) and DBB [[3]](https://arxiv.org/abs/1912.02175)
- Support [Gurobi](https://www.gurobi.com/) and [Pyomo](http://www.pyomo.org/) API
- Support Parallel computing for optimization solver
- Support solution caching [[4]](https://arxiv.org/abs/2011.05354) to speed up training

## Installation

You can download ``PyEPO`` from our GitHub repository.

```bash
git clone --branch MPC https://github.com/khalil-research/PyEPO.git
```

And install it.

```bash
pip3 install PyEPO/pkg/.
```


## Dependencies

* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)
* [Pathos](https://pathos.readthedocs.io/)
* [tqdm](https://tqdm.github.io/)
* [Pyomo](http://www.pyomo.org/)
* [Gurobi](https://www.gurobi.com/)
* [Scikit Learn](https://scikit-learn.org/)
* [Auto-Sklearn](https://www.automl.org/automl/auto-sklearn/)
* [PyTorch](http://pytorch.org/)
* [SciencePlots](https://pypi.org/project/SciencePlots/)
* [tol-colors](https://pypi.org/project/tol-colors/)


## Experiments Instruction

For all experiments, all hyperparameters for training (epoch, learning rate, batch size, etc.) are fixed in "./config/*"

However, You can run `pipeline.py` for different experiment setting (including hyperparameters).

```bash
python3 pipeline.py --prob sp --mthd spo --lan gurobi --data 1000 --deg 2 --noise 0.5 --epoch 20 --lr 1e-1 --batch 32 --optm adam --proc 1
```

**Warning**: In the original paper, experiments were completed with multiple processors, while these experiments are based on a single CPU.

### Performance Comparison (Figure 5-7)

To draw performance comparison graphs, you need to train and evaluate linear regression, random forest, automl, SPO+, and DBB with varying training data size in {100, 1000, 5000}, polynomial degree in {1, 2, 4, 6}, and noise half-width in {0.0, 0.5}.

Experiments for shortest path:

```bash
python3 experiments.py --prob sp  --mthd lr    --expnum 10
python3 experiments.py --prob sp  --mthd rf    --expnum 10
python3 experiments.py --prob sp  --mthd spo   --expnum 10
python3 experiments.py --prob sp  --mthd dbb   --expnum 10
```

The argument `expnum` is the number of experiments repeated with different data randomization. For example, in the original paper, `expnum` is 10. Therefore, you can use less repetition to save time.

**Warning:** The two-stage automated model selection and hyperparameters tuning depends on [Auto-Sklearn](https://www.automl.org/automl/auto-sklearn/), which is time-consuming. In addition, automl training requires a time limit (150 sec), so the results may be very different from the paper because of the resource allocations.

Experiments of automl for shortest path is ***optional***:

```bash
python3 experiments.py --prob sp  --mthd auto  --expnum 10
```

Once the results of the experiments are ready, you can draw a plot for Figure 5. This figure will be saved to "./images/*"

```bash
python3 plot.py --plot cmp --prob sp
```

Similarly, the comparison of 2D knapsack (Figure 6) and TSP (Figure 7) can be plotted as follows:

```bash
python3 experiments.py --prob ks  --mthd lr    --expnum 10
python3 experiments.py --prob ks  --mthd rf    --expnum 10
python3 experiments.py --prob ks  --mthd spo   --expnum 10
python3 experiments.py --prob ks  --mthd dbb   --expnum 10
# python3 experiments.py --prob ks  --mthd auto  --expnum 10
python3 plot.py --plot cmp --prob ks
```

```bash
python3 experiments.py --prob tsp --mthd lr    --expnum 10
python3 experiments.py --prob tsp --mthd rf    --expnum 10
python3 experiments.py --prob tsp --mthd spo   --expnum 10
python3 experiments.py --prob tsp --mthd dbb   --expnum 10
# python3 experiments.py --prob ks  --mthd auto  --expnum 10
python3 plot.py --plot cmp --prob tsp
```


### Relaxation (Figure 8-10)

To draw performance comparison graphs with relaxation, you need to additional train and evaluate SPO+ and DBB with linear relaxation for 2D knapsack and TSP. And TSP has different formulations.

Experiments for 2D knapsack with relaxation:
```bash
python3 experiments.py --prob ks  --mthd spo   --expnum 10 --rel
python3 experiments.py --prob ks  --mthd dbb   --expnum 10 --rel
```

Experiments for TSP with relaxation (Miller-Tucker-Zemlin):
```bash
python3 experiments.py --prob tsp --mthd spo   --expnum 10 --rel --tspform mtz
python3 experiments.py --prob tsp --mthd dbb   --expnum 10 --rel --tspform mtz
```

Experiments for TSP with relaxation (Miller-Tucker-Zemlin):
```bash
python3 experiments.py --prob tsp --mthd spo   --expnum 10 --rel --tspform mtz
python3 experiments.py --prob tsp --mthd dbb   --expnum 10 --rel --tspform mtz
```

Experiments for TSP with relaxation (Gavish–Graves):
```bash
python3 experiments.py --prob tsp --mthd spo   --expnum 10 --rel --tspform gg
python3 experiments.py --prob tsp --mthd dbb   --expnum 10 --rel --tspform gg
```

Once the results of the experiments are ready, you can draw a plot for Figure 8-10:

```bash
# 2D knapsack
python3 plot.py --plot rel  --prob ks
# TSP
python3 plot.py --plot rel  --prob tsp
```


### Regularization (Figure 11)

To draw performance comparison graphs with regularization, you need to additional train and evaluate SPO+ and DBB with L1/L2 regularization of cost. In our paper, the regularization parameter is 0.001.

Experiments for L1 regularization:

```bash
# shortest path
python3 experiments.py --prob sp  --mthd spo   --expnum 10 --l1
python3 experiments.py --prob sp  --mthd dbb   --expnum 10 --l1
# 2D knapsack
python3 experiments.py --prob ks  --mthd spo   --expnum 10 --l1
python3 experiments.py --prob ks  --mthd dbb   --expnum 10 --l1
# TSP
python3 experiments.py --prob tsp --mthd spo   --expnum 10 --l1
python3 experiments.py --prob tsp --mthd dbb   --expnum 10 --l1
```

Experiments for L2 regularization:

```bash
# shortest path
python3 experiments.py --prob sp  --mthd spo   --expnum 10 --l2
python3 experiments.py --prob sp  --mthd dbb   --expnum 10 --l2
# 2D knapsack
python3 experiments.py --prob ks  --mthd spo   --expnum 10 --l2
python3 experiments.py --prob ks  --mthd dbb   --expnum 10 --l2
# TSP
python3 experiments.py --prob tsp --mthd spo   --expnum 10 --l2
python3 experiments.py --prob tsp --mthd dbb   --expnum 10 --l2
```

Once the results of the experiments are ready, you can draw a plot for Figure 11:

```bash
# shortest path
python3 plot.py --plot reg  --prob sp
# 2D knapsack
python3 plot.py --plot reg  --prob ks
# TSP
python3 plot.py --plot reg  --prob tsp
```

### MSE-Regret Trade-off (Figure 15)

To examine the MSE-regret trade-off among all above methods, you can draw a plot for Figure 15:

```bash
# shortest path
python3 plot.py --plot trd  --prob sp
# 2D knapsack
python3 plot.py --plot trd  --prob ks
# TSP
python3 plot.py --plot trd  --prob tsp
```


### Training Scalability (Figure 16,17)

To see the effect of increasing decision variables and/or constraints, you can change the size of the graph for the shortest path and the number of constraints for the knapsack.

Experiments for the shortest path with 8x8 grid network:

```bash
python3 experiments.py --prob sp  --mthd lr    --expnum 10 --spgrid 8 8
python3 experiments.py --prob sp  --mthd rf    --expnum 10 --spgrid 8 8
python3 experiments.py --prob sp  --mthd spo   --expnum 10 --spgrid 8 8
python3 experiments.py --prob sp  --mthd dbb   --expnum 10 --spgrid 8 8
```

Experiments for the shortest path with 10x10 grid network:

```bash
python3 experiments.py --prob sp  --mthd lr    --expnum 10 --spgrid 10 10
python3 experiments.py --prob sp  --mthd rf    --expnum 10 --spgrid 10 10
python3 experiments.py --prob sp  --mthd spo   --expnum 10 --spgrid 10 10
python3 experiments.py --prob sp  --mthd dbb   --expnum 10 --spgrid 10 10
```

Experiments for the shortest path with 12x12 grid network:

```bash
python3 experiments.py --prob sp  --mthd lr    --expnum 10 --spgrid 12 12
python3 experiments.py --prob sp  --mthd rf    --expnum 10 --spgrid 12 12
python3 experiments.py --prob sp  --mthd spo   --expnum 10 --spgrid 12 12
python3 experiments.py --prob sp  --mthd dbb   --expnum 10 --spgrid 12 12
```

Experiments for the shortest path with 15x15 grid network:

```bash
python3 experiments.py --prob sp  --mthd lr    --expnum 10 --spgrid 15 15
python3 experiments.py --prob sp  --mthd rf    --expnum 10 --spgrid 15 15
python3 experiments.py --prob sp  --mthd spo   --expnum 10 --spgrid 15 15
python3 experiments.py --prob sp  --mthd dbb   --expnum 10 --spgrid 15 15
```

Once the results of the experiments are ready, you can draw a plot for Figure 16:

```bash
# shortest path
python3 plot.py --plot scl --prob sp
```

Similarly, the experiments of 1D and 3D knapsack can be run as follows:

```bash
# 1D knapsack
python3 experiments.py --prob ks  --mthd lr    --expnum 10 --ksdim 1
python3 experiments.py --prob ks  --mthd rf    --expnum 10 --ksdim 1
python3 experiments.py --prob ks  --mthd spo   --expnum 10 --ksdim 1
python3 experiments.py --prob ks  --mthd dbb   --expnum 10 --ksdim 1
# 2D knapsack
python3 experiments.py --prob ks  --mthd lr    --expnum 10 --ksdim 2
python3 experiments.py --prob ks  --mthd rf    --expnum 10 --ksdim 2
python3 experiments.py --prob ks  --mthd spo   --expnum 10 --ksdim 2
python3 experiments.py --prob ks  --mthd dbb   --expnum 10 --ksdim 2
```

Once the results of the experiments are ready, you can draw a plot for Figure 17:

```bash
# shortest path
python3 plot.py --plot scl --prob ks
```
