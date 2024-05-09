# Teste Prático

Neste documento será apresentado uma proposta de solução às questões abaixo:
- [Desenho e descrição de injestão e processamento em real time](#desenho-e-descrição-de-injestão-e-processamento-em-real-time)
- [Exemplo airflow](#exemplo-airflow)


aaaaaaaaaaaaaaaa
a

### 1. Desenho e descrição de injestão e processamento em real time

#### Proposta de Solução 1: Streaming

![Design 1](https://raw.githubusercontent.com/victor-alexandre/aws-design-exercise/main/Proposta%20de%20solu%C3%A7%C3%A3o%201.png)

Referências:

- [https://pages.awscloud.com/Customer-Showcase-Perform-Real-time-ETL-from-IoT-Devices-into-your-Data-Lake-with-Amazon-Kinesis_2019_0307-ABD_OD.html](https://pages.awscloud.com/Customer-Showcase-Perform-Real-time-ETL-from-IoT-Devices-into-your-Data-Lake-with-Amazon-Kinesis_2019_0307-ABD_OD.html)
- [https://aws.amazon.com/blogs/database/load-cdc-data-from-relational-databases-to-amazon-kinesis-using-database-migration-service/](https://aws.amazon.com/blogs/database/load-cdc-data-from-relational-databases-to-amazon-kinesis-using-database-migration-service/)
- [https://aws.amazon.com/blogs/database/use-the-aws-database-migration-service-to-stream-change-data-to-amazon-kinesis-data-streams/](https://aws.amazon.com/blogs/database/use-the-aws-database-migration-service-to-stream-change-data-to-amazon-kinesis-data-streams/)


#### Proposta de Solução 2: Batch D-1

![Design 2](https://raw.githubusercontent.com/victor-alexandre/aws-design-exercise/main/Proposta%20de%20solu%C3%A7%C3%A3o%202.png)

Referências:

- Eu.

### 2. Exemplo airflow

O código no airflow executa uma dag que é composta por três atividades, uma que pega informaçoes de um personagem da disney de id par, outro que faz o mesmo para um id ímpar e, por último, uma atividade que junta as duas informações em um arquivo e salva localmente.

