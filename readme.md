# Teste Prático

Neste documento será apresentado uma proposta de solução às questões abaixo:
- [Desenho e descrição de injestão e processamento em real time](#desenho-e-descrição-de-injestão-e-processamento-em-real-time)
- [Exemplo airflow](#exemplo-airflow)


aaaaaaaaaaaaaaaa
a

### 1. Desenho e descrição de injestão e processamento em real time
![Design 1](https://raw.githubusercontent.com/victor-alexandre/aws-design-exercise/main/Proposta%20de%20solu%C3%A7%C3%A3o%201.png)



![Design 2](https://raw.githubusercontent.com/victor-alexandre/aws-design-exercise/main/Proposta%20de%20solu%C3%A7%C3%A3o%202.png)


### 2. Exemplo airflow

O código no airflow executa uma dag que é composta por três atividades, uma que pega informaçoes de um personagem da disney de id par, outro que faz o mesmo para um id ímpar e, por último, uma atividade que junta as duas informações em um arquivo e salva localmente.
Há uma função para salvar em um bucket s3, basta inserir os parametros da sua conta na aws para poder utilizar a função.
