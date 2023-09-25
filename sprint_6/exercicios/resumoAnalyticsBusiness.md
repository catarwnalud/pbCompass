#
## Data Analytics Business

### Módulo 1: Oportunidade de mercado

#### O que é Big Data?

    Big data são dados em quantidade tão grande e com crescimento tão rápido que seu armazenamento e gerenciamento tornam-se um desafio.

    Características (os quatro V's):

    - Volume: escala de tamanho de dados
    - Velocidade: taxa de criação e crescimento dos dados
    - Variedade: variedade de formatos
    - Veracidade: incerteza dos dados

#### Dados como um ativo estratégico e diferencial

    - Dados são informações registradas em formato digital, de pessoas, eventos, itens, transações, entre outros.

    - Dados se transformam em insights que possuem valor econômico oferecendo serviços personalizados.

    - Dados são: transmitidos, processados, analisados e armazenados.

#### Desafios de análise de dados enfrentados por empresas

    - Insuficientes habilidades técnicas.

    - Insuficiente privacidade de dados.

    - Insuficiente segurança dos dados

#### Governança de dados

    - Os usuário de dados necessitam de agilidade para acessar e trabalhar em cima dos dados, é necessário fornecer acesso democratizado aos dados aplicando a governança de dados para evitar má gestão.

    - Os principais pontos de atenção são a segurança e privacidade.

        - Segurança: como impedir o acesso não autorizado aos dados da empresa.

        - Privacidade: como proteger os dados pessoais dos clientes.

#### O pipeline de dados e o Data Flywheel

    Antes de extrair insights dos dados os cliente devem decidir como irão realizar o processo de gerenciamento de dados.

    - Desafios no gerenciamento de dados

        - Coletar uma variedade de tipos de dados acumulados em velocidade váriaveis

        - Coletar dados de várias fontes acumuladas em velocidades diferentes

        - Armazenar grandes quantidades de dados sem esgotar espaço

        - Limpar e aumentar a quantidade dos dados a serem analisados

        Uma maneira fácil de lidar com o gerenciamento é automatizando esses proccessos.

#### Criar um pipeline de análise de dados com a AWS

    - Para coletar:

        - Amazon Kinesis Data Streams
        - Amazon Kinesis Data Firehose
        - AWS Snowball
        - AWS Direct Connect

    - Para armazenamento:

        - Amazon Simple Storage Service (Amazon S3)
        - Amazon S3 Glacier
        - Amazon DynamoDB
        - Amazon RDS
        - Amazon ES
        - Amazon CloudSearch
        - Amazon Aurora

    - Para processar/analisar:

        - Amazon EMR
        - Amazon Athena
        - Amazonn Redshift
        - Amazon  Kinesis Data Analyctics
        - Amazon SageMaker

    - Para visualizar:

        - Amazon QuickSight

    Para automatizar os processos:

        - AWS Database Management Service: para migração de dados de banco de dados e a replicação de proccessamento de transações online (OLTP) e Data WareHouse para o Amazon Redshift

        - AWS Glue: serve para o agendamento e orquestração de dados
    
##  Data Flywheel e a jornada do cliente para arquitetura de dados moderna

    Primeiro os clientes devem migrar seus dados e workloads para a nuvem, quando os dados estiverem na nuvem, é possível serviços gerenciados para se benificiar da agilidade, escala, performance economia de despesas operacionais (OpEx) sobre despesas de capital (CapEx). Em seguida, os clientes podem começar a criar aplicações orientadas por dados e monetizar insights a partir dos dados, podem também modernizar os Data Warehouse e construir um Data Lake para ter os dados que precisam em um único local.

#

### Módulo 2: Soluções de análises de dados na AWS

#

#### Solução 1: Modernizar um data warehouse com o Amazon Redshift

- Jornada do cliente para uma arquitetura de dados moderna

    - Devem adotar uma estratégia de priorização da nuvem, migrando os banco de dados on-premises para a nuvem.

    - Em seguida os clientes devem determinar como armazenar e gerenciar os dados de uma forma que economize custo, para ter melhor performance, escabilidade e agilidade.

    A AWS oferece recursos para a migração de dados, e a escolha depende da quantidade de dados, a fonte de dados e da rapidez com que se deseja mover eles.

        - AWS Direct Connect
        - AWS Snowball
        - AWS Storage Gateway
        - AWS Database Migration Service (AWS DMS), que move o banco de dados para o Amazon RDS
        - Amazon Kinesis Data Firehose
        - Amazon S3 Transfer Acceleration

- Data WareHouse

    Um repositório central de dados selecionados de diferentes fontes

    - Benefícios:

    - Tomadas de decisão
    - Dados consolidados
    - Quantidade de dados aprimorada
    - Acesso à inteligência histórica
    - Melhora de performance

    Muitos clientes migram seu banco de dados on-premises para o Data Warehouse na nuvem.

    Desafios de um Data WareHouse on-premises:

        - Custos de escabilidade
        - Longos ciclos de implementação e altas taxas de falha
        - Falha de adaptação às novas tecnologias
        - Não conseguem lidar com a variedade de dados
        - Problemas de governança e controle
        - Custo de manuntenção

- Amazon Redshift

    É um Data WareHouse em nuvem totalmente gerenciado, otimizado para alta performance, compatível com formatos de arquivos abertos, flexível e de alta escabilidade, com capacidade de executar consultas e análises complexas, integrado com outros serviços da AWS e com menor custo.

#

#### Solução 2: Criar um Data Lake

    Após modernizar os Data Warehouse usando o Amazon Redshift, deve-se mover os restanta dos dados locais. Criar um Data Lake permite que seus clientes obtenham insights mais rápidos.

    Um Lake é uma abordagem de arquitetura para um repositório de dados centralizado, que permite armazenar dados estruturados ou não estruturados de qualquer escala e fonte além de possibilitar diversos tipos de análise.

- Data Lakes no Amazon S3

    Sem um Lake, colocar dados corporativos em um bucket do S3 pode resultar em um swamp de dados. 

    Data Swamp = dark data, não pesquisável e de pouco valor.

- Etapas típicas da criação de um Data Lake:

    - Configurar armazanamento: os Lakes devem ser capazes de conter uma grande quantidade de dados

    - Mova os dados: deve-se conectar a diferentes fontes de dados on-premises, na nuvem e em dispositos IoT, usar ferramentas de transferência e extração que coletam e organizam conjuntos de dados

    - Limpe e prepare os dados: particionar, indexar e transformar dados. 

    - Configurar e aplicar políticas: proteger dados de acordo com os requisitos de compatibilidade, devem criar e aplicar políticas de acesso aos dados.

    - Facilitar a localização de dados: o objetivo é facilitar para os usuários finais como analistas de dados, a localização de dados relevantes e confiáveis no Lake


- AWS Lake Formation

    Simplifica e automatiza o processo para criar um Lake seguro, reduzindo o tempo de configuração de meses para dias.

- Amazon Redshift Spectrum

    Armazene seus dados onde quiser, no formato desejado e disponibilize quando precisar

# 

#### Solução 3: Transmissão e análise preditiva

    Após criar o Data Lake, eles podem utilizar o Kinesis para coletar dados em transmissão.

- Dados de transmissão 

    Gerados continuamente de milhares de fontes de dados coletados em tempo real. Devem ser processados sequencialmente e incrementalmente ou em janelas de tempo.

    - Processamento

    Requer uma camada de armazenamento:: é compatível com pedidos de registros e consistência forte, e outra de processamento: consome dados, executa cálculos e notifica quando os dados não são mais úteis.

- Solução de transmissão de dados da AWS

    O Amazon Kinsis é um serviço de análise em tempo real.

    - Kinesis Data Stream: captura e armazena os dados

    - Kinesis Data Analytics: analisa fluxos de dados em tempo real

    - Kinesis Data Firehose: carrega dados de streaming

    - Kinesis Video Streams: análise de áudio e video em tempo real

    - Kinesis Managed Streaming For Apache Kafta: serviço gerenciado para o Apache Kafta

#

#### Solução 4: Analisar a governança de dados

    Desafios de um repositório centralizado:

    - Proteção de dados
    - Auditoria do uso de dados
    - Gerenciamento do acesso a dados
    - Proteção de dados sigilosos

- Ferramentas e serviços para descobrir, classificar e proteger dados sigilosos:

    - Amazon S3: armazenamento seguro de dados em andamento e repouso com o supoorte de criptografia

    - Amazon Macie: descubra, classifique e proteja os dados sigilosos com o suporte de machine learning.

    - Amazon Cloud Watch: monnitore e observe recursos, aplicações e dados.

- AWS Glue e AWS Glue Data Catalog

    - AWS Glue: totalmente gerenciável, categoriza, limpa, enriquece e move os dados entre armazenamentos de dados.

    - AWS Glue Data Catalog: repositório central de metadados

#

#### Solução 5: Machine Learning 

    É possível usar ML e IA com o Data Lake para continuar processando e analisando os dados. Eles podem fazer previsões e monetizar os seus dados, criando novos insights, aplicativos, entre outros.

    Esses novos serviços e produtos por sua vez criam mais dados que podem ser armazenados e gerenciados na nuvem, dando a oportunidade de criar novos recursos e aplicações, criando um impulso real e sustentado com o ciclo virtuoso do Data Flywheel.

#

#### Diferenciais de análise de dados da AWS

- Serviços de análise de dados da AWS

    - Amazon Athena: serviço de consulta iterativa e sem servidor usando SQL

    - AWS Glue: prepara e carrega dados

    - AWS Data Exchange: encontre e assine dados de terceiros na nuvem

    - Amazon SageMaker: cria, treina e implanta modelos de machine learning em grande escala

#

### Módulo 3: Conversas de negócios

#

#### Perguntas sobre a descoberta e público-alvo

    Duas maneiras de visualizar o público dos clientes:

    - Amplamente: por cargo e responsabilidades

    - Detalhadamente: por uma função em um ciclo de vendas

    E dois modos:

    - Empresarial

    - Técnico

- Perguntas de descobertas:

    - Estado e iniciativas atuais: quais são as principis prioridade? Quais são seus projetos atuais de big data e análise?

    - Desafios: quais são os principais problemas empresariais que estão tentando solucionar com a análise de dados? Quais desafios você enfrentou na execução de seus projetoss e iniciativas?

    - Dependências: qual sua função no projeto? Quem mais está envolvido no processo de decisão? Quais são seus investimentos existentes na infraestrutura de dados?

    - Impacto: o que pode aconetcer se você não conseguir realizar suas iniciativas? O que pode acontecer se voccê não fizer nada com seus dados?

#






























































