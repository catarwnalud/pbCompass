#
## Data Analytics Fundamentals

### Lição 1: Introdução a soluções de avaliações de dados

    "Como armazenar, processar, analisar e apresentar dados?"

#

## Tópico 1: Análise de dados e soluções de avaliações de dados

- Avaliação de dados: é o processo de compilar, processar e analisar dados para que você possa usá-los para tomar decisões.
    
- Análise de dados: extrai valor dos dados, ajudando a gerenciar todo o ciclo de gerenciamento de dados, desde a coleta até a criação de relatórios.
    
- Benefícios de análise de dados em grande escala

    - Personalização do cliente: com base no hábito de compra, qual produto mostrar ao cliente?
    
    - Detecção de fraude: essa transação pendente é fraudulenta?

    - Detecção de ameaças à segurança: quais padrões de uso indicam possíveis riscos de segurança?

    - Comportamento do usuário: qual nível de influência que uma pessoa possui?

    - Modelagens e previsões financeiras: quais tendências podem ser detectadas nesses terabytes de dados fincanceiros? Como usar isso para prever mudanças no mercado?

    - Alerta em tempo real: qual é o problema e quem precisa ser notificado?

- Os desafios identificados em muitas soluções de avaliação de dados podem ser resumidas pelos cinco componentes do Big Data: volume, velocidade, variedade, veracidade e valor.

- Componentes de uma solução de avaliação de dados

    - Ingerir/coletar: é a coleta dos dados brutos. Uma boa solução de avaliação de dados permite a ingestão de grande variedade de dados - estruturados, semiestruturados ou não estruturados - a qualquer velocidade.

    - Armazenar: uma boa solução deve oferecer armazenamento seguro, escalável e durável, que possa armazenar dados estruturados (como o Data Warehouse), semiestruturados (como banco de dados, que também é possivel incluir os dados estruturados)  e não estruturados (como Data Lakes que armazena os três tipos).

    - Processar/analisar: primeiro dados devem ser processados, tranformados para tornar-los mais consumível. Como parte do processamento, os dados também serão analisados, isso significa classificar, agregar, unir e aplicar a lógica de negócio. A etapa final é carregar esse conjunto de dados analíticos significativos em um novo local de armazenamento, como um Data Lake, Warehouse.

    - Consumir/visualizar: existem duas maneiras de consumir dados: consultas ou usando ferramentas de business intelligence (BI). A consulta produz resultados excelentes para avaliações rápidas por analistas de dados. As ferramentas BI produzem visualizações agrupadas em relatórios e painéis para ajudar a explorar os dados e determinar as melhores ações.

#

## Tópico 2: Introdução aos desafios de análise de dados

    "Qual solução de análise de dados eu preciso? Complexa? Básica?"

    Tudo depende dos cincos V's

    - Volume: quantidade de dados

    - Velocidade: rápidez com que os dados entram e transitam

    - Variedade: ingestão de dados com tipo, fontes diversas

    - Veracidade: confiabilidade dos dos dados

    - Valor: capacidade de criar insights

- Planejamento de uma solução de avaliação de dados

    - Conheça a origem dos dados: provem de banco de dados e armazementos de arquivos on-premises. Pode ser dados de streaming feitos em tempo real, ou o conjunto de dados públicos que conta com dados de censo, de saúde, populacionais, entre outros.

    - Conheça as opções para processar os dados

    - Saiba o que você precisa aprender com seus dados

#

### Lição 2, volume: armazenamento de dados

    Quando uma empresa tem mais dados do que conseguem processar e analisar, ela têm um problema de volume.

- Classificação ampla de tipos de origem de dados:

    - Dados estruturados: organizado e armazenado na forma de valores que são agrupados em linhas e colunas de uma tabela

    - Dados semiestruturados: arquivos CSV, XML, JSON

    - Dados não estruturados: imagens, email, tweets

#

## Tópico 1: Introdução ao Amazon S3

    A Amazon Simple Storage Service (Amazon S3) é o serviço de armazenamento que pode ajudar a solucionar qualquer volume de dados.

- Conceitos do Amazon S3

    - Buckets: armazena os objetos (dados)

    - Objeto: é composto por um arquivo. Para armazenar um objeto na Amazon S3, é necessário fazer o upload que deseja armazenar no bucket. Ao fazer o upload de um arquivo você pode definir permissões no objeto e adicionar dados.

    - Chave de acesso: juntamente com o nome do bucket é possível acessar um objeto

#

## Tópico 2: Introdução ao Data Lakes

    "Como os dados são armazenados na Amazon S3?"

- Data Lakes são conceitos de arquitetura que auxiliam no gerenciamento. Tem a ideia de ser um repositório centralizado que permite armazenar dados estruturados, semiestruturados e não estruturados em qualquer escala.
É uam solução econômica, seguro e com conformidade, possui diversas ferramentas de coleta e ingestão e ajuda a categorizar e extrair valor dos dados.

