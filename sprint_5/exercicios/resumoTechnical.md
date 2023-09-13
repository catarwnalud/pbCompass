#
## AWS Skill Builder - AWS Partner: Accreditation (Technical)

### Benefícios da computação em nuvem

    - Agilidade: as organizações podem inovar com mais rapidez devido ao acesso facilitado a uma ampla variedade de tecnologias.

    - Elasticidade: os recursos computacionais podem ser ajustados na capacidade ideal de acordo com a evolução das necessidades empresariais.

    - Economia de custo: as despesas de capital com data centers, data lakes, entre outros, são trocados por despesas variáveis bem menores, devido a escalabilidade, assim pagando apenas o que foi consumido.

    - Implantação global em questão de minutos: com a computação em nuvem as organizações podem ampliar as atividades para novas regiões geográficas e implementa-las globalmente em minutos.

#

### Infraestrutura

    As regiões são isoladas entre si, cada região é em uma área geográfica separada com vários locais separados uns dos outros, conhecidos como zonas de disponibilidade ou AZs. Cada AZs é totalmente isolado de outro AZ dentro de uma região.

    Todas as AZs dentro de uma região são interconectadas por meio de fibra, o que melhora a latência.

#

### Serviços computacionais

    Desenvolva, implante, execute e dimensione cargas de trabalho na AWS Cloud.

    - Amazon EC2: é um serviço web que disponibiliza capacidade computacional segura e redimensionável na nuvem.

    - Amazon EC2 Auto Scaling: configura a partir de gatilhos para aumentar ou diminuir automaticamente o número de instâncias.

    - Elastic Load Balancing: distribui o tráfego de entrada dos aplicativos em diversos destinos.

    - Amazon Elastic Container Service: É um serviço de gerenciamento de container que executa aplicativos em um cluster gerenciado.

    - Amazon Elastic Kubernetes Service: executa aplicativos Kubernetes na aws e no local.

    - Amazon Lambda:  é um serviço computacional que executa código sem a necessidade de provisionar ou gerenciar servidores.

    “instâncias” -> se refere aos recursos de hardware como memória e processador.

    Amazon Machine Image (AMIs) ->  se refere a configuração de software inicial de uma instância.

    O serviço de computação da AWS possibilita instâncias do EC2 com os componentes básicos, aplicar AMIs para personalizar as instâncias, configurar o auto scaling e o balanceamento de carga, pagando apenas pelo que é usado.


### Serviços de armazenamento

    São locais confiáveis, dimensionáveis e seguros para os dados.

    - Amazon Elastic Block Store:  é como um disco rígido para instâncias da Amazon EC2, configurado de acordo com as necessidades.

    - Amazon S3:  é ideal para o armazenamento em massa, seja de imagens, vídeos, entre outros,  foi projetado para facilitar a computação em escala na web para desenvolvedores,  possui a característica de ser rápido.

    - Amazon S3 Glacier:  permite reter dados por meses, anos e décadas.

### Serviços de bancos de dados

    Desenvolvido especificamente para casos de usos de aplicativos específicos.

    - Amazon Relational Database Service:  é um serviço de banco de dados relacional gerenciado com uma opção de seis mecanismos de banco de dados.

    - Amazon DynamoDB:  desempenho rápido e previsível.

    - Amazon ElastiCache: para dados que precisam ser recuperados rapidamente.

    O objetivo do serviço de banco de dados da AWS é substituir as tarefas diárias de gerenciamento por processos de valor agregado.

### Serviços de rede

    É possível criar uma rede virtual na nuvem ou VPC, atribuir ao VPC intervalo de endereços IP e configurar sub-redes públicas e privadas dentro da rede maior.

    Posso proteger a sub-redes usando ACL de redes e criar outra camada de segurança no nível da instância usando grupos de segurança.

### Serviços de segurança

    Possui modelo de responsabilidade compartilhada. Os clientes são responsáveis por aspectos relacionados à proteção dos dados e recursos criados na nuvem,  enquanto a WS o processo a parte de segurança da infraestrutura e os seus serviços gerenciados.

