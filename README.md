## Re2Com

### Requirements
- Python 3.7
- TensorFlow 1.15
- CUDA 10.1
- NLTK 3.4.5
- Java 1.8.0

### Train and Test

Our code is based on 

- put the dataset into the "funcom" directory
    - the dataset can be found at https://s3.us-east-2.amazonaws.com/icse2018/funcom.tar.gz
```
    tar xvf funcom.tar.gz
```
- Process the dataset and generate the vocabulary
```
    ./data-process.py
```
- Build the Retrieval corpus
```
    cd retrieve
    ./compile.sh
    ./buildIndex.sh
```
- Generate exemplars for training and testing
```
    cd retrieve
    ./buildExemplars.sh
```
- Train Re2Com model for standard dataset
```
    cd standard
    python __main__.py re2com.yaml --train -v
```
- Train Re2Com model for challenge dataset
```
    cd challenge
    python __main__.py challenge.yaml --train -v
```
- Retrieve code with standard dataset as corpus
  - Note that the output file will only contain numbers, which are the line numbers of the retrieved code.
```
    cd retrieve
    ./search.sh standard-corpus ${input-file} ${output-file}
```

### Evaluation
The evaluation results are located at `standard/models/eval/` or `challenge/models/eval/`.
Evaluation code is based on https://github.com/tylin/coco-caption
```
    cd evaluation
    python2 evaluate.py
```
