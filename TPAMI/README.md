# Todo - List

## SOTA

### ConvNet Search Space

| Name  | MFLOPs(M)  | Top-1 (%) |
| :------------ |:---------------:| -----:|
| AlphaNet-A0      | 203 | 77.87 |
| *Cream-S*      | 287 | 77.60 |
| AlphaNet-A1     | 279 | 78.94 |
| AlphaNet-A2     | 317 | 79.20 |
| AlphaNet-A3    | 357 | 79.41 |
| AlphaNet-A4     | 444 | 80.01 |
| *Cream-M*     | 481 | 79.20 |
| AlphaNet-A5 (small)     | 491 | 80.29 |
| AlphaNet-A5 (base)    | 596 | 80.62 |
| *Cream-L*    | 604 | 80.00 |
| AlphaNet-A6     | 709 | 80.78 | 

### Transformer Search Space

| Name  | MFLOPs(G) | Params(M)  | Top-1 (%) |
| :------------: |:---------------:|:---------------:| :-----:|
| AutoFormer-T  |  1.3  | 5.7 | 74.7 |
| ViTAS-T     | 1.4 | 13.8 | 79.4 |
| BossNet-T0  |  3.4  | - | 80.5 |
| AutoFormer-S  |  5.1  | 22.9 | 81.7 |
| BossNet-T1  |  5.7  | - | 81.6 |
| Twins-SVT-S  |  2.9  | 24.0 | 81.7 |
| S3-S  |  54.7  | 28.1 | 82.1 |
| ViTAS-S    | 3.0 | 30.5 | 82.0 |
| S3-T-384  |  33.0  | 50.0 | 84.5 |
| AutoFormer-B  |  -  | 53.7 | 82.4 |
| Twins-SVT-B  |  8.6  | 56.0 | 83.2 |
| ViTAS-B     | 8.8 | 66.0 | 83.5 |
| S3-B-384     | 46.0 | 71.0 | 84.7 |


## Plans

### 1: Once-For-All, ConvNets

#### Progressively Sampling -> Search Space Shrinking / Searching Search Space

* Enlarge search space and progressively shrink to small but better search space
    * Reason: Better MaxNet, Better teacher
    * stage 3 can have more blocks -> better accuracy
    * Efficient archs are trained by more resources
* paragraphs in paper
* Add Abaltion Studies
    * Supernet Accuracy of different search space
    * Add visualization of space search progress
    
#### Meta Matching

* by uncertainty, [GreedyNASV2](https://arxiv.org/abs/2111.12609)
* by BN statistics (teacher and student), [BN-NAS](https://arxiv.org/abs/2108.07375)

#### Accuracy Predictor -> Online Accuracy Predictor

* pretrained -> online update
* final accuracy = predicted accuracy + *modifiled accuracy*
    * predicted accuracy is obtained by a pretrained predictor
    * *modifiled accuracy* is obtained by a predictor updated online
    
#### Risk

* Accuracy (under once for all scheme)
* Attentivenas leverage MAXNet to obtain better accuracy, we propose to search a teacher for each student
    * Without MAXNet, accuracy might drop vastly
    * AttentiveNAS accuracy benefits from huge parameters, retrained accuracy should be larger than once-for-all.

### ***2: Extremely Quick Search, Retrain, ConvNets

#### Search Space Shrinking and Extremely Quick Search

* Enlarge search space and quickly shrink it to a small but better search space
    * Shrink by the prioritized board prior
        - Common OPs
        - learn an online update indicator (whether efficient or not)
            * by arch / BN / features
        - generate new archs by mutation and crossover
    * Extremely Quick Search
        * Train BN only, leveraging [BN-NAS](https://arxiv.org/abs/2108.07375)
        * Train supernet for only a few epochs without degradation of correlation leveraging metaNN
            * Shrink search space by PB prior
            * a few epochs (a few iterations)
    
#### Meta Matching

* by uncertainty, [GreedyNASV2](https://arxiv.org/abs/2111.12609)
* by BN statistics (teacher and student), [BN-NAS](https://arxiv.org/abs/2108.07375)

#### Accuracy Predictor -> Efficiency Indicator

* Identify whether arch is efficient or not
    * Model the learning as: Huge negative data, few postive data
        * Random Forest
        * Outlier detection 
        * ....

### 3: Conv Stem + Transformer Search Space

#### search space -> transformer block 

* Similarly to [BossNAS](https://arxiv.org/abs/2103.12424)
* Refine search space by newly published transformer models

#### Retrain / Once for ALL 

* Extremely Quick Search
    - Same as before, a few epochs/iterations are included
* Retrain or directly slice the discovered arch from PB 



