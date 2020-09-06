# General Python notes

If you're using Miniconda / Anaconda and want to switch Python versions, do like:

```sh
conda create -n py37 python=3.7
```

To switch to Python 3.7 (or whatever environment you create) do in **each terminal**:

```sh
conda activate py37
```
and then run the desired commands. Note you'd need to again do:

```sh
python -m pip install -e .
```
to activate this program in the environment (one time).