- AWS Lake Formation: é um serviço que organiza e faz curadoria de dados dentro de Data Lakes do Amazon S3. Garante a segurança e a conformidade de itens dentro do Lake, bem como orquestra trabalhos de transformação.

#

## Tópico 3: Introdução aos métodos de armazenamento de dados

- Data Warehouse são utilizados para armazenar dados estruturados provenientes de muitas origens, esses dados são transformados, agregados e preparados.
    
    - dados -> etl -> data warehouse -> valor

- Amazon S3 hsopeda o Data Lake

- Amazon Redshift hospeda Data Warehouse

- Amazon Redshift Spectrum combina o Data Lake e o Data Warehouse como única fonte de dados.

- Benefícios do Amazon Redshift:

    - 10X mais rápido do que Data Warehouse on-premises

    - Fácil de configurar, implantar e gerenciar

    - Seguro

    - Escala rapidamente para atender as necessidades

#

### Lição 3: Velocidade de processamento de dados

    Quando empresas precisam de informações rápidas dos dados que estão coletando, mas os sistemas implantados não atendem as necessidades, há um problema de velocidade.

- Processamento de dados: refere-se tanto à coleta quanto a manipulação dos dados.

#

## Tópico 1: Introdução aos métodos de processamento de dados

- Processamento Batch: processamento de dados em intervalos. Usado quando existem grandes quantidades de dados para processar em intervalos.

    - Agendado: uma rotina regular que processa grande quantidade de dados

    - Periódico: é feita em uma rotina aleátoria

- Processamento em Stream: processa dados em fluxos contínuos, em pequenos conjuntos de dados.

    - Tempo real: processa em tempo real, mas em muita pouca quantidade

    - Próximo do tempo real: processa QUASE em tempo real conjuntos pequenos de dados

#

## Tópico 2: Introdução ao processamento de dados em Batch

    O processamento de dados em Batch oferece a capacidade de aprofundamento nos dados coletados para análises complexas

- Apache Hadoop: sistema de armazenamento e processamento de dados em Batch. Complementa os sistemas de dados existentes ao ingerir e processar simultaneamente grandes volumes de dados, estruturados ou não, de qualquer fonte.

- Amazon EMR: é um serviço gerenciado para a implantação de cargas de trabalho do Apache Hadoop. Executa esse e vários outros frameworks. Pode ser usado para procesar quantidades massivas de dados a uma velocidade extremamente alta, além de ser personalizavel e fornecer análises complexas.

- Em uma arquitetura de processamento em Batch, o AWS Lambda é uma opção de computação sem servidor para acionar eventos de processamentos.

- O Amazon Redshift é um serviço gerenciado para armazenar grandes quantidades de dados em transações para fins de análise em um sistema de big data.

#

## Tópico 3: Introdução ao processamento de dados em Stream

- Amazon Kinesis: facilita a coleta, processamento e a análise de dados de Stream em tempo real, permitindo a rápida reação a informações, além de ser econômico. É dividido em várias recusros individuais que auxiliam em todos os processos.

- Benefícios de processamento em Stream

    - Desacoplar coleta de processamento

    - Coletar vários fluxos juntos

    - Preservar a ordem do cliente

    - Consumir dados em paralelo 

- Arquitetura do processamento Stream

    - Amazon Kinesis Data Firehose: coleta os dados de streaming pelo dispositivo de sensor

    - Amazon Kinesis Data Analytics: recebe os dados do Amazon Kinesis Data Firehose e filtra para os registros relevantes, enviando de volta para o Data Firehose em outro processo, que coloca os resultados em um bucket do Amazon S3.

    - Amazon Athena: acessando os dados dos bucktes consulta dados para ter relatórios usando o Amazon QuickSight.

#

### Lição 4, variedade: estruturas e tipos de dados

    Quando sua empresa fica sobrecarregada pelo grande número de origens dos dados para analisar e você não consegue encontrar sistemas para fazer análise, existe um problema de variedade

#

## Tópico 1: Introdução ao armazenamento de dados de origem

- Tipos de origem de dados

    - Dados estruturados, semiestruturados e não estruturados

#

## Tópico 2: Introdução a Data Stores estruturados

- Um banco de dados relacional é criado para armazenar dados estruturados para que possam ser coletados, atualizados e consultados fácilmente

- Métodos principais para organizar os dados em um banco de dados

    - Processamento de transação on-line (OLTP): dados coletados por esse processamento geralmente alimentam outro tipo de banco de dados que se concentra em análises.

    - Processamento analítico on-line (OLAP): coletam dados de sistemas OLTP com o objetivo de organizar para operações analíticas.

#

## Tópico 3: Introdução a Data Stores semiestruturados e não estruturados

- Esses tipos de dados são armazenados em banco de dados não relacionais, ou seja não precisam de relacionamentos conectando-os.

- Dynamo DB: serviço para armazenamento de dados NoSQL, chave-valor é a solução.

- Banco de Grafos: principalmente para a análise de relacionamento entre qualquer tipo de dados. O Amazon Neptu é o serviço de banco de dados de grafo da AWS.

#

### Lição 5, veracidade: limpeza e transformação







