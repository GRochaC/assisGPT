# assisGPT

Implementação, treinamento e avaliação de um modelo de linguagem baseado na arquitetura GPT-2, utilizando textos do escritor brasileiro Machado de Assis.

O projeto foi desenvolvido para a disciplina **PPGI0034 — Redes Neurais e Aprendizado Profundo**.

> **Importante:** este repositório é um fork de [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT), criado por Andrej Karpathy. A implementação-base do modelo, o processo de treinamento e os scripts de geração foram desenvolvidos no projeto original. O assisGPT adapta essa base para a preparação dos textos de Machado de Assis, configuração dos experimentos, treinamento e avaliação do modelo.

## Requisitos

- Python 3.10 ou superior;
- PyTorch;

## Instalação

Instale as dependências:

```bash
pip install torch numpy transformers tiktoken wandb tqdm pypdf
```

## Preparação dos dados

Os textos de Machado de Assis e o script de preparação ficam em:

```text
data/machado/
```

O arquivo principal com o corpus deve estar em:

```text
data/machado/input.txt
```

Para tokenizar o corpus e criar os conjuntos de treino e validação, execute:

```bash
python data/machado/prepare.py
```

Ao final, serão criados os arquivos:

```text
data/machado/train.bin
data/machado/val.bin
```

## Treinamento

As configurações do experimento estão em:

```text
config/train_machado.py
```

Para iniciar o treinamento, execute:

```bash
python train.py config/train_machado.py
```

Durante o treinamento, o programa apresenta as perdas de treino e validação. O melhor checkpoint é salvo no diretório definido por `out_dir` na configuração, por padrão:

```text
out-machado/ckpt.pt
```

Caso uma GPU não esteja disponível, um simples treinamento utilizando a CPU pode ser feito pelo comando:
```bash
python train.py config/train_machado.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
```

## Avaliação

Para carregar o checkpoint salvo e calcular novamente as perdas de treino e validação, execute:

```bash
python train.py config/train_machado.py --init_from=resume --eval_only=True
```

A principal métrica acompanhada é a *loss*. Valores menores indicam melhores previsões sobre o conjunto avaliado. Uma `train loss` decrescente acompanhada por uma `val loss` crescente pode indicar *overfitting*.

## Geração de texto

Após o treinamento, utilize o checkpoint para gerar novos textos:

```bash
python sample.py \
    --out_dir=out-machado \
    --start="Era uma vez" \
    --num_samples=5 \
    --max_new_tokens=500
```

Principais argumentos:

- `--out_dir`: diretório que contém o checkpoint;
- `--start`: texto inicial usado como entrada;
- `--num_samples`: quantidade de textos gerados;
- `--max_new_tokens`: quantidade máxima de novos tokens por texto.

Para rodar em uma CPU, execute:
```bash
python sample.py \
    --out_dir=out-machado \
    --device=cpu
    --start="Era uma vez" \
    --num_samples=5 \
    --max_new_tokens=500
```

## Créditos

Este projeto é derivado do [nanoGPT](https://github.com/karpathy/nanoGPT), de [Andrej Karpathy](https://github.com/karpathy). Os créditos, a licença e o histórico do projeto original devem ser preservados.

Adaptação desenvolvida por **Guilherme da Rocha Cunha** para a disciplina **PPGI0034 — Redes Neurais e Aprendizado Profundo**.
