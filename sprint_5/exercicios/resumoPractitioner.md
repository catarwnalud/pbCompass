#
## AWS Skill Builder - Exam Prep: AWS Certified Cloud Practitioner

### Conceitos da nuvem

- Aspectos econômicos da AWS Cloud: como a operação na AWS afeta os custos operacionais e de propriedade da organização

    - Proposta de Custo Total de Propriedade (TCO)

        - Despesas operacionais (OpEx): são os custos do dia a dia da organização como serviçoes e itens consumidos.

        - Despesas de capital (CapEx): são os custos associados à criação, que criam benefícios de longo prazo, exemplo: compra de um prédio. Comprados uma vez e esperado que auxilie por anos a organização.

        - Custos de mão de obra associados a  operação on-premises: são os custos necessários para efetuar as operações on-premises.

        - Impacto do custo de licenciamento de software ao migrar para a nuvem: como um licenciamento de software pode ser afetado por uma migração para a nuvem.

- Identificar quais operações vão reduzir os custos ao serem movidas para a nuvem

    Embora alguns aplicativos possam ser migrados totalmente para a nuvem, geralmente hà outras coisas que precisam ser consideradas por serem mais econômicas.

    - Dimensionamento correto das infraestrutura: em vez de focar o provisionamento para picos de demanda, é avaliado o que é necessário e verifica outras maneiras de atender esse pico de demanda.

    - Automação: configurar automatização como o scaling automatizado pode ajudar a atender as necessidades para que não seja preciso executar a capacidade de pico quando não está em um pico de demanda.

    - Redução de escopo de conformidade e uso de serviços: utilizar dados e relatórios direcionados pode ajudar a reduzir o escopo e economizar tempo durante auditorias.

    - Uso de serviçoes autogerenciados: ajuda a reduzir sua carga de trabalho técnica e os custos para uma variedade de casos de uso.

- Principios de design para a arquitetura de nuvem

    - Design à prova de falhas: entenda como e quais componentes falham e como arquitetar falhas para adicionar resiliência.

    - Desacoplamento de componentes X arquiteturas monolíticas: nas arquiteturas monolíticas todos os processos são fortemente acoplados e executados como um único serviço, o que pode ocasionar problemas com pico de demanda além da complexidade de aprimorar e atualizar esses aplicativos, o desacoplamento pode ajudar solucionar essa questão.

    - Implementação de elasticidade na nuvem X on-premises: a aplicação de elasticidade sob demanda em um ambiente on-premise é complexa, pois a demanda é instável e investir em componentes de TI é caro. Na nuvem existe a possibilidade de mudar dinamicamente a capacidade baseado na demanda

    - Pensamento paralelo: o processamento serial e sequencial, semelhantes às arquiteturas monolíticas são limitantes e essas dependências podem criar ou quebrar processos inteiros. O pensamento paralelo é semelhante ao desacoplamento, mas é analisado como pode-se dividir um trabalho da forma mais simples e então, distribuir essa carga para vários componentes para lidar com a demanda.

#

### Securança e Conformidade 

    "Quem é responsável pelo que em relação à segurança?"

- Modelo de responsabilidade compartilhada

    - Cliente: responsável pela segurança NA nuvem

        - dados do cliente
        - plataforma, aplicativos, gerenciamento de identidade e acesso
        - configurações de SO, rede e firewall
        - criptografia

    - AWS: responsável pela segurança DA nuvem

        - softaware: computação, armazenamento, banco de dados, redes
        - hardware/infraestrutura global: regiôes, zonas de disponibilidade, locais de borda

- Conformidade: os requisitos de cada aplicação variam de acordo com o serviço

- Monitoramento de logs:

    - Amazon CloudWatch: serve para monitorar relatórios, envolve a estatística dos dados

    - Amazon CloudTrail: registra atividade da conta AWS, envolve registrar todas chamadas na conta

    - Amazon Config: serve para auditorias e inventário de configurações.

- Menor privilégio: conceder às pessoas exatamente o nível de acesso que precisam e nada mais.

- Criptografia: de dados em trânsito e dados em repouso

- Recursos de gerenciamento de acesso

    Nem todos que usam uma conta na AWS precisam do mesmo nível de acesso, e para controlar como as pessoas usam os serviços da AWS é preciso uma maneira de controlar o nível de acesso que elas têm.

    - AWS Identify and Access Management (IAM)

    - Usuário-raiz: o usuário inical, que tem acesso a tudo assim que uma conta é criada. O acesso é completo e irrestrita a todos os recursos, porém não se deve usar esse usuário para realizar tarefas diárias na AWS.

    - Usuários

    - Grupos

    - Perfis: são identidades usadas que dão credenciais temporárias.

    - Políticas gerenciadas e políticas não gerenciadas

#

### Tecnologias

- Defina os métodos de implantação e operações na AWS

    - Métodos para comunicação com AWS Cloud 

        - APIs e SDKs
        
        - AWS Command Line Interface (CLI)

        - AWS Management Console

        - Insfraestrutura como código (IaC)

    - Modelos de implantação na nuvem: métodos de utilização da nuvem

        - Nativo da nuvem ou integral com nuvem

        - Híbrido

        - On-premises
        
    - Opções de conexão: rede privada virtual (VPN), AWS Direct Connect e Internet pública

- Infraestrutura Global: zonas de disponibilidade, regiões e locais de borda da AWS.

- As principais categorias de serviços da AWS são: compuatação, armazenamento, redes e banco de dados.

- O suporte pode incluir auxílio no projeto, orientação na arquitetura, resolução de problemas e colaboração da comunidade.

    - Documentação

    - Suporte específica da conta

    - AWS Partner Network (APN)

    - AWS Trusted Advisor

#

### Modelos de preço da AWS

- Modelos de preço da Amazon EC2

    - Instâncias sob demanda

    - Instâncias reservados

    - Instâncias spot

# 