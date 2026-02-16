<!-- # toyceptron
A simple implementation of a Perceptron neural network in Python for educational purposes. -->
<a id="fr"></a>

<div align="center">
  <a href="#en">EN</a> · 
  <a href="#fr">FR</a>

# Toyceptron

***Un projet minimaliste de réseau neuronal ou perceptron multicouche***

---

</div>

Toyceptron est un projet pédagogique dont le but est de comprendre le fonctionnement interne d’un **perceptron multi-couches** en l’implémentant entièrement en Python, **sans** bibliothèques externes.

L'idée est de mieux comprendre les mécanismes fondamentaux qui sous-tendent les réseaux neuronaux. 

## Objectif

Implémenter un réseau de neurones capable de :
- être initialisé avec des poids et biais fixes ou aléatoires
- effectuer une propagation avant (forward pass)
- produire une sortie à partir d’un vecteur d’entrée

Il n’y a pas d’apprentissage dans ce projet.

## Contraintes

- langage : python
- aucune bibliothèque externe autorisée (numpy, pytorch, sklearn, etc.)
- les vecteurs sont représentés avec des listes python
- le fichier `main.py` est fourni et sert de test

## Structure du projet

``` 
toyceptron/
├── neuron.py # neurone individuel
├── layer.py # couche de neurones
├── network.py # réseau de neurones
├── main.py # script de test
└── README.md
```

## Composants

![class diagram](./docs/class-diagram.png)

### Neuron
Un neurone stocke ses poids et son biais et calcule une sortie à partir d’un vecteur d’entrée.

### Layer
Une couche est un ensemble de neurones identiques. Elle applique une entrée à tous ses neurones et retourne un vecteur de sorties.

### Network
Le réseau est une composition de couches. Il propage une entrée à travers l’ensemble des couches et retourne la sortie finale.

## fonctions d’activation

Les fonctions suivantes sont supportées :
- identité
- seuil
- sigmoïde
- ReLU

## exécution

``` bash
python main.py
```

## compétences abordées

- python
- programmation orientée objet
- bases des réseaux de neurones
- compréhension du forward pass

*Projet réalisé dans un cadre pédagogique.*

<a id="en"></a>

<div align="center">
  <a href="#en">EN</a> · 
  <a href="#fr">FR</a>

# Toyceptron

***A minimal neural network or multi-layer perceptron project***

</div>

Toyceptron is an educational project aimed at understanding the internal
workings of a **multi-layer perceptron** by implementing it entirely in Python, **without** external libraries. 

The idea is to better understand the fundamental mechanisms behind neural networks. 

## Objective

Implement a neural network capable of:
- being initialized with fixed or random weights and biases
- performing a forward pass
- producing an output from an input vector

There is no training in this project.

## Constraints

- language: python
- no external libraries allowed (numpy, pytorch, sklearn, etc.)
- vectors are represented using python lists
- the `main.py` file is provided and serves as a test

## Project Structure

```
toyceptron/ 
├── neuron.py # individual neuron 
├── layer.py # layer of neurons 
├── network.py # neural network 
├── main.py # test script 
└── README.md
```

## Components

![class diagram](./docs/class-diagram.png)

### Neuron
A neuron stores its weights and bias and calculates an output from an input
vector.

### Layer
A layer is a collection of identical neurons. It applies an input to all its
neurons and returns a vector of outputs.

### Network
The network is a composition of layers. It propagates an input through all
layers and returns the final output.

## activation functions

The following functions are supported:
- identity
- threshold
- sigmoid
- ReLU

## execution

``` bash
python3 main.py
```

## skills covered

- python
- object-oriented programming
- neural network basics
- understanding the forward pass

*Educational project.*