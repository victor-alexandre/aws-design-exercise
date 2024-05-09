# Teste Prático

Neste documento será apresentado uma proposta de solução aos itens abaixo:
- [Desenho e descrição de injestão e processamento em real time](#desenho-e-descrição-de-injestão-e-processamento-em-real-time)
- [Exemplo airflow](#2.-exemplo-airflow)

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
_______

### 1. Desenho e descrição de injestão e processamento em real time

#### Proposta de Solução 1: Streaming

![Design 1](https://raw.githubusercontent.com/victor-alexandre/aws-design-exercise/main/Proposta%20de%20solu%C3%A7%C3%A3o%201.png)

Descrição: 

Nessa arquitetura 1 os dados modificados no banco transacional serão capturados pelo DMS (Database Migration Servive), item 2; serão direcionados para o Kinesis, item 3, em forma de stream; processados por uma das ferramentas do item 4, sendo o Glue a que apresenta melhor custo benefício (caso o volume de dados seja muito alto será melhor utilizar outra ferramenta como o EMR ou o Apache Flink); armazenados em uma das opções do item 5 sendo o s3 + athena a mais barata e, por último, visualizados por uma ferramenta de BI.

Prós: 
  - Responde o exercício proposto pelo teste, pois provê uma arquitetura real time.
    
Cons: 
  - Mais caro de se implementar e manter:
    - Componentes que trabalham com stream são mais caros;
    - Mais tempo levado a desenvolver, debugar, testar e manter.



Referências:

- [https://pages.awscloud.com/Customer-Showcase-Perform-Real-time-ETL-from-IoT-Devices-into-your-Data-Lake-with-Amazon-Kinesis_2019_0307-ABD_OD.html](https://pages.awscloud.com/Customer-Showcase-Perform-Real-time-ETL-from-IoT-Devices-into-your-Data-Lake-with-Amazon-Kinesis_2019_0307-ABD_OD.html)
- [https://aws.amazon.com/blogs/database/load-cdc-data-from-relational-databases-to-amazon-kinesis-using-database-migration-service/](https://aws.amazon.com/blogs/database/load-cdc-data-from-relational-databases-to-amazon-kinesis-using-database-migration-service/)
- [https://aws.amazon.com/blogs/database/use-the-aws-database-migration-service-to-stream-change-data-to-amazon-kinesis-data-streams/](https://aws.amazon.com/blogs/database/use-the-aws-database-migration-service-to-stream-change-data-to-amazon-kinesis-data-streams/)

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
_______

#### Proposta de Solução 2: Batch D-1

![Design 2](https://raw.githubusercontent.com/victor-alexandre/aws-design-exercise/main/Proposta%20de%20solu%C3%A7%C3%A3o%202.png)

Descrição: 

Nessa arquitetura 2 os dados completos do banco transacional serão enviados a um bucket s3, uma vez por dia; esse evento será capturado pelo Event Bridge, item 3, que irá disparar o processamento do pipeline; aplicará as transformações utilizando o Glue, item 4; salvará os dados em um bucket, item 5, que ficará acessível via athena, item 6, e poderão ser visualizados por uma ferramenta de BI, item 7.

Prós: 
  - Mais barato de se implementar e manter:
    - Componentes que trabalham com batch são mais baratos;
    - Menos tempo levado a desenvolver, debugar, testar e manter;
    - Menos tempo processando dados, pois o pipeline não ficará executando constantemente.
  - Resolve o problema de forma mais simples

Cons: 
  - Não resolve o problema da maneira pedida.
  - Existirá o atraso de 1 dia nas análises (creio que isso não gerará nenhuma degradação na hora de tomada de deciões, dado o domínio da aplicaão, entretanto, para uma análise justa estou elencando este item como um ponto negativo).

Referências:

- Eu.

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
_______

### 2. Exemplo airflow

O código no airflow executa uma dag que é composta por três atividades, uma que pega informaçoes de um personagem da disney de id par, outro que faz o mesmo para um id ímpar e, por último, uma atividade que junta as duas informações em um arquivo e salva localmente.

link: [exemplo_airflow](https://github.com/victor-alexandre/aws-design-exercise/blob/main/fetch_disney_character_info.py)
