#!/usr/bin/env python
# coding: utf-8
"""
Knapsack configuration
"""

from copy import deepcopy
from types import SimpleNamespace

# init configs
config = SimpleNamespace()
configKS = {}


### ========================= general setting =========================
## optimization model configuration
# problem type
config.prob = "ks"
# number of items
config.item = 32
# dimension
config.dim = 2
# capacity
config.cap = 20

## experiments configuration
# number of experiments
config.expnum = None
# seed
config.seed = 135
# relaxation
config.rel = False
# path to save result
config.path="./res"

## solver configuration
# modelling language
config.lan = "gurobi"
# solver for Pyomo
#config.solver = "gurobi"

## data configuration
# training data size
config.data = None
# feature size
config.feat = 5
# features polynomial degree
config.deg = None
# noise half-width
config.noise = None


### ========================= lr =========================
config_lr = deepcopy(config)

## experiments configuration
# method
config_lr.mthd = "2s"
# predictor
config_lr.pred = "lr"

configKS["lr"] = config_lr

### ========================= rf =========================
config_rf = deepcopy(config)

## experiments configuration
# method
config_rf.mthd = "2s"
# predictor
config_rf.pred = "rf"

configKS["rf"] = config_rf

### ========================= auto =========================
config_auto = deepcopy(config)

## experiments configuration
# method
config_auto.mthd = "2s"
# predictor
config_auto.pred = "auto"
# metric
config_auto.metric = "mse"

configKS["auto"] = config_auto

### ========================= SPO =========================
config_spo = deepcopy(config)

## experiments configuration
# method
config_spo.mthd = "spo"

## training configuration
# size of neural network hidden layers
config_spo.net = []
# number of epochs
config_spo.batch = 32
# number of epochs
config_spo.epoch = None
# optimizer neural network
config_spo.optm = "adam"
# learning rate
config_spo.lr = 1e-2
# l1 regularization parameter
config_spo.l1 = 0.0
# l2 regularization parameter
config_spo.l2 = 0.0
# number of processor for optimization
config_spo.proc = 1

configKS["spo"] = config_spo


### ======================== DBB =========================
config_dbb = deepcopy(config)

## experiments configuration
# method
config_dbb.mthd = "dbb"
# loss
config_dbb.loss = "r"

## training configuration
# size of neural network hidden layers
config_dbb.net = []
# number of epochs
config_dbb.batch = 32
# number of epochs
config_dbb.epoch = None
# optimizer neural network
config_dbb.optm = "adam"
# learning rate
config_dbb.lr = 1e-1
# smoothing parameter for Black-Box
config_dbb.smth = 10
# l1 regularization parameter
config_dbb.l1 = 0.0
# l2 regularization parameter
config_dbb.l2 = 0.0
# number of processor for optimization
config_dbb.proc = 1

configKS["dbb"] = config_dbb