#

### Integração de serviços e soluções

    Os sete R 's são as maneiras de migrar um sistema on-premise para a nuvem.

    - Re-hospedar:  lift and shift

    Para aplicativos on-premise a abordagem mais comum é re-hospedar, basicamente transfere os recursos do aplicativo on-premise para nuvem nas instâncias EC2 e no bucket do S3.

    - Redefinir plataforma: lift, thinker and shift

	Retém a arquitetura principal, fazendo otimizações direcionadas para a nuvem.

    - Realocar: lift and shift no nível hypervisor

    Essa migração move uma Infraestrutura VMware para a nuvem sem comprar novo hardware, reescrever aplicativos ou modificar operações existentes.

    - Refatorar: modernizar
	
	Reinventar como aplicativo é arquitetado e desenvolvido usando recursos nativos da nuvem, adicionando recursos, dimensionamento ou desempenho.
        
    - Retirar

    Desativa aplicativos inúteis, que reduzem a velocidade, o gerenciamento e a segurança.

    - Reter

    Mantém determinados aplicativos on-premise.

    - Recomprar

    Move fluxos de trabalho para a SaaS.

#

### Práticas recomendadas de arquitetura na nuvem

    - Design à prova de falhas

        - Use várias instâncias em vez de uma
        - Utilize várias zonas de disponibilidade
        - Separe um único servidor em vários aplicativos em camadas, para que cada um fique responsável por uma função

    - Crie segurança em cada camada

        - Criptografe dados em repouso e em trânsito
        - Aplique o princípio de menor privilégio no IAM (gerenciador de identidade em nuvem, garante os acessos adequados)
        - Implante grupos de segurança e listas de controle de acessos à rede (NACL)

    - Aproveite diferentes opções de armazenamento

        - Mova ativos estáticos para a Amazon S3
        - Utilize o Amazon CloudFront para permitir a escalabilidade global do seu conteúdo estático
        - Armazene o estado da sessão no DynamoDB
        - Use o ElastiCache para armazenar resultados comuns de consultas de banco de dados

    - Implementar a elasticidade

        - Implemente políticas de Auto Scaling
        - Arquitete resiliência para reinicializar e relançar
        - Use serviços gerenciados como Amazon S3 e o Amazon DynamoDB

    - Pense paralelo

        - Adicione mais recursos computacionais ao seu aplicativo, em vez de adicionar mais potência aos recursos computacionais 
        - Desacople a computação da sessão/estado, para ajudar com scaling e disponibilidade 
        - Use balanceadores de carga elásticos para distribuir a carga 
        - Dimensione corretamente a infraestrutura de acordo com sua carga de trabalho 
        
    - O acoplamento fraco

        - Quando serviços são acoplados fracamente, eles podem ser dimensionados e tolerantes a falhas além de serem independentes um do outro.

# 

### Well-Architected Framework 

    - O que é?

        Um recurso essencial para ajudar a projetar soluções seguindo as práticas recomendadas

    - Os seis pilares

        - Excelência operacional: se concentra em executar e monitorar sistemas para entregar valor empresarial e melhorar continuamente os processos

        - Segurança: protege as informações, incluindo a confidencialidade, integridade dos dados, identificação e gerenciamento de quem pode fazer o quê

        - Confiabilidade: foca na capacidade de evitar e se recuperar rapidamente de falhas

        -  Eficiência de desempenho: uso eficiente de recursos de TI e computação
    
        - Otimização de recursos: tem como objetivo evitar gastos desnecessários

        - Sustentabilidade: se concentra em minimizar os impactos ambientais da execução  de cargas de trabalho em nuvem

    - O processo de migração

        - Avaliação: identificar a preparação

        - Preparação e planejamento: determinar estratégias de migração e criar uma landing zone bem arquitetada

        - Migração e modernização: projetar, migrar e validar cada aplicativo de maneira automática ou manual e migrar os dados
